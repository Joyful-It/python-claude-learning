# 学习会话记录 - 2026-06-08

## 今日理解跃迁

> 从"State/TypedDict/Tool/Node 糊在一起" → "State=数据说明书，Node=干活函数，Tool=普通函数，ToolNode=工具执行器，LLM=大脑，五个概念各司其职"

---

## 会话概览

- **日期**：2026-06-08
- **核心主题**：LangGraph 核心概念拆解（State/Node/Tool/ToolNode/LLM/类型注解）+ demoscore/demo_weanotool/demo_weatool 实战调试
- **代码文件**：`Agent/langgraph/demoscore.py`、`Agent/langgraph/demo_weanotool.py`、`Agent/langgraph/demo_weatool.py`
- **晨考状态**：⚠️ 中断未完成（Bank 8/8 完成，注入层仅答第9题三元运算符，剩余9题待继续）

---

## 学员提出的问题（原文）

- "这两个message区别在哪" — MessagesState vs HumanMessage
- "city = 已经是 'beijing' 不是我最后才将北京和30传入进去的吗" — State 字段的写入与读取时机
- "为什么city不用return返回呢" — LangGraph 节点返回值规则
- "这个model是什么库" — from model import llm 中的 model 是自定义模块
- "这个代码问题在哪" — demo_weatool.py StateGraph 参数错误
- "能查看这个文件吗" — demo_weanotool.py

---

## 概念与教学内容

### 核心突破：LangGraph 六概念拆解（学员自主总结）

学员在今日会话末尾，独立将最容易混淆的六个概念拆开并写出总结。这是本次会话**最有价值的产出**。

#### 1. LangGraph 本质

> LangGraph = 把流程图变成代码

```text
判断 → 执行 → 结束  就是图的逻辑
Node = 干活
Edge = 控制流程
State = 流程中的共享数据
```

#### 2. Node 节点

对 LangGraph 来说，只要满足 `输入 State → 输出 dict` 的函数就是 Node。不管里面是手动调 LLM 还是调工具，都是 Node。

#### 3. State 状态

`class State(TypedDict)` 不是数据，是**数据格式说明书**。

真正的数据是 `{"score": 80, "grade": ""}` 这样的 dict。

`state: State` 意思是「变量 state，符合 State 结构」，不是「state 等于 State」。

类比：`name: str` → name 是变量，str 是类型。

#### 4. TypedDict

规定字典里应该有哪些字段，IDE 可以检查拼写错误。本质 = State 结构说明书。

#### 5. Annotated 与 add_messages

- 默认 `return {"messages": [...]}` → **覆盖**
- `Annotated[list, add_messages]` → **追加**（聊天记录必须用，否则 Agent 失忆）

MessagesState = 官方帮你写好的带 add_messages 的 messages 列表。

#### 6. Tool 工具

`@tool` 装饰的普通 Python 函数。它不知道 state 是什么，只管收参数、返回结果。

**Tool ≠ State**

#### 7. ToolNode

作用 = 帮 Agent 执行工具。流程：LLM 决定调工具 → ToolNode 执行 → 结果写回 State。

学员自己的项目（客服）里，`judge()` / `classify()` 是手动 `llm.invoke(...)`，不需要 ToolNode。

#### 8. LLM 与 Tool 的区别（学员金句）

```text
LLM = 大脑（思考/分类/判断/生成）
Tool = 手脚（执行具体动作）
LLM 不是 Tool，Tool 不是 LLM
```

### 其他概念

**MessagesState vs HumanMessage**：

| | MessagesState | HumanMessage |
|---|---|---|
| 来源 | langgraph.graph | langchain_core.messages |
| 是什么 | 状态容器（聊天记录笔记本） | 一条消息（用户在笔记本里写的一行） |
| 用法 | StateGraph 的状态类型 | 创建用户消息放进 messages |

**`from model import llm`**：model 不是第三方库，是自定义本地模块（封装 LLM 初始化），需自己创建 `Agent/langgraph/model.py`。

---

## 踩坑与纠正

### demo_weanotool.py 踩坑

| 错误 | 原因 | 正确 |
|------|------|------|
| `city = state['city'],` | 末尾逗号 → Python 自动变成元组 `('beijing',)` | 去掉逗号：`city = state['city']` |
| `return f"...is {temputer}"` | 节点返回了字符串，LangGraph 要 dict | `return {"temputer": temputer}` |
| 节点名 `huodetiansqi` vs 边 `huodetianqi` | 少打了一个 `s`，找不到节点 | 名字统一 |
| `return f"...{"temputer"}"` | 双引号套双引号语法错误 + 引用了字符串字面量而非变量 | `return f"...{temputer}"` |

### demo_weatool.py 踩坑

| 错误 | 原因 | 正确 |
|------|------|------|
| `StateGraph(weather)` | StateGraph 要状态类型（TypedDict），传了函数 | 先定义 `class WeatherState(TypedDict)`，再传类 |
| `invoke("beijign")` | invoke 要 dict，传了裸字符串；还有拼写错误 | `invoke({"city": "beijing"})` |

### demoscore.py 踩坑（06-06 遗留）

| Bug | 说明 | 正确 |
|-----|------|------|
| `Score['score']` | Score 是类名，不是实例 | `state['score']` — 学员自主发现 ✅ |
| `"score": "61"` | score 类型是 int，传了 str | `"score": 61` |

---

## 今日核心理解

以下为学员**原话**（不润色），独立总结的 LangGraph 六概念拆解：

> "LangGraph = 把流程图变成代码。Node = 干活，Edge = 控制流程，State = 流程中的共享数据"

> "class State(TypedDict) 不是数据，这是数据格式说明书"

> "state: State 意思不是 state 等于 State，而是变量 state 符合 State 结构。就像 name: str → name 是变量，str 是类型"

> "LLM 不是 Tool，Tool 不是 LLM。LLM = 大脑，Tool = 手脚"

> "ToolNode = 帮 Agent 执行工具。我自己的客服项目里不需要 ToolNode，因为我是手动 llm.invoke()"

> "State 是全局的，city 在 invoke 时就写进去了，节点读它用它，但没有改它，所以不用返回它"

学员最终形成的认知模型：

```text
State → Node → LLM思考 → 决定是否调用Tool → ToolNode执行Tool → 结果写回State → 下一节点
```

---

## 知识漏洞

- ~~State 与 TypedDict 混淆~~ → ✅ 已贯通（学员独立拆解「数据格式说明书」vs「数据」）
- ~~state 变量 vs State 类型混淆~~ → ✅ 已贯通（name:str 类比）
- ~~节点返回值规则~~ → ✅ 已贯通（只返回修改的字段）
- ~~Tool vs ToolNode vs Node 混淆~~ → ✅ 已贯通（学员画出完整链路图）
- LangGraph 条件边（Conditional Edge）🆕 → 下一步
- ReAct Agent 完整流程 🆕 → 下一步
- LangGraph demo_weatool.py 含 ToolNode 版本 → 待实操

---

## 关键总结

### LangGraph 六概念口诀（学员原创）

```
State = 数据说明书（TypedDict）
Node = 干活函数（收 State 返 dict）
Tool = 普通函数（不知道 State 存在）
ToolNode = 工具执行器（帮 Agent 跑 Tool）
LLM = 大脑（思考/判断/生成）
add_messages = 追加不覆盖（聊天记忆必备）
```

### MessagesState 口诀

```
MessagesState 是聊天框
HumanMessage 是用户发的一句话
```

### 节点返回值原则

```
读过的不用还，改了的必须写
没改任何字段 → return {}
```

---

## 完成的练习

- demoscore.py 两个 bug 识别与修复（Score['score']→state['score']，学员自主；"61"→61，类型匹配）
- demo_weanotool.py 三个 bug 排查（元组逗号、节点返回字符串、节点名不一致）
- demo_weatool.py 两个问题诊断（StateGraph 参数错误、invoke 参数错误）
- LangGraph 六概念独立拆解总结

---

## 学习效果评估

| 考点 | 前值 | 后值 | 备注 |
|------|------|------|------|
| State/TypedDict 认知 | 30% | 85% | 学员独立写出「数据格式说明书」类比 |
| state 变量 vs State 类型 | 20% | 85% | name:str 类比完全贯通 |
| Node 本质理解 | 40% | 80% | 输入 State→输出 dict 即节点 |
| Tool vs ToolNode | 0% | 75% | 首次接触，学员画出完整链路 |
| LLM vs Tool | 30% | 80% | 大脑 vs 手脚 金句 |
| LangGraph 整体认知 | 20% | 70% | 能独立画流程图 |

---

## 晨考状态

⚠️ **06-08 晨考中断，待下次继续**

- Bank 层：8/8 完成
- 注入层：仅第9题（Python三元运算符）已答
- 剩余：注入层 ~9 题待继续

**Bank 层薄弱点记录**：
- fit_transform 学规矩 vs 用规矩
- 蒸馏 T>1 = 暗知识显形（非确定性）
- Tokenizer 四步流程
- sklearn 五步缺标准化和评估
- view vs reshape 区别
