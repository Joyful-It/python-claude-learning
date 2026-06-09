# AI大模型开发48之Langchain二和RAG一

> 作者：AI芯源邢朋辉



# 0.课程内容

## 0.1晨考



## 0.2 课程回顾

Agent 智能体（智能系统）=LLM(大模型)+Tools(工具) 实现的ReAct(循环决策)的智能系统

开发Agent的主流技术栈：LangChain

LangChain1.0+

智能体开发步骤：

1.模型 

2.工具函数

3.智能体

核心模型：

1.Model

模型，支持主流模型的调用

执行推理有三种方式：

​	1.invoke

​	2.stream

​	3.betch

2.Tools

工具函数

智能体不仅依赖于大模型，还可以通过调用函数，来弥补大模型的不足（1.实时性数据 2.精确计算 3.复杂逻辑 4.其他工具(软件)等操作）

工具函数的定义：

1.普通的Python函数

2.@tool装饰器修饰函数，可以额外设置信息

> 函数的文档注释，告诉大模型什么时候调用

3.Agent

构建智能体

create_agent



> 可以基于LangChain实现Agent开发



# 1.Langchain核心模块

## 1.1 LangChain基础模块

Model模块

Tools模块

Agent模块



示例：

```python
# Langchain 核心操作
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage
from langchain.tools import tool

# 创建模型
model=ChatOpenAI(
    model="deepseek-v4-flash",
    open_api_key="",
    base_url="",
    temperature=1,
    max_tokens=1024,
    timeout=3000
)
# 定义工具函数
def clac_num(num1:int,num2:int,op:str)->str:
    """
     进行数学运算
     如果涉及到数字的数学运算就调用
    :param num1: 第一个数字
    :param num2: 第二个数字
    :param op: 操作符 + - * /
    :return: 运算结果
    """
    if op=="+":
        return num1+num2
    elif op=="-":
        return num1-num2
    elif op=="*":
        return num1*num2
    elif op=="/":
        if num2!=0:
            return num1/num2
        else:
            return f"{num2}除数不能为0"
# 创建智能体
agent=create_agent(
    model=model,
    tools=[clac_num],
    system_prompt="你是一个很强的数学老师！"
)
# 使用智能体
r1=agent.invoke({"messages":[HumanMessage("计算11和34的和，给出解释！")]})
print(r1["messages"][-1])
```

`create_agent` 核心实现的是 **ReAct (Reasoning + Acting)** 循环：

│                  ReAct 循环

│   1. Agent 接收消息（用户问题 + 历史）

│              ↓                                 │

│   2. 调用 LLM → LLM 决策： 

│      ├─ 直接回答 → 返回结果（循环结束）

│      └─ 调用工具 → 生成 tool_calls

│              ↓                                 │

│   3. 执行工具 → 生成 ToolMessage 

│              ↓                                 │

│   4. 将工具结果追加到消息列表│              ↓                                 │

│   5. 回到步骤 2（再次调用 LLM）

│   直到 LLM 不再调用工具 → 返回最终回答

## 1.2 记忆

记忆（Memory）是一个能够记住先前交互信息的系统。对于 AI 智能体（agent）而言，记忆至关重要，因为它能让智能体记住之前的交互、从反馈中学习并适应用户偏好。

Agent 本身是**无状态的**。"记忆"本质上是把之前的对话保存下来，下次请求时全部塞进 Context。

checkpointer可以实现Agent的记忆

聊天对话数据存储到内存或数据库中



## 1.3 中间件

中间件提供了一种更精细控制智能体内部行为的方式。

Middleware 是 LangChain v1.x 的**核心创新**——借鉴了 Web 框架（Express/Django）的洋葱模型，让你无需修改业务逻辑就能注入安全、监控、限流等横切逻辑。

![1780456627069](D:\class\2603\随堂笔记\第十周\AI大模型开发48之Langchain二和RAG一.assets\1780456627069.png)

| **Hook**          | **执行时机**           | **典型用途**           |
| ----------------- | ---------------------- | ---------------------- |
| `before_agent`    | Agent 启动前（仅一次） | 全局初始化、环境校验   |
| `before_model`    | 每次模型调用前         | PII 脱敏、上下文摘要   |
| `wrap_model_call` | 包裹模型调用过程       | 缓存、熔断、模型切换   |
| `after_model`     | 每次模型调用后         | 输出校验、人工审批拦截 |
| `wrap_tool_call`  | 包裹工具调用过程       | 重试、权限校验         |
| `after_agent`     | Agent 结束后（仅一次） | 资源清理、计费日志     |

LangChain 为常见用例提供了预构建的中间件。每个中间件都是生产就绪的，并且可以根据具体需求进行配置。

中间件适用于任何 LLM 提供商：

| 中间件                                                       | 描述                                          |
| ------------------------------------------------------------ | --------------------------------------------- |
| [摘要](https://langchain.longbao.wang/oss/python/langchain/middleware/built-in#summarization) | 在接近令牌限制时自动总结对话历史。            |
| [人在回路](https://langchain.longbao.wang/oss/python/langchain/middleware/built-in#human-in-the-loop) | 暂停执行以等待人工批准工具调用。              |
| [模型调用限制](https://langchain.longbao.wang/oss/python/langchain/middleware/built-in#model-call-limit) | 限制模型调用次数以防止成本过高。              |
| [工具调用限制](https://langchain.longbao.wang/oss/python/langchain/middleware/built-in#tool-call-limit) | 通过限制调用次数来控制工具执行。              |
| [模型回退](https://langchain.longbao.wang/oss/python/langchain/middleware/built-in#model-fallback) | 当主模型失败时自动回退到备用模型。            |
| [PII 检测](https://langchain.longbao.wang/oss/python/langchain/middleware/built-in#pii-detection) | 检测和处理个人身份信息 (PII)。                |
| [待办事项列表](https://langchain.longbao.wang/oss/python/langchain/middleware/built-in#to-do-list) | 为智能体配备任务规划和跟踪能力。              |
| [LLM 工具选择器](https://langchain.longbao.wang/oss/python/langchain/middleware/built-in#llm-tool-selector) | 在调用主模型之前使用 LLM 选择相关工具。       |
| [工具重试](https://langchain.longbao.wang/oss/python/langchain/middleware/built-in#tool-retry) | 使用指数退避自动重试失败的工具调用。          |
| [模型重试](https://langchain.longbao.wang/oss/python/langchain/middleware/built-in#model-retry) | 使用指数退避自动重试失败的模型调用。          |
| [LLM 工具模拟器](https://langchain.longbao.wang/oss/python/langchain/middleware/built-in#llm-tool-emulator) | 使用 LLM 模拟工具执行以进行测试。             |
| [上下文编辑](https://langchain.longbao.wang/oss/python/langchain/middleware/built-in#context-editing) | 通过修剪或清除工具使用来管理对话上下文。      |
| [Shell 工具](https://langchain.longbao.wang/oss/python/langchain/middleware/built-in#shell-tool) | 向智能体暴露一个持久的 shell 会话以执行命令。 |
| [文件搜索](https://langchain.longbao.wang/oss/python/langchain/middleware/built-in#file-search) | 提供对文件系统文件的 Glob 和 Grep 搜索工具。  |

自定义中间件

通过实现钩子（hooks）在智能体执行流程的特定节点运行，来构建自定义中间件。

节点式钩子

在特定的执行节点顺序运行。用于日志记录、验证和状态更新。

**可用钩子：**

- `before_agent` - 在智能体启动前（每次调用一次）
- `before_model` - 在每次模型调用前
- `after_model` - 在每次模型响应后
- `after_agent` - 在智能体完成后（每次调用一次）

包装式钩子

拦截执行并控制何时调用处理器。用于重试、缓存和转换。

你可以决定处理器被调用零次（短路）、一次（正常流程）或多次（重试逻辑）。

**可用钩子：**

- `wrap_model_call` - 围绕每次模型调用
- `wrap_tool_call` - 围绕每次工具调用

基本使用对应的节点或包装式函数

```python
# Agent 中间件 生命周期
from typing import Any
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage
from langchain.tools import tool
from langchain.agents.middleware import before_agent, after_agent, before_model, after_model, wrap_model_call, \
    wrap_tool_call, ModelResponse

# 模型
model=ChatOpenAI(
    model="deepseek-v4-flash",
    openai_api_key="sk-bf6b5981d3694f358df92886d9978605",
    base_url="https://api.deepseek.com/",
)

# 中间件函数
# 节点  函数要求：1.参数 固定 2.模型相关 返回值必须为字典类型
# 中间件执行前
@before_agent
def fun1(state, runtime):
    print(f"即将开始执行 {state} ")
@after_agent
def fun2(state, runtime):
    print(f"执行完成 {runtime} ！")
@before_model
def fun3(state, runtime) -> dict[str, Any] | None:
    print(f"模型执行前：{state}")
    return None
@after_model
def fun4(state, runtime) -> dict[str, Any] | None:
    print(f"模型执行后：{runtime}")
    return None

# 包装式 函数返回值 ModelResponse 通过 handler(request)
@wrap_model_call
def fun5(request, handler) -> ModelResponse:
    print("模型执行前后")
    return handler(request)

@wrap_tool_call
def fun6(request,handler) -> ModelResponse:
    print("工具函数执行前后")
    return handler(request)


# 工具函数
@tool
def fun7(name:str)->str:
    """ 查询班级的同学实时信息 """
    return f"{name}的详细信息如下所示：成绩 A+"

# 智能体
agent=create_agent(
    model=model,
    tools=[fun7],
    middleware=[fun1,fun2,fun3,fun4,fun5,fun6],
    name="超级助手"
)
# 调用
r1=agent.invoke({"messages":[{"role":"user","content":"我想知道朱子龙的详细信息"}]})
print("AI回复：")
print(r1["messages"][-1])
# r2=agent.invoke({"messages":[HumanMessage("饿了，不知道中午想吃什么？推荐一下")]})
# print("AI回复：")
# print(r2["messages"][-1])
```

![1780459174288](D:\class\2603\随堂笔记\第十周\AI大模型开发48之Langchain二和RAG一.assets\1780459174288.png)

> 节点式钩子
>
> 自定义函数的要求：
>
> ​	1.参数 2个参数，第一个为state 第二个为runtime
>
> ​	2.返回值 模型前后的钩子函数，返回值要求必须为字典类型
>
> 包装式钩子
>
> ​	1.参数 2个参数，第一个request 第二个handler
>
> ​	2.返回值 必须为ModelResponse 

动态提示词，需要使用装饰器：@`dynamic_prompt` 

可以根据输入的内容，动态设置提示词

动态模型选择，需要装饰器：@wrap_model_call（包装式钩子）

可以进行模型的动态指定

## 1.4 多Agent

单个 Agent 能力有限。当任务复杂时，需要多个专家 Agent 协作。

Supervisor 多智能实现流程如下所示：

用户请求 → [Supervisor 主管Agent] → 分析任务

​                ├─→ [日历Agent] → 处理日程相关

​                ├─→ [邮件Agent] → 处理邮件相关

​                └─→ [搜索Agent] → 处理信息查询

​                        ↓

​              [Supervisor] 汇总结果 → 返回用户

示例代码：

```python
# 多Agent
from typing import Any, TypedDict
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage
from langchain.tools import tool

# 准备模型
model=ChatOpenAI(
    model="deepseek-v4-flash",
    openai_api_key="sk-bf6b5981d3694f358df92886d9978605",
    base_url="https://api.deepseek.com/",
)
# 定义第一个Agent
@tool
def send_email(email, message)->str:
    """ 发送邮件 """
    if len(email)>0 and len(message)>0:
        return f"发送邮件：{email}: {message}"
    else:
        return "邮件发送失败，请检查内容"
# 智能体
email_agent=create_agent(
    model=model,
    tools=[send_email],
    system_prompt="你是一个发送邮件小助手"
)

# 第二个智能体
@tool
def add_plan(title,message)->str:
    """ 实现日程计划的安排 """
    with open("plan.txt","a",encoding="utf-8") as f:
        f.writelines(f"{title}\n{message}\n")
        f.flush()
    return "日程计划安排已完成！"
# 智能体
plan_agent=create_agent(
    model=model,
    tools=[add_plan],
    system_prompt="你是一个日程计划安排小助手"
)
# 多智能体对象 一个智能体
@tool
def send_email_a(question:str)->str:
    """ 发送邮件 """
    return email_agent.invoke({"messages":[{"role":"user","content":f"{question}"}]})
@tool
def send_plan(question:str)->str:
    """ 实现日程计划的安排 """
    return plan_agent.invoke({"messages":[{"role":"user","content":f"{question}"}]})
# 智能体
supervisor=create_agent(
    model=model,
    tools=[send_plan,send_email_a],
    system_prompt="你是一个超强的个人助手"
)
# 调用
r1=supervisor.invoke({"messages":[{"role":"user","content":"我需要在明天下午开个会，需要提前发送邮件给xingfei_work@163.com"}]})
print("AI回复：")
print(r1["messages"][-1])

```



# 2.RAG

**RAG**（Retrieval-Augmented Generation，检索增强生成）是一种让大模型"先查资料再回答"的技术架构。

RAG执行流程：

用户提问 → 检索知识库 → 获取相关文档 → 喂给 LLM → 生成回答

为什么需要 RAG？

| **痛点**     | **纯 LLM**             | **RAG 方案**               |
| ------------ | ---------------------- | -------------------------- |
| **知识滞后** | 模型知识截止于训练日期 | 实时接入最新数据           |
| **幻觉问题** | 可能编造答案           | 基于检索结果生成，有据可查 |
| **私有数据** | 模型没学过你的内部文档 | 检索企业知识库回答         |
| **成本**     | 微调成本高             | 无需训练，即插即用         |

RAG vs 传统方案

| **方案**       | **原理**            | **优点**           | **缺点**         |
| -------------- | ------------------- | ------------------ | ---------------- |
| 传统数据库     | SQL 精确匹配        | 精确、快速         | 只支持结构化数据 |
| 全文检索（ES） | 倒排索引 + BM25     | 文本搜索快         | 无法理解语义     |
| **RAG**        | 向量检索 + LLM 生成 | 理解语义、生成答案 | 有一定延迟       |

# 3.综合练习

### 带记忆和中间件的客服 Agent


 **知识点**：Checkpointer 对话记忆、PIIMiddleware 脱敏、SummarizationMiddleware、SqliteSaver、工具定义与结构化参数  

**背景**
 多轮对话是客服场景的基础，同时需要保护用户隐私并控制上下文长度。构建一个智能客服 Agent。



# 4.今日总结

1.LangChain核心模块

Model

Agent

Tools

Memory

Middleware

2.RAG



# 5.作业

### Supervisor 多 Agent 协作

 **知识点**：子 Agent 包装为工具、多 Agent 架构、任务路由、自然语言到结构化参数转换  

**背景**
 请实现一个简易的多 Agent 系统，同时处理信息查询和数学计算两类任务。