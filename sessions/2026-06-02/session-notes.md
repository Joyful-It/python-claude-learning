# 学习会话记录 - 2026-06-02

## 今日理解跃迁

> 从"Agent 就是有知识库的聊天机器人" → "Agent 核心是自主决策调用工具，ReAct 循环：思考→行动→观察→再输出"

---

## 会话概览

- **日期**：2026-06-02
- **核心主题**：LangChain 入门——Agent 开发三大核心模块
- **代码文件**：`Agent/langchain/demo.py`、`Agent/langchain/6月2.py`

---

## 学员提出的问题（原文）

- "langchain怎么下载"
- "RAG和微调是什么区别，什么时候需要微调，harness和RAG区别"
- "langchain要学的东西都有哪些"
- "init_chat_model 这个不是标准的吧，这个意思是只能聊天是吧"
- "写注释文档便于agent查看，可以使用普通注释吗"

---

## 概念与教学内容

### 1. Harness vs RAG vs Agent

| 概念 | 一句话 | 层级 |
|------|------|------|
| RAG | 检索外部文档增强生成，开卷考试 | 应用层技术 |
| Agent | 自主决策调用工具，完成复杂任务 | 应用层框架 |
| Harness | 大模型工程缰绳，覆盖推理/API/监控/安全全链路 | 基础设施层 |

**关系**：RAG ⊂ Harness，Agent ⊂ Harness。RAG 和 Agent 都是 Harness 体系中的可插拔组件。

### 2. RAG vs 微调

| | RAG | 微调 |
|------|------|------|
| 知识在哪 | 外部文档 | 模型权重内 |
| 更新成本 | 换文档，秒级 | 重新训练 |
| 适用场景 | 需引用来源、频繁更新 | 改风格/推理方式/专业术语 |
| 口诀 | 改知识用RAG | 改能力用微调 |

### 3. LangChain 三大核心模块

| 模块 | 核心 API | 要点 |
|------|------|------|
| Model | `invoke` / `stream` / `batch` | 三种调用：一次性/流式/批量并行 |
| Tools | `@tool` 装饰器 + 文档注释 | 文档注释是给模型看的工具说明书，`#`注释模型读不到 |
| Agent | `create_agent(model, tools, system_prompt)` | 组装模型+工具+人设 |

### 4. Agent 内部 ReAct 循环

```
用户问 → 模型思考(该调哪个工具) → 调工具执行 → 拿到结果 → 模型再思考 → 输出最终答案
```

不是一次调用出结果，是**至少两轮模型调用**：第一轮决定工具调用，第二轮消化工具结果。

### 5. `@tool` vs 裸函数

```python
# 裸函数 —— 也能用，但工具描述不完整
def get_weather(city):
    """查询天气"""
    ...

# 标准写法 —— @tool 显式标记，自动提取签名+文档作为工具说明
@tool
def get_weather(city) -> str:
    """查询指定城市的天气信息"""
    ...
```

---

## 今日核心理解

学员对 Agent 本质的理解：
> "agent可以有知识库，确保安全性有限制范围" ← 这是RAG的特点
> 纠正后：Agent 核心是**自主决策调用工具**，不是知识库

学员对 ReAct 循环的理解：
> "发生了抉择时用那个工具那个agent 中间需要很多步骤"

---

## 踩坑与纠正

| 错误 | 纠正 | 原因 |
|------|------|------|
| LangChain 是"神经" | LangChain 是工具链编排框架，不是神经网络 | 名字带"chain"容易联想神经网络 |
| `#` 普通注释能给 model 看 | `#` 运行时丢弃，`"""文档注释"""` 存在 `__doc__` 里 LangChain 才能读 | Python 底层机制 |
| `api_ley` 拼写错误 | `api_key` | 手误 |
| `print(res)` 打 generator 对象 | stream 返回生成器，需 for 循环遍历 | stream 是惰性求值 |
| Agent 有知识库 | Agent 是有工具调用能力，知识库是 RAG | 概念混淆 |

---

## 知识漏洞

- `#` vs `""" """` 的底层区别刚建立，需巩固
- Harness 概念刚接触（0%→15%），后续 E 模块深入

---

## 关键总结

**LangChain 万能公式**：
```
Agent = Model + Tools + system_prompt
```

**Model 三种调用口诀**：
> invoke 等全部，stream 逐字蹦，batch 群发并行

**Tools 铁律**：
> `@tool` 装饰器 + `"""文档注释"""`（给模型看，不是 `#`）

**Harness vs RAG 一句话**：
> RAG 解决"模型怎么查资料"，Harness 解决"模型怎么稳定上线"

---

## 完成的练习

- `Agent/langchain/demo.py`：老师课堂示例，修复 `langchain-deepseek` 缺失和 `api_key` 拼写
- `Agent/langchain/6月2.py`：独立完成小学老师智能体（语数英三工具 + stream 调用成功）

---

## 学习效果评估

| 考点 | 前值 | 后值 | 备注 |
|------|------|------|------|
| LangChain 三大模块 | 0% | 55% | Model/Tools/Agent 概念清晰，独立写出 |
| ReAct 循环 | 0% | 50% | 理解两轮模型调用流程 |
| @tool 装饰器 | 0% | 60% | 理解了 vs 裸函数的区别 |
| Harness 概念 | 0% | 15% | 刚建立认知，后续深入 |
| C 模块 Agent | 0% | 10% | 首次开荒 |
| B 模块 RAG | 0% | 10% | 首次开荒 |

---

## 补充：transform_all.py 代码审查 + 任务梳理

### 学员操作
- 打开 `torch_pre/transform_all.py` 审查是否有 bug

### 踩坑与纠正（新增）

| 错误 | 纠正 | 原因 |
|------|------|------|
| 我以为 `processing_class=` 是拼写错误，改成 `tokenizer=` | 查 HuggingFace 最新文档后发现 **`processing_class` 才是新版 API**，`tokenizer` 已弃用 | HuggingFace 从纯文本向多模态演进，`processing_class` 可接收 tokenizer/image_processor/feature_extractor |

**教训**：不确定就查，不靠猜。GitHub Issue #37734 确认了此变更。

### transform_all.py 最终结论
- ✅ 代码无 bug，`processing_class=tokenizer` 是新版正确写法
- ✅ 六件套导入齐全，数据流完整，骨架清晰
- ⚠️ `fp16=True` 需 GPU，本地 CPU 会报错
- 📌 后续复习重点：常用参数、六件套库、训练骨架、关键语句

### 愿望清单全量梳理
从 tracker 重新梳理全部待办：

**愿望清单**：11 项未完成（代码实操 6 + 论文 4 + 理论 3，已完 2）
**知识漏洞**：14 项未解决（SQLAlchemy 🔴、sklearn 默写 🔴、GridSearchCV 🟡 等）
**课件未看**：Matplotlib/Seaborn、SQLAlchemy
**常犯错误**：5 条模式性错误仍在活跃

### 下一步决策
首推 **泰坦尼克号 PyTorch 独立重现**（试金石，检验 F 模块真实水平），明天开干。
