# 2026-06-09 会话笔记

## 今日理解跃迁

前半场：从"interrupt=暂停"的模糊认知 → 完整理解 Human-in-the-Loop 的七步全流程
后半场：Transformer 手搓起步——QKV 投影从"知道公式" → "用 PyTorch 矩阵乘法亲手算出来，弄清形状变化"

## 会话概览

- **日期**：2026-06-09
- **核心主题**：LangGraph Human-in-the-Loop（人工审批）完整机制
- **代码文件**：[demo3_2_hum_loop.py](../Agent/langgraph/demo3_2_hum_loop.py)

## 学员提出的问题

1. "这段代码是审批消息，如果实战里面，在哪传入消息人工去审批呢？"
2. "如果我想审批很多东西怎么办？"
3. "interrupt中的message和state中的message是一个吗？"
4. "AIMessage是什么东西呢？"
5. "你修改了哪些？"

## 概念与教学内容

### 1. Human-in-the-Loop 全流程（核心）

**Q：人工审批的完整流程是怎样的？**
**A：**
```
invoke(初始state) → gen_message(生成content)
    ↓
jud_message → interrupt()暂停，抛content给人看
    ↓
人看到内容，决定 approve/reject
    ↓
Command(resume={"approved": True/False}) 把决定塞回 review 变量
    ↓
publish_message 根据 approved 决定发布/拒绝
```

### 2. interrupt() 抛出的不是整个State

- `interrupt({...})` 只抛出花括号里的内容，不是全部 state
- 人看不到 `thread_id`、历史消息、内部状态——只看到需要审批的内容
- 设计理念：你决定给人看什么，不给什么

### 3. state["message"] vs interrupt({"message": ...}) 同名不同物

| | `state["message"]` | `interrupt({"message":...})` |
|---|---|---|
| 类型 | list（消息列表） | str（提示文字） |
| 谁用 | 图内部流转 | 抛给人类看 |
| 作用 | 存对话历史 | 告诉人"请审批" |

→ 学员立刻联想到之前 weather/TypedDict 同名覆写的坑，这次一眼看穿

### 4. AIMessage = AI 说的消息

| 消息类型 | 谁说的 |
|---------|--------|
| HumanMessage | 用户 |
| AIMessage | AI/系统 |
| ToolMessage | 工具执行结果 |

`add_messages` 靠消息类型判断合并方式——消息类型是 LangGraph 消息流的"身份证"

### 5. MemorySaver = 记忆系统

`checkpointer=MemorySaver()` 保存：State + 当前执行位置 + 节点上下文

为什么需要？因为 `interrupt()` 暂停后可能等5分钟甚至更久，没有 checkpointer 系统就忘了

### 6. thread_id = 存档编号

```python
config = {"configurable": {"thread_id": "task-001"}}
```

MemorySaver 内部结构：
```python
{"task-001": {state...}, "task-002": {state...}}
```

恢复时 thread_id 必须一致，否则找不到之前的状态

### 7. Command(resume=...) 不是更新 State

关键理解：`Command(resume={"approved": True})` 不是直接改 State，而是**把数据送回 interrupt() 暂停的位置**，赋值给 `review` 变量。

相当于：
```python
review = {"approved": True}  # resume 之后 review 才获得值
```

然后节点 `return {"approved": review["approved"]}` 才更新 State。

## 今日核心理解

### 学员自己的完整总结（原话，不润色）

以下为学员独立完成的 LangGraph Human-in-the-Loop 全程拆解：

---

**纠错**：代码中 `Command(resume={"approved": cmd: "approve"})` 应为 `Command(resume={"approved": cmd == "approve"})`，这里是判断相等返回 True/False。

---

**第一部分：graph.compile(checkpointer=memory)**

```python
memory = MemorySaver()
graph = builder.compile(checkpointer=memory)
```

翻译：把设计图(builder)编译成真正能运行的 graph，并且给 graph 安装一个记忆系统。

对比简单版 `app = flow.compile()` —— 多了 checkpointer 参数，意思是在运行过程中保存状态。

为什么需要保存？因为有 `interrupt()`。执行到 `interrupt()` 时暂停等待人工审批，如果不保存，用户5分钟后审批系统早忘了当前在哪个节点、State 是什么。

MemorySaver() 负责保存：State + 当前执行位置 + 节点上下文。

---

**第二部分：config**

```python
config = {"configurable": {"thread_id": "task-001"}}
```

thread_id = 任务编号。MemorySaver 内部是多槽位的，通过 thread_id 区分不同任务。恢复时 thread_id 必须一致，否则找不到之前的状态。

---

**第三部分：第一次 invoke**

```python
app.invoke({"content": "", "approved": False, "messages": []}, config)
```

传入的字典就是 State 实例，翻译：拿着这份 State 启动流程。

---

**第四部分：interrupt 发生了什么**

执行到 `review = interrupt({"messages": ..., "content": ...})` 时暂停。MemorySaver 记录 thread_id、state、current_node，然后程序停下来。

---

**第五部分：管理员审批**

```python
cmd = input("approve/reject")
```

输入 `approve` → `cmd == "approve"` → `True`

---

**第六部分：Command(resume=...)**

```python
Command(resume={"approved": True})
```

**关键理解**：这不是直接更新 State。它的真正意思是**把数据送回 interrupt()**。暂停时 `review` 没有值，resume 之后 `review` 变成 `{"approved": True}`。相当于 `review = {"approved": True}`。

---

**第七部分：LangGraph 更新 State**

节点 `return {"approved": True}` 后，LangGraph 自动合并到 State 中。

---

**面试级总结**：

> invoke(初始State, config) 用于启动或恢复图执行。
> checkpointer 负责保存 State 和执行位置。
> thread_id 用于标识同一个工作流实例。
> interrupt() 暂停执行并保存状态。
> Command(resume=...) 向 interrupt 返回数据并恢复执行。
> 节点 return 的 dict 会自动合并到 State 中。

---

### 第二部分：Transformer 手搓（注意力机制）

**Q：手搓的 Transformer 算是模型吗，和 ChatGPT/DeepSeek 区别？**
**A：** 手搓的是发动机（核心齿轮），ChatGPT/DeepSeek 是整车。GPT = Transformer Decoder 摞 96 层，核心齿轮一样，差别在规模+训练+工程细节。

**Q：Transformer 和深度神经网络什么关系？**
**A：** Transformer 就是深度神经网络。一个 Block 里藏着 6 个 Linear（Q/K/V/O + FFN×2），GPT-3 摞 96 个 Block = 576 个 Linear。只是把全连接打包进 Block，外面看不见。

**Q：特征在行还是列？**
**A：** PyTorch 里行是样本（字），列是特征。`(seq_len, d_model)`。规则：`(..., 特征数) @ (特征数, 新特征数)`。

**Q：Q、K、V 是 X 的分数吗？**
**A：** 不是。Q、K、V 是 X 的三种投影/三种身份。分数是 Q@K^T 碰出来之后的结果——(4,4) 方阵，第i行第j列=第i个字对第j个字的关注分数。

**Q：只有一个 X，怎么求和其他字的关系？**
**A：** 自注意力——4 个字都投影出 Q 和 K，然后 `Q @ K.T` → (4,4)，每行 = 当前字对所有字的关系。一句话内部互相看，这就是"自"注意力。

**Q：nn.Linear 行列坑是什么？**
**A：** `nn.Linear(输入, 输出)` 内部 weight 存成 `(输出, 输入)`——反的。内部算 `x @ W^T`，PyTorch 自己翻。记忆：`(..., in) @ (in, out) = (..., out)`。

**当前代码**（[handle_transform.py](../torch_pre/handle_transform.py)）：
```python
import torch
X = torch.randn(4, 512)          # 4个字，每个512维

W_Q = torch.randn(512, 64)       # Q投影矩阵 (512→64)
W_K = torch.randn(512, 64)       # K投影矩阵 (512→64)
W_V = torch.randn(512, 64)       # V投影矩阵 (512→64)

Q = X @ W_Q    # (4,512)@(512,64) = (4,64)
K = X @ W_K    # (4,512)@(512,64) = (4,64)
V = X @ W_V    # (4,512)@(512,64) = (4,64)
```

下一步待做：`attn_scores = Q @ K.T / sqrt(d_k)` → softmax → 权重 × V

---

## 踩坑与纠正

| 错误 | 发现方式 | 正确 | 原因 |
|------|---------|------|------|
| `false`（小写）作为 `.get()` 默认值 | 代码审查 | `False` | Python 小写 false 是未定义变量，只是碰巧 interrupt 返回总包含 approved 才没炸 |
| 审批前看不到待审内容（盲批） | 运行体验 | 用 `app.get_state(config).interrupts[0].value` 取 interrupt 数据打印 | interrupt 把内容抛出来了但 input() 没打印，管理员不知道在批什么 |
| emoji 炸 Windows GBK | 运行报错 | 去掉 emoji 用纯文本 | `\U0001f4cb` 在 GBK 编码下非法 |
| `cmd == "approve"` 笔误写成 `cmd: "approve"` | 学员自查 | `cmd == "approve"` | 冒号 vs 双等号 |
| K_Q / V_Q 命名混淆 | 代码审查 | 改为 W_K / W_V | 名字暗示"K的Q"让人困惑，应该是K的投影矩阵 |
| QKV 被说成"X的分数" | 概念纠正 | QKV是X的三种投影/身份，分数是QK^T之后产生的 | 分数是碰撞产物，不是投影本身 |

## 知识漏洞

无新增漏洞。学员对 LangGraph HITL 全程理解透彻，能独立拆解七步流程并用"面试级总结"输出。Transformer QKV 投影形状变化正确，命名和概念混淆已当场纠正。

## 关键总结

1. **Human-in-the-Loop 七步**：invoke → 节点执行 → interrupt暂停 → MemorySaver保存 → 人工输入 → Command(resume) 送回 → 节点return更新State
2. **interrupt ≠ state**：只抛出花括号内的内容
3. **Command(resume) ≠ 更新State**：是送回 interrupt 暂停点，赋值给 review 变量
4. **同名陷阱**：state.message（list）≠ interrupt.message（str），和 weather 那次一样
5. **AIMessage/HumanMessage/ToolMessage**：消息流的"身份证"

## 完成的练习

- [demo3_2_hum_loop.py](../Agent/langgraph/demo3_2_hum_loop.py) — 调试并跑通完整的 Human-in-the-Loop 审批流程
- [handle_transform.py](../torch_pre/handle_transform.py) — 手搓 Transformer 起步：QKV 三投影矩阵定义与计算

## 学习效果评估

- **LangGraph Human-in-the-Loop 理解度**：85%（学员能独立拆解全流程并输出面试级总结）
- **代码调试验证**：approve → reject 两条路径均跑通
- **Transformer QKV 投影**：形状运算正确 (4,512)→(4,64)，命名纠正后理解到位，下一步注意力分数计算
- **nn.Linear 行列坑**：复习后当场纠正，口诀"行是字，列是特征"
