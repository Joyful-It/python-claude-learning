# Agent 工具函数完整指南

> 让大模型从"会说话"变成"能做事"

---

## 第1节：大模型的三大固有缺陷

大语言模型（LLM）虽然强大，但存在三大与生俱来的局限：

| 缺陷 | 说明 |
|------|------|
| **知识截止** | 无法获取训练数据之后的实时信息 |
| **计算能力弱** | 复杂数学计算、精确算术经常出错 |
| **无法与真实世界交互** | 不能读取文件、调用 API、执行代码 |

### 工具函数的作用

工具函数是 Agent 连接外部世界的"手和脚"，弥补大模型的所有上述缺陷，让 Agent 从"会说话"变成"能做事"。

> 💡 **核心思想：大模型做决策，工具函数做执行**

---

## 第2节：本质区别 — Agent 工具 vs 普通工具

| 对比维度 | 普通 Python 工具函数 | Agent 专用工具函数 |
|----------|---------------------|-------------------|
| **调用者** | 人类程序员 | 大语言模型 |
| **第一优先级** | 功能正确、运行高效 | 可被大模型理解 |
| **输入输出** | 固定格式 | 结构化、自描述 |
| **错误处理** | 抛出异常给开发者 | 返回友好错误信息给大模型 |
| **文档** | 给人看的注释 | 给模型看的结构化描述 |
| **返回值** | 任意类型 | 必须是字符串 |

---

## 第3节：标准 Agent 工具函数三要素

一个合格的 Agent 工具函数必须包含：

### 1. 结构化参数定义
- 使用 Pydantic 模型明确每个参数的类型和要求
- 每个参数都要有详细的 `Field` 描述

### 2. 自然语言工具描述
- 明确告诉大模型：这个工具**能做什么**
- 明确告诉大模型：**什么时候**应该用这个工具
- 明确告诉大模型：这个工具**不能做什么**

### 3. 健壮的实现逻辑
- 处理所有可能的边界情况
- **永远不抛出异常**，所有错误都返回字符串
- 返回结果简洁明了，方便大模型理解

---

## 第4节：核心工具 1 — 数学计算器

### 为什么必须有？

大模型在计算方面的表现极其糟糕，即使是简单的加减乘除也经常出错。

### 完整代码

```python
# 导入Pydantic的BaseModel和Field，用于定义结构化参数
from pydantic import BaseModel, Field
# 导入LangChain的tool装饰器，用于将普通函数转换为Agent工具
from langchain.tools import tool

# 定义计算器工具的输入参数模型
class CalculatorInput(BaseModel):
    # 定义expression参数，类型为字符串，并添加详细描述
    expression: str = Field(description="需要计算的数学表达式，只支持基本的加减乘除和括号，例如：(3+5)*2")

# 使用@tool装饰器将函数标记为Agent工具，指定参数模型
@tool(args_schema=CalculatorInput)
def calculator(expression: str) -> str:
    """
    高精度数学计算器工具。
    ✅ 当你需要进行任何数学计算时，请使用这个工具，不要自己计算
    支持：加减乘除、括号、小数运算
    ❌ 不支持：复杂函数、代数方程、微积分
    """
    try:
        # 使用eval函数计算表达式，限制命名空间只允许使用基本运算，防止代码注入
        # __builtins__设为None，禁止访问所有内置函数
        result = eval(expression, {"__builtins__": None}, {})
        # 返回格式化的计算结果
        return f"计算结果: {result}"
    # 捕获表达式语法错误
    except SyntaxError:
        return "错误：表达式语法不正确，请检查括号和运算符"
    # 捕获除零错误
    except ZeroDivisionError:
        return "错误：除数不能为零"
    # 捕获其他所有异常
    except Exception as e:
        return f"计算错误: {str(e)}"
```

**使用场景**：价格计算、统计数据、时间差、单位换算

---

## 第5节：核心工具 2 — Python 代码解释器

### 为什么必须有？

这是最强大的 Agent 工具，没有之一。能让大模型通过编写代码解决几乎所有复杂问题。

### 完整代码

```python
# 导入io模块，用于创建内存中的字符串缓冲区
import io
# 导入contextlib模块，用于重定向标准输出
import contextlib
# 导入traceback模块，用于获取完整的错误堆栈信息
import traceback
from pydantic import BaseModel, Field
from langchain.tools import tool

# 定义代码解释器工具的输入参数模型
class CodeInput(BaseModel):
    code: str = Field(description="要执行的Python代码，必须是完整可运行的代码块")

@tool(args_schema=CodeInput)
def execute_python_code(code: str) -> str:
    """
    Python代码解释器工具。
    当你需要进行复杂数据处理、数据分析、文件操作、图表生成或任何需要编程解决的问题时，
    请编写Python代码并使用这个工具执行。所有输出都会被捕获并返回给你。
    """
    # 创建一个字符串缓冲区，用于捕获代码的标准输出
    output_buffer = io.StringIO()
    
    try:
        # 使用redirect_stdout上下文管理器，将标准输出重定向到缓冲区
        with contextlib.redirect_stdout(output_buffer):
            # 执行代码，允许使用所有内置函数（生产环境建议进一步限制）
            exec(code, {"__builtins__": __builtins__}, {})
        
        # 从缓冲区中获取所有输出内容
        execution_output = output_buffer.getvalue()
        # 如果没有输出，返回成功提示
        if not execution_output:
            return "代码执行成功，但没有输出"
        # 否则返回格式化的输出结果
        return f"代码执行成功，输出:\n{execution_output}"
    
    # 捕获代码执行过程中的所有异常
    except Exception:
        # 获取完整的错误堆栈信息，方便大模型调试
        error_trace = traceback.format_exc()
        return f"代码执行错误:\n{error_trace}"
```

**使用场景**：数据清洗、统计分析、生成图表、文件格式转换、算法实现

---

## 第6节：核心工具 3 — 网页搜索

### 为什么必须有？

解决大模型知识截止问题，获取实时信息和最新知识。

### 完整代码

```python
from pydantic import BaseModel, Field
from langchain.tools import tool
# 导入requests库，用于发送HTTP请求
import requests

# 定义网页搜索工具的输入参数模型
class WebSearchInput(BaseModel):
    query: str = Field(description="搜索关键词，要具体明确，例如：2024年中国GDP增长率")

@tool(args_schema=WebSearchInput)
def web_search(query: str) -> str:
    """
    网页搜索工具。
    当你需要获取实时信息、最新新闻、未知知识、产品价格、天气等
    任何不在你知识库中的信息时，请使用这个工具进行搜索。
    """
    # Serper API的搜索接口地址（也可以使用Google Search API或Bing API）
    api_url = "https://google.serper.dev/search"
    # 请求参数：q=搜索关键词，num=返回结果数量
    request_payload = {"q": query, "num": 5}
    # 请求头：包含API密钥和内容类型
    request_headers = {
        "X-API-KEY": "YOUR_SERPER_API_KEY",  # 替换为你自己的API密钥
        "Content-Type": "application/json"
    }
    
    try:
        # 发送POST请求到Serper API，设置超时时间为10秒
        response = requests.post(api_url, json=request_payload, headers=request_headers, timeout=10)
        # 检查响应状态码，如果不是200则抛出异常
        response.raise_for_status()
        # 解析JSON格式的响应结果
        search_results = response.json()
        
        # 初始化一个列表，用于存储格式化后的搜索结果
        formatted_results = []
        # 遍历前5条有机搜索结果
        for index, item in enumerate(search_results.get("organic", []), 1):
            # 将每条结果格式化为易读的字符串
            formatted_results.append(
                f"{index}. 标题: {item.get('title')}\n"
                f"   摘要: {item.get('snippet')}\n"
                f"   链接: {item.get('link')}\n"
            )
        
        # 如果没有找到结果，返回提示信息
        if not formatted_results:
            return "没有找到相关结果"
        
        # 返回所有格式化后的结果
        return "搜索结果:\n" + "\n".join(formatted_results)
    
    # 捕获所有网络请求相关的异常
    except Exception as e:
        return f"搜索失败: {str(e)}"
```

**使用场景**：查询实时新闻、产品信息、技术文档、旅游攻略、天气

---

## 第7节：核心工具 4 — 文件读取工具

### 为什么必须有？

Agent 需要能够读取本地文件获取数据，作为处理的输入。

### 完整代码

```python
from pydantic import BaseModel, Field
from langchain.tools import tool
# 导入os模块，用于检查文件是否存在
import os

# 定义读取文件工具的输入参数模型
class ReadFileInput(BaseModel):
    file_path: str = Field(description="要读取的文件的完整路径或相对路径")
    encoding: str = Field(default="utf-8", description="文件编码格式，默认utf-8，中文文件也可能是gbk")

@tool(args_schema=ReadFileInput)
def read_file(file_path: str, encoding: str = "utf-8") -> str:
    """
    读取本地文本文件的内容。
    当你需要读取用户指定的文件内容进行处理时使用这个工具。
    只支持读取文本文件，不支持二进制文件（如图片、视频）。
    """
    try:
        # 检查文件是否存在
        if not os.path.exists(file_path):
            return f"错误：文件 {file_path} 不存在，请检查路径是否正确"
        
        # 使用with语句打开文件，自动管理文件上下文，确保文件会被正确关闭
        with open(file_path, "r", encoding=encoding) as file:
            # 读取文件全部内容
            file_content = file.read()
        
        # 限制返回内容的长度，避免超过大模型的上下文窗口
        max_return_length = 5000
        if len(file_content) > max_return_length:
            truncated_content = file_content[:max_return_length]
            return f"文件内容（共{len(file_content)}个字符，已截断到前{max_return_length}个）:\n{truncated_content}"
        
        # 返回完整的文件内容
        return f"文件内容（共{len(file_content)}个字符）:\n{file_content}"
    
    # 捕获编码错误
    except UnicodeDecodeError:
        return f"错误：文件编码不是{encoding}，请尝试使用gbk或其他编码"
    # 捕获其他所有异常
    except Exception as e:
        return f"读取文件失败: {str(e)}"
```

**使用场景**：读取配置文件、处理用户上传的文本文件、读取日志文件

---

## 第8节：核心工具 5 — 文件写入工具

### 为什么必须有？

Agent 需要能够将处理结果保存到文件中，方便用户后续使用。

### 完整代码

```python
from pydantic import BaseModel, Field
from langchain.tools import tool

# 定义写入文件工具的输入参数模型
class WriteFileInput(BaseModel):
    file_path: str = Field(description="要写入的文件的完整路径或相对路径")
    content: str = Field(description="要写入文件的内容")
    mode: str = Field(default="w", description="写入模式，w=覆盖原有内容，a=追加到文件末尾")

@tool(args_schema=WriteFileInput)
def write_file(file_path: str, content: str, mode: str = "w") -> str:
    """
    将内容写入本地文件。
    当你需要将处理结果、生成的报告、代码等内容保存到文件时使用这个工具。
    如果文件不存在，会自动创建；如果文件已存在，会根据mode参数决定是覆盖还是追加。
    """
    try:
        # 使用with语句打开文件，指定写入模式和编码
        with open(file_path, mode, encoding="utf-8") as file:
            # 将内容写入文件
            file.write(content)
        
        # 返回成功提示，包含文件路径和写入的字符数
        return f"成功写入文件: {file_path}，共写入了{len(content)}个字符"
    
    # 捕获所有异常
    except Exception as e:
        return f"写入文件失败: {str(e)}"
```

**使用场景**：保存分析结果、生成报告、保存代码文件、导出数据

---

## 第9节：核心工具 6 — CSV 数据处理工具

### 为什么必须有？

CSV 是最常见的结构化数据格式，专门的 CSV 处理工具比让 Agent 自己写代码更高效可靠。

### 完整代码

```python
from pydantic import BaseModel, Field
from langchain.tools import tool
# 导入csv模块，用于处理CSV文件
import csv

# 定义读取CSV工具的输入参数模型
class ReadCSVInput(BaseModel):
    file_path: str = Field(description="CSV文件的完整路径或相对路径")
    delimiter: str = Field(default=",", description="CSV文件的分隔符，默认逗号，也可能是制表符\\t")

@tool(args_schema=ReadCSVInput)
def read_csv(file_path: str, delimiter: str = ",") -> str:
    """
    读取CSV文件并返回基本统计信息和前10行数据预览。
    当你需要分析CSV格式的结构化数据时使用这个工具。
    """
    try:
        # 打开CSV文件
        with open(file_path, "r", encoding="utf-8") as file:
            # 创建CSV字典读取器，将每行数据转换为字典
            csv_reader = csv.DictReader(file, delimiter=delimiter)
            # 将所有行转换为列表
            all_rows = list(csv_reader)
        
        # 如果文件为空，返回提示
        if not all_rows:
            return "CSV文件为空"
        
        # 获取总行数
        total_rows = len(all_rows)
        # 获取列名列表
        columns = list(all_rows[0].keys())
        
        # 初始化列表存储前10行预览
        preview_rows = []
        for index, row in enumerate(all_rows[:10], 1):
            preview_rows.append(f"行{index}: {row}")
        
        # 返回格式化的CSV信息
        return (
            f"CSV文件信息:\n"
            f"总行数: {total_rows}\n"
            f"列名: {', '.join(columns)}\n"
            f"\n前10行预览:\n" + "\n".join(preview_rows)
        )
    
    except Exception as e:
        return f"读取CSV失败: {str(e)}"
```

**使用场景**：分析销售数据、用户数据、财务报表、实验数据

---

## 第10节：核心工具 7 — 通用 API 调用工具

### 为什么必须有？

让 Agent 能够调用各种外部 API 服务，扩展无限能力。

### 完整代码

```python
from pydantic import BaseModel, Field
from langchain.tools import tool
import requests
# 导入json模块，用于格式化JSON输出
import json

# 定义API调用工具的输入参数模型
class APIRequestInput(BaseModel):
    url: str = Field(description="API的完整URL地址")
    method: str = Field(default="GET", description="HTTP请求方法，支持GET和POST")
    headers: dict = Field(default={}, description="请求头字典，例如：{'Authorization': 'Bearer token'}")
    params: dict = Field(default={}, description="URL查询参数字典")
    body: dict = Field(default={}, description="POST请求的JSON请求体")

@tool(args_schema=APIRequestInput)
def call_api(url: str, method: str = "GET", headers: dict = None, 
             params: dict = None, body: dict = None) -> str:
    """
    通用API调用工具。
    当你需要调用外部API服务获取数据或执行操作时使用这个工具。
    支持GET和POST两种请求方法。
    """
    # 为可选参数设置默认值
    headers = headers or {}
    params = params or {}
    body = body or {}
    
    try:
        # 根据请求方法发送不同的请求
        if method.upper() == "GET":
            # 发送GET请求
            response = requests.get(url, headers=headers, params=params, timeout=10)
        elif method.upper() == "POST":
            # 发送POST请求，自动将body转换为JSON格式
            response = requests.post(url, headers=headers, params=params, json=body, timeout=10)
        else:
            # 不支持其他请求方法
            return f"错误：不支持的HTTP方法 {method}，只支持GET和POST"
        
        # 检查响应状态码
        response.raise_for_status()
        
        # 尝试将响应解析为JSON格式
        try:
            json_result = response.json()
            # 格式化JSON输出，确保中文正常显示
            formatted_json = json.dumps(json_result, indent=2, ensure_ascii=False)
            return f"API调用成功，状态码: {response.status_code}\n响应内容:\n{formatted_json}"
        except:
            # 如果不是JSON格式，返回纯文本内容，限制长度
            return f"API调用成功，状态码: {response.status_code}\n响应内容:\n{response.text[:2000]}"
    
    # 捕获所有请求异常
    except requests.exceptions.RequestException as e:
        return f"API调用失败: {str(e)}"
```

**使用场景**：调用天气 API、地图 API、支付 API、企业内部服务

---

## 第11节：核心工具 8 — 知识库检索工具（RAG）

### 为什么必须有？

让 Agent 访问私有知识，回答专业领域问题，避免幻觉。

### 完整代码

```python
from pydantic import BaseModel, Field
from langchain.tools import tool
# 导入Chroma向量数据库
from langchain_community.vectorstores import Chroma
# 导入OpenAI嵌入模型
from langchain_openai import OpenAIEmbeddings

# 定义知识库检索工具的输入参数模型
class RetrieveInput(BaseModel):
    query: str = Field(description="要检索的问题或关键词")
    top_k: int = Field(default=3, description="返回最相关的文档数量，默认3个")

@tool(args_schema=RetrieveInput)
def retrieve_from_knowledge_base(query: str, top_k: int = 3) -> str:
    """
    知识库检索工具。
    当你需要回答关于公司内部文档、产品手册、技术规范等私有知识的问题时，
    请使用这个工具从知识库中检索相关信息。
    只有在知识库中找到的信息才是准确的，不要编造信息。
    """
    try:
        # 初始化OpenAI嵌入模型，用于将查询转换为向量
        embeddings = OpenAIEmbeddings(api_key="YOUR_OPENAI_API_KEY")
        
        # 加载已持久化的向量数据库
        vectorstore = Chroma(
            persist_directory="./knowledge_base",  # 向量数据库存储目录
            embedding_function=embeddings,
            collection_name="company_docs"  # 集合名称
        )
        
        # 执行相似度搜索，返回top_k个最相关的文档
        relevant_docs = vectorstore.similarity_search(query, k=top_k)
        
        # 如果没有找到相关文档，返回提示
        if not relevant_docs:
            return "知识库中没有找到相关信息，请尝试其他关键词"
        
        # 格式化检索结果
        formatted_docs = []
        for index, doc in enumerate(relevant_docs, 1):
            formatted_docs.append(
                f"文档{index}:\n"
                f"内容: {doc.page_content}\n"
                f"来源: {doc.metadata.get('source', '未知来源')}\n"
            )
        
        # 返回所有格式化后的文档
        return "从知识库检索到以下相关信息:\n" + "\n".join(formatted_docs)
    
    except Exception as e:
        return f"检索知识库失败: {str(e)}"
```

**使用场景**：公司内部问答、产品咨询、技术支持、文档问答

---

## 第12节：核心工具 9 — 记忆管理工具

### 为什么必须有？

大模型的上下文窗口有限，无法记住所有历史对话，需要长期记忆能力。

### 完整代码

```python
from pydantic import BaseModel, Field
from langchain.tools import tool
import json
import os

# 定义记忆文件的路径
MEMORY_FILE_PATH = "agent_long_term_memory.json"

# 定义保存记忆工具的输入参数模型
class SaveMemoryInput(BaseModel):
    key: str = Field(description="记忆的唯一键名，要简洁明了，例如：user_name、project_deadline")
    value: str = Field(description="要保存的记忆内容")

@tool(args_schema=SaveMemoryInput)
def save_memory(key: str, value: str) -> str:
    """
    保存重要信息到长期记忆中。
    当你获取到用户的重要信息（如姓名、偏好、需求）或需要记住的关键事实时，
    请使用这个工具保存下来，以便后续对话使用。
    """
    try:
        # 初始化记忆字典
        memory_dict = {}
        # 如果记忆文件存在，加载现有记忆
        if os.path.exists(MEMORY_FILE_PATH):
            with open(MEMORY_FILE_PATH, "r", encoding="utf-8") as file:
                memory_dict = json.load(file)
        
        # 保存新记忆或更新已有记忆
        memory_dict[key] = value
        
        # 将更新后的记忆写入文件
        with open(MEMORY_FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(memory_dict, file, ensure_ascii=False, indent=2)
        
        return f"成功保存记忆: {key} = {value}"
    
    except Exception as e:
        return f"保存记忆失败: {str(e)}"


# 定义加载记忆工具的输入参数模型
class LoadMemoryInput(BaseModel):
    key: str = Field(description="要加载的记忆的键名")

@tool(args_schema=LoadMemoryInput)
def load_memory(key: str) -> str:
    """
    从长期记忆中加载指定的信息。
    当你需要使用之前保存的重要信息时使用这个工具。
    """
    try:
        # 检查记忆文件是否存在
        if not os.path.exists(MEMORY_FILE_PATH):
            return "当前没有任何保存的记忆"
        
        # 加载记忆文件
        with open(MEMORY_FILE_PATH, "r", encoding="utf-8") as file:
            memory_dict = json.load(file)
        
        # 检查指定的键是否存在
        if key not in memory_dict:
            return f"没有找到键为 '{key}' 的记忆"
        
        return f"记忆内容: {key} = {memory_dict[key]}"
    
    except Exception as e:
        return f"加载记忆失败: {str(e)}"
```

**使用场景**：记住用户偏好、保存对话中的关键信息、记录任务进度

---

## 第13节：核心工具 10 — 时间工具

### 为什么必须有？

大模型不知道当前时间，也不擅长处理复杂的时间计算。

### 完整代码

```python
from pydantic import BaseModel, Field
from langchain.tools import tool
# 导入datetime模块，用于处理日期和时间
from datetime import datetime, timedelta

@tool
def get_current_time() -> str:
    """
    获取当前的日期和时间。
    当你需要知道现在是什么时间、今天是几号、星期几的时候使用这个工具。
    """
    # 获取当前时间
    now = datetime.now()
    # 定义星期列表
    weekdays = ["一", "二", "三", "四", "五", "六", "日"]
    # 格式化时间字符串
    formatted_time = now.strftime("%Y年%m月%d日 %H:%M:%S")
    # 获取星期几
    weekday = weekdays[now.weekday()]
    
    return f"当前时间: {formatted_time} 星期{weekday}"


# 定义计算时间差工具的输入参数模型
class CalculateTimeDiffInput(BaseModel):
    start_time: str = Field(description="开始时间，格式必须为：YYYY-MM-DD HH:MM:SS")
    end_time: str = Field(description="结束时间，格式必须为：YYYY-MM-DD HH:MM:SS")

@tool(args_schema=CalculateTimeDiffInput)
def calculate_time_difference(start_time: str, end_time: str) -> str:
    """
    计算两个时间之间的差值。
    当你需要计算两个日期之间相差多少天、多少小时的时候使用这个工具。
    """
    try:
        # 将字符串时间转换为datetime对象
        start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        # 计算时间差
        time_diff = end - start
        
        # 提取天数、小时、分钟、秒
        days = time_diff.days
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        return f"时间差: {days}天 {hours}小时 {minutes}分钟 {seconds}秒"
    
    # 捕获时间格式错误
    except ValueError:
        return "错误：时间格式不正确，请使用 YYYY-MM-DD HH:MM:SS 格式"
```

**使用场景**：计算截止日期、安排日程、计算时间间隔、生成时间戳

---

## 第14节：工具函数设计最佳实践

### 1. 工具描述是灵魂

| | 示例 |
|--|--|
| ✅ **好的描述** | "当你需要进行任何数学计算时，请使用这个工具，**不要自己计算**" |
| ❌ **坏的描述** | "这是一个计算器工具" |

一定要明确说明**什么时候用**和**什么时候不用**。

### 2. 参数设计原则

- 使用 Pydantic 模型，每个参数都要有详细描述
- 参数越少越好，必要参数不超过 3 个
- 为可选参数提供合理的默认值

### 3. 错误处理要友好

- **永远不要抛出异常**，所有错误都返回字符串
- 错误信息要具体："除数不能为零" 而不是 "计算错误"
- 告诉大模型哪里错了、怎么改

### 4. 安全与性能

- 代码执行工具必须严格限制权限
- 限制返回结果长度，避免超过上下文窗口
- API 调用工具要限制请求频率

---

## 第15节：工具调用完整流程

```
用户提问
    ↓
大模型判断：是否需要调用工具？
    ├─ 不需要 → 直接回答用户
    └─ 需要 → 选择合适的工具并生成参数
        ↓
调用工具函数执行
        ↓
获取工具返回结果
        ↓
大模型根据工具返回结果生成最终回答
        ↓
返回给用户
```

> 💡 **关键**：大模型会自主判断是否需要调用工具、调用哪个工具、以及如何组合使用多个工具

---

## 第16节：常见误区与避坑指南

| 误区 | 问题 | 正确做法 |
|------|------|----------|
| ❌ 工具越多越好 | 工具太多会让大模型困惑，增加选择困难 | 只保留当前任务真正需要的工具 |
| ❌ 工具描述越详细越好 | 太长的描述会增加大模型的理解负担 | 简洁精准，突出核心功能和使用时机 |
| ❌ 让大模型自己处理所有错误 | 工具应该尽可能处理错误，返回清晰的解决方案 | 工具内部消化错误，返回友好字符串 |
| ❌ 返回结果越长越好 | 大模型的上下文窗口有限 | 返回结果要简洁，只保留关键信息 |

---

## 第17节：总结

1. **工具函数是 Agent 的核心能力**，没有工具的 Agent 只是一个聊天机器人
2. **Agent 工具函数与普通工具函数有本质区别**，第一优先级是可被大模型理解
3. **10 类核心工具**：计算器、代码解释器、网页搜索、文件读写、CSV 处理、API 调用、知识库检索、记忆管理、时间工具
4. **工具描述是灵魂**，好的描述能让工具发挥最大作用
5. **遵循最佳实践，避免常见误区**，才能写出好用的 Agent 工具函数

---


