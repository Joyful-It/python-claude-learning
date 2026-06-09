# AI大模型开发47Agent之RAG

> 作者：AI芯源邢朋辉

# 0.课程内容

## 0.1 晨考



## 0.2 课程回顾

Jupyter 在线的IDE

可以在线的进行编写Python代码，或写Markdown文档

特别适合做知识整理

JupyterLab

> 要求基于JupyterLab+AI编程工具完成个人知识栈的梳理和总结，同时完成求职的面试备战

提示词工程

更好的认知大模型

Zero 零样本，直接问即可

Few 少样本，给出少量的示例

CoT 思维链，一步步思考

ToT 思维树，多分支判断

ReAct 循环实现外部工具

Context 上下文工程



**大模型应用开发**

提示词

RAG

LangChain

Agent

LangGrash

Muilt-Agent

> Python、全栈开发，数据分析，机器学习，深度学习，Transformer，LLM，大模型微调，大模型压缩（大模型轻量化），大模型评测，大模型部署（推理加速），安全伦理

AI编程工具辅助（主导）开发，务必搞懂实现的代码，记忆核心的知识点，手动实现最小代码验证

特别是AI时代下，如何学习，如何记忆，都要之前简单



# 1.Agent



# 2.LangChain

## 2.1 LangChain

LangChain 是开始构建由大语言模型（LLM）驱动的智能体（agent）和应用程序的最简单方式。

开发Agent的库

基于LangChain可以轻松开发Agent

LangChain = 一个帮你把大模型（LLM）变成"应用"的工具箱

  没有 LangChain:
​    你每次都要自己写:
​      - 和 API 通信的代码
​      - 管理对话历史
​      - 让模型调用工具
​      - 组织 Prompt
​      - ...

  有了 LangChain:
​    这些都封装好了！你只管"搭积木"就行了。



## 2.2 环境安装

1.下载库

pip install langchain

2.导入使用

```
import langchain
print("版本号：",langchain.__version__)
```

3.验证版本号

![1780371891030](D:\class\2603\随堂笔记\第十周\AI大模型开发47Agent之RAG.assets\1780371891030.png)

## 2.3 初体验

基于LangChain实现Agent的开发

1.导入包

> 1.Agent 智能体
>
> 2.Model 大模型

```
# 导入
import random
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
```

2.定义 调用函数

> 必须写文档注释，必须和函数实现的功能一致

```python
# 定义函数 工具调用
def get_weather(city):
    """查询天气"""
    return f"{city}天气信息：晴天，25-36"
def get_num():
    """获取幸运数字"""
    return random.randint(1, 100)
```

3.实例化大模型对象

> 需要申请大模型的key，推荐使用deepseek

```python
# 准备模型
model=init_chat_model(
    model="deepseek-v4-flash", # 具体模型名称 全程
    api_key="sk-bf6b5981d3694f358df92886d9978605", # 模型的key
    model_provider="deepseek" # 大模型的名称 必须写指定
)
```

4.创建Agent

> 组装多个模块
>
> Agent的角色设定很重要

```
# 定义 Agent
agent=create_agent(
    model=model, # 设置对应的模型
    tools=[get_weather,get_num], # 设置可以调用的函数
    system_prompt="你是一个天气预报员，准确预报天气！" # 智能体角色设定
)
```

5.使用智能体

> 直接调用智能体，完成任务

```python
# 执行智能体
# 传递的消息必须为 标准的消息格式（大模型的消息格式一样）
res=agent.invoke(
    {"messages": [{"role": "user", "content": "杭州的天气"}]}
)
print(res)
```

6.查看运行结果

![1780372552352](D:\class\2603\随堂笔记\第十周\AI大模型开发47Agent之RAG.assets\1780372552352.png)

结果示例：

```json
{'messages': [HumanMessage(content='杭州的天气', additional_kwargs={}, response_metadata={}, id='0ebd8a9a-5faf-47e0-aeb7-e9c5ef68edc0'), AIMessage(content='', additional_kwargs={'refusal': None, 'reasoning_content': '用户想知道杭州的天气。我来调用get_weather工具查询杭州的天气。'}, response_metadata={'token_usage': {'completion_tokens': 62, 'prompt_tokens': 305, 'total_tokens': 367, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 17, 'rejected_prediction_tokens': None}, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 256}, 'prompt_cache_hit_tokens': 256, 'prompt_cache_miss_tokens': 49}, 'model_provider': 'deepseek', 'model_name': 'deepseek-v4-flash', 'system_fingerprint': 'fp_8b330d02d0_prod0820_fp8_kvcache_20260402', 'id': 'a4f75f51-0101-47a0-9651-574ec38f4850', 'finish_reason': 'tool_calls', 'logprobs': None}, id='lc_run--019e8663-9238-7af1-acbc-25f0c0a10b53-0', tool_calls=[{'name': 'get_weather', 'args': {'city': '杭州'}, 'id': 'call_00_5F9lIxbcIAVdbvMqqfGf9372', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 305, 'output_tokens': 62, 'total_tokens': 367, 'input_token_details': {'cache_read': 256}, 'output_token_details': {'reasoning': 17}}), ToolMessage(content='杭州天气信息：晴天，25-36', name='get_weather', id='dec73b68-b02c-4f03-9dcf-c6aa2ac451b0', tool_call_id='call_00_5F9lIxbcIAVdbvMqqfGf9372'), AIMessage(content='☀️ **杭州天气预报来啦！**\n\n- **天气状况：** 晴天 ☀️\n- **温度范围：** 25°C ~ 36°C\n\n今天杭州天气晴好，阳光充足，最高温度达到 **36°C**，体感较热，出门的话记得做好防晒措施，多喝水补充水分哦！祝您愉快度过这一天！😊', additional_kwargs={'refusal': None, 'reasoning_content': '杭州的天气信息已经获取到了。我来给用户做一个清晰的天气播报。'}, response_metadata={'token_usage': {'completion_tokens': 100, 'prompt_tokens': 388, 'total_tokens': 488, 'completion_tokens_details': {'accepted_prediction_tokens': None, 'audio_tokens': None, 'reasoning_tokens': 17, 'rejected_prediction_tokens': None}, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 256}, 'prompt_cache_hit_tokens': 256, 'prompt_cache_miss_tokens': 132}, 'model_provider': 'deepseek', 'model_name': 'deepseek-v4-flash', 'system_fingerprint': 'fp_8b330d02d0_prod0820_fp8_kvcache_20260402', 'id': '9c852dda-7627-4c20-8e28-06ef308a757a', 'finish_reason': 'stop', 'logprobs': None}, id='lc_run--019e8663-c1a7-7ab1-90bf-4ca337b0c7c0-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 388, 'output_tokens': 100, 'total_tokens': 488, 'input_token_details': {'cache_read': 256}, 'output_token_details': {'reasoning': 17}})]}

```

# 3.LangChain核心模块

## 3.1 Model

> Kimi：sk-R2jL86pp6orUPP2aGafSwPi1By7bcHPoELm3tVmtgrEDj4af

大语言模型（LLMs）是强大的人工智能工具，能够像人类一样理解和生成文本。它们功能多样，足以编写内容、翻译语言、总结信息以及回答问题，而无需为每项任务进行专门训练。

模型是智能体（Agent）的推理引擎。它们驱动智能体的决策过程，决定调用哪些工具、如何解释结果以及何时提供最终答案。

模型可以通过两种方式使用：

1. **与智能体一起使用** - 在创建[智能体](https://langchain.longbao.wang/oss/langchain/agents#model)时可以动态指定模型。
2. **独立使用** - 模型可以直接调用（在智能体循环之外），用于文本生成、分类或提取等任务，而无需智能体框架。

调用模型，实现输出

> 可以使用OpenAI，可以接入各个大模型

示例：

```python
# Langchain的Model模块 调用大模型
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage,SystemMessage
# 可以使用langchain_openai 调用任意模型，主流的大模型都支持OpenAI格式的api

# 创建模型
model1=ChatOpenAI(
    model="kimi-k2.6",
    openai_api_key="sk-R2jL86pp6orUPP2aGafSwPi1By7bcHPoELm3tVmtgrEDj4af",
    base_url="https://api.moonshot.cn/v1",
)
# 使用模型
print(model1)
# invoke 执行，调用模型实现推理
# r1=model1.invoke("我想做一个小智AI，怎么做？")
# print("Kimi模型：\n",r1)

# 流式请求
# for s in model1.stream("帮我总结一下Langchain的用法，通俗易懂！"):
#     print(s.text)
# 批量请求 一次处理多个请求，并行
r3=model1.batch([
    "怎么理解微积分？教教我",
    "深度学习的重点内容是什么",
    "该高考了写一段打油诗"
])
for s in r3:
    print(s.text)

```

Model模块的核心：

1.会调用各种模型

​	推荐使用OpenAI(支持各种模型)

2.三种调用方式

​	invoke

​	stream

​	betch

3.模型可以绑定工具函数

​	bind_tools

4.模型支持结构化输出

​	with_structured_output



## 3.2 Tools

工具扩展了智能体 (agents)的能力——让它们能够获取实时数据、执行代码、查询外部数据库，并在现实世界中采取行动。

在底层，工具是具有明确定义输入和输出的可调用函数，它们会被传递给聊天模型 (chat model)。模型根据对话上下文决定何时调用工具，以及提供哪些输入参数。

创建工具最简单的方法是使用 [`@tool`](https://reference.langchain.com/python/langchain/tools/#langchain.tools.tool) 装饰器。默认情况下，函数的文档字符串会成为工具的描述，帮助模型理解何时使用它

> 划重点：
>
> 1.工具函数 使用@tool 标记
>
> 2.都需要写清楚文档注释（必须写，让大模型知道这个函数是干什么的）

语法格式：

```python
@tool
def 函数名(参数名,……)->返回值数据类型:
	"""函数的说明信息，文档注释"""
	实现函数的特定的代码块
	return 返回值
	
```

示例：

```python
# Tools 工具
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.messages import HumanMessage

# 1.先创建模型
model=ChatOpenAI(
    model="deepseek-v4-pro",
    openai_api_key="sk-bf6b5981d3694f358df92886d9978605",
    base_url="https://api.deepseek.com/",
)
# 2.工具函数
@tool
def query_bus(bus)->str:
    """查询某个公交车的信息"""
    return f"{bus}路公交车目前已经到了二七万达站"
@tool
def query_train(train)->str:
    """查询某个的火车信息"""
    return f"{train}火车目前已到达郑州站"

# 3..创建Agent
agent=create_agent(
    model=model,
    tools=[query_bus, query_train],
    system_prompt="你是一个万能助手，可以获取各种信息数据"
)
# 4.调用智能体
m1=HumanMessage(content="117路公交车到哪里了")
print(m1)
r=agent.invoke(m1)
print(r)
r2=agent.invoke(HumanMessage(content="K1312到哪里了？"))
print(r2)
```

## 3.3 Agent

智能体（Agents）将语言模型与[工具](https://langchain.longbao.wang/oss/langchain/tools)相结合，构建出能够推理任务、决定使用哪些工具，并迭代式地寻找解决方案的系统。

把模型+工具进行组合

![1780389175258](D:\class\2603\随堂笔记\第十周\AI大模型开发47Agent之RAG.assets\1780389175258.png)

LLM 智能体通过循环运行工具来实现目标。 智能体会持续运行，直到满足停止条件——即模型产生最终输出或达到迭代限制。

通过create_agent创建对应的智能体

动态模型和静态模型：

静态模型：静态模型在创建智能体时配置一次，并在整个执行过程中保持不变。

动态模型：动态模型在 运行时 根据当前的 状态 和上下文进行选择

> 动态模型需要通过中间件实现，动态选择大模型
>
> @wrap_model_call 修饰的函数

关于工具：

工具赋予智能体执行操作的能力。智能体超越了简单的仅模型工具绑定，能够实现：

- 按顺序进行多次工具调用（由单个提示触发）
- 在适当时进行并行工具调用
- 基于先前结果的动态工具选择
- 工具重试逻辑和错误处理
- 跨工具调用的状态持久性

ReAct：智能体遵循 ReAct（"推理 + 行动"）模式，在简短推理步骤与针对性工具调用之间交替进行，并将结果观察反馈到后续决策中，直到能够给出最终答案。

设置系统提示词：

通过提供提示来塑造智能体处理任务的方式。[`system_prompt`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent(system_prompt)) 参数可以作为字符串提供



# 4.综合练习

## 4.1 学习计划生成智能体

​	基于Langchain实现一个智能体，要求可以去生成学习计划（保存问text文档）

​	要求使用：模型、工具、智能体

## 4.2 查询数据库的智能体

​	基于Langchain实现一个智能体，可以实现数据库信息的查询，结果数据保存到text文档

​	要求使用：模型 工具 智能体 SqlAIchemy

# 5.今日总结

Agent

RAG

Langchain

基于Langchain实现Agent开发

掌握Langchain的三大核心模块

​	1.Model 模型

​	2.Tools 工具

​	3.Agent 智能体

基于Langchain快速实现常用的Agent的开发（模型+工具）



# 6.作业

1.查漏补缺

2.写一个智能体（结合你的创意去实现）

3.继续二阶段团队项目

> 不允许使用AI编程工具



