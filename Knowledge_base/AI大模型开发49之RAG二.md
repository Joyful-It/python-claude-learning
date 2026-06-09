# AI大模型开发49之RAG二

> 作者：AI芯源邢朋辉



# 0.课程内容

## 0.1晨考



## 0.2 课程回顾

LangChain实现Agent开发

核心：

1.Model模块

​	调用云端大模型或本地大模型

2.Tools模块

​	Function Calling

​	定义工具函数，可以实现接口调用，数据存储等行为

​	加函数的文档注释

3.Agent模块

​	create_agent 创建智能体

4.Memory模块

​	可以开启记忆模块，存储对话信息，可以选择存储到内存中，也可以数据库

5.MiddleWare模块

​	中间件模块

​	6个生命周期（钩子函数：到什么节点就自动调用）

​	4个节点式钩子：

​	@before_agent

​	@before_model

​	@after_model

​	@after_agent

​	2个包装式钩子：

​	@wrap_model_call

​	@wrap_tool_call

> 切记每个函数的执行时机
>
> 理解ReAct模式

​	内置了一些中间件

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

还可以自定义中间件

实现动态提示词，需要使用@dynamic_prompt

可以实现模型的动态切换，配合包装式钩子：@wrap_model_call

> 记住8个装饰器

6.多智能体

把智能体再封装到工具函数（Function Calling）,重新再定义一个智能体，就可以实现多个智能体

> 熟练基于LangChain开发Agent



# 1.RAG

## 1.1 RAG

**RAG**（Retrieval-Augmented Generation，检索增强生成）是一种让大模型"先查资料再回答"的技术架构。

用户提问 → 检索知识库 → 获取相关文档 → 喂给 LLM → 生成回答

![1780539134485](D:\class\2603\随堂笔记\第十周\AI大模型开发49之RAG二.assets\1780539134485.png)

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

## 1.2 RAG开发流程

1.文档加载

​	获取各种数据

2.文档分块

​	拆分文档内容

3.向量化处理

​	把文档内容进行向量化转换

4.向量数据库

​	把向量化内容存储到向量数据库

5.构建RAG

​	实现RAG链的定义

​	主流采用：Agentic RAG

6.使用RAG

​	结合到Agent还是配合LLM使用

## 1.3 文档加载

读取文档的内容

> 文档格式：pdf、md、excel、csv、json、py、网页数据……

任何RAG应用的起点都是将非结构化的原始文件转化为机器可以理解和处理的“结构化文本单元”，这个单元在LangChain中被抽象为 **Document** **对象**。

`Document` 是LangChain生态中的原子单位。所有加载器（Loader）的最终输出都是一个或多个 `Document` 对象列表。后续的文本分割（Splitting）、向量化（Embedding）等操作，都基于此对象展开

通过LangChain社区 (`langchain-community`) 提供了覆盖几乎所有常见文件类型的加载器。

安装：

pip install langchain-community pypdf

使用

比如加载pdf文档

```python
# 加载pdf文档 读取pdf内容
from langchain_community.document_loaders import PyPDFLoader

# 加载pdf文档
# 创建加载器对象
# loader=PyPDFLoader("./data/AI大模型开发47Agent之Langchain.pdf")
# 提高读取速度，关闭图片提取
loader=PyPDFLoader("./data/AI大模型开发47Agent之Langchain.pdf",extract_images=False)
# 读取文档内容 
pages=loader.load()
print("页数：",len(pages))
# 获取每一页的信息
for page in pages:
    # 元信息
    print(page.metadata)
    # 当前页面的内容
    print(page.page_content)
```

![1780540423961](D:\class\2603\随堂笔记\第十周\AI大模型开发49之RAG二.assets\1780540423961.png)

比如加载py文档 使用自定义加载器

```python
# 读取源文件 py 或普通文档
from pathlib import Path
from langchain_core.documents import Document
from langchain_core.document_loaders import BaseLoader
# 自定义文档加载器
class PythonLoader(BaseLoader):
    def __init__(self,file_path):
        self.file_path = file_path

    def load(self):
        with open(self.file_path,'r',encoding="utf-8") as f:
            c=f.read()
            return Document(
                page_content=c,
                metadata={
                    "type":"python",
                    "title":self.file_path,
                },
            )
        return None
# 创建加载器
loder = PythonLoader('main.py')
doc = loder.load()
print(doc)

```

![1780541284281](D:\class\2603\随堂笔记\第十周\AI大模型开发49之RAG二.assets\1780541284281.png)

要加载多个文档，一般需要开启异步处理

```python
# 一次性加载多个文件，需要使用异步加载处理
# 加载多个网页
import asyncio

import aiohttp
from bs4 import BeautifulSoup
from langchain_core.documents import Document


# 定义函数 实现网页获取
async def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as resp:
            html = await resp.text()
            return html
# 定义函数异步处理数据
async def load_urls(urls:list[str])->list[Document]:
    docs = []
    for url in urls:
        html = await get_html(url)
        if isinstance(html, Exception):
            print(f"网页加载失败 {url}: {html}")
            continue
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(separator="\n", strip=True)
        docs.append(Document(
            page_content=text,
            metadata={"source": url}
        ))
    return docs
# 使用
async def load_data():
    docs = await load_urls([
        "https://www.cnblogs.com/uniqueDong/p/20304104",
        "https://www.cnblogs.com/ymtianyu/p/20302715",
        "https://www.cnblogs.com/wuyuegb2312/p/20302163",
        "https://www.cnblogs.com/ai-old-six/p/20300790"])
    print("获取的文档数量：",len(docs))
    for doc in docs:
        print("文档内容：")
        print(doc.metadata)
        print(doc.page_content)
if __name__ == "__main__":
    asyncio.run(load_data())
```

![1780543982106](D:\class\2603\随堂笔记\第十周\AI大模型开发49之RAG二.assets\1780543982106.png)

还可以设置异常的情况

比如设置重试机制

```python
# 装饰器 配置加载错误的处理
import tenacity
from langchain_community.document_loaders import PyPDFLoader
from tenacity import retry, stop_after_attempt,wait_fixed

# 定义加载函数
# @retry 设置重试机制
@retry(stop=stop_after_attempt(3),wait=wait_fixed(5))
def get_pdf(url):
    print("加载文档：",url)
    loder=PyPDFLoader(url)
    return loder.load()

urls=["data/adbc.pdf","data/wee.pdf","data/wewee.pdf"]
docs = []
dcos_error = []
for url in urls:
    try:
        docs.append(get_pdf(url))
    except Exception as e:
        docs.append({"file":url})
print("加载成功：",len(docs))
print("加载失败：",len(dcos_error))
```

![1780544495726](D:\class\2603\随堂笔记\第十周\AI大模型开发49之RAG二.assets\1780544495726.png)、

## 1.4 文本分块

文本分块是连接非结构化文档与结构化向量数据库的**关键桥梁**。

- 技术约束（Token限制）**：**所有** LLM**（包括** **GPT、Claude）**和 Embedding 模型（如 text-embedding-3-small）都有最大上下文窗口。超过此限制的文本会被截断，导致信息损失。

- 语义约束（检索精度）：这是分块的核心考量。如果块太大，会包含过多无关信息，形成“语义噪声”，导致向量化后检索相关性下降；如果块太小，关键信息的语义上下文不完整，同样影响召回率。

  >  黄金法则：256-512 Token。这是一个经过实践检验的平衡点，能在保持语义完整与控制开销之间取得最佳效果。10-20%的重叠（Chunk Overlap） 是关键，它能有效防止语义在块与块之间断裂，确保上下文的连贯性。

`RecursiveCharacterTextSplitter` 是 LangChain 中最通用、最推荐的分块器。它的工作原理是**递归地按分隔符优先级切割文本**，直到每个块的大小都小于或等于 `chunk_size`。

示例：

```python
# 文档分块
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    UnstructuredMarkdownLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
# 定义函数 实现多文档加载器
def load_documents(file_path: str):
    ext = file_path.split(".")[-1].lower()
    loaders = {
        "pdf": PyPDFLoader,
        "txt": TextLoader,
        "csv": CSVLoader,
        "md": UnstructuredMarkdownLoader,
    }
    loader_class = loaders.get(ext)
    if not loader_class:
        raise ValueError(f"不支持的格式: {ext}")
    loader = loader_class(file_path)
    return loader.load()

# 批量加载
all_docs = []
for path in ["AI大模型开发47Agent之Langchain.pdf", "feq.txt"]:
    all_docs.extend(load_documents(f"data/{path}"))
print("文档：",len(all_docs))
print(all_docs[0].page_content)
# 文本切块
spider=RecursiveCharacterTextSplitter(
    chunk_size=512, # 切块大小
    chunk_overlap=51, # 块间的重叠大小
    add_start_index=True, # 记录原始索引
    separators=["\n","。","！","，"," "], # 切割的符号
    length_function=len # 计数的方式
)
# 开启切块
# 获取要切的文本内容
# d=all_docs[0]
# spider.split_text() # 切割文本内容
# 切割文档
res=spider.split_documents(all_docs)
print(f"原始：{len(all_docs)}，切块：{len(res)}")
print("切块结果：")
print(res[0].page_content)
```

![1780553374534](D:\class\2603\随堂笔记\第十周\AI大模型开发49之RAG二.assets\1780553374534.png)

> - `separators`：决定了文本的自然语义边界。默认优先级从段落（`\n\n`）到句子再到词语，尽可能在大的语义单元处切割。
> - `length_function`：默认按字符数（`len`）计算。如果你的模型按Token计费（如OpenAI），建议使用 `tiktoken` 库的编码器函数，实现**精准的Token级分块**。

分块规则：

语义分块（Semantic Chunking）

适用于对结构要求高、需要按主题划分的文档。它不是简单地按长度分割，而是利用嵌入模型或NLP工具识别语义边界（如主题转换）。

- **库/工具**：`SemanticChunker`（LangChain-experimental）、spaCy 的句子边界检测。
- **适用场景**：论文、长报告、书籍章节。

基于标记（Markdown/HTML）的分块

对于高度结构化的文档（如API文档、技术手册），利用其固有标记进行分块效果最好。

- **MarkdownHeaderTextSplitter**：按标题层级（H1, H2, H3...）分割，保留标题信息作为元数据，构建层次化的知识块。
- **HTMLSectionSplitter**：针对网页内容，按 `<div>`, `<section>`, `<p>` 等标签分割。

固定大小分块与滑动窗口

- **CharacterTextSplitter**：最简单的按字符数固定切分，不考虑语义，速度快，适合日志、代码等对上下文依赖弱的文本。
- **滑动窗口（Sliding Window）**：通过设置 `chunk_size` 和 `chunk_overlap` 即可实现，是处理长序列（如时间序列数据、连续对话）的常见模式。

分块不是一刀切，必须**对症下药**。下表是经验参数的起点，需结合具体任务调整。

| **文档类型**         | **推荐 chunk_size (字符)** | **推荐 chunk_overlap (字符)** | **首选分块策略与关键 separators**                            | **核心目标**                               |
| -------------------- | -------------------------- | ----------------------------- | ------------------------------------------------------------ | ------------------------------------------ |
| **新闻/博客文章**    | 500-800                    | 50-80                         | `RecursiveCharacterTextSplitter`   `separators=["\n\n", "\n", "。", "！", "？"]` | 保持段落/故事的完整性，便于提炼核心事件。  |
| **技术文档/API手册** | 800-1200                   | 100-150                       | `MarkdownHeaderTextSplitter` 或 `Recursive...`   `separators=["\n## ", "\n### ", "\n", "。"]` | 以函数/模块/章节为单位，保留完整接口说明。 |
| **学术论文/长报告**  | 1000-1500                  | 150-200                       | `SemanticChunker` 或 `Recursive...`   `separators=["\n\n", "\n", ". "]` | 确保每个“观点-论据”闭环在一个块内。        |
| **代码仓库**         | 600-1000                   | 80-120                        | `RecursiveCharacterTextSplitter`   `separators=["\nclass ", "\ndef ", "\nasync def ", "\n\t", "\n"]` | 按类、函数、代码块分割，便于检索具体实现。 |
| **对话/会议记录**    | 300-500                    | 30-50                         | `RecursiveCharacterTextSplitter`   `separators=["\n\n", "\n", "？", "。", " "]` | 保持单轮或相关多轮对话的上下文。           |
| **法律/合同文本**    | 800-1200                   | 100-150                       | `RecursiveCharacterTextSplitter`   `separators=["\n第X条", "\n\n", "。"]` | 按法条或条款分割，确保法律条款的独立性。   |

> 记住，分块是RAG系统的基石。没有完美的通用参数，只有最适合你当前数据和业务场景的参数。投入时间进行分块策略的调试，其回报远超盲目堆砌模型参数。



## 1.5 向量化

向量化与向量存储是RAG系统的“记忆中枢”，决定了知识如何被理解、编码与检索。

Embedding（嵌入）的核心任务，是将非结构化的文本（或图像、音频）映射到高维向量空间中的一个点。两个文本的语义相似度，由它们对应向量在空间中的“距离”（如余弦相似度）来衡量。RAG的检索质量，根本上受限于Embedding模型对领域语义的“理解”能力。

需要使用向量模型，完成对文档切割后的内容进行向量化处理

1.云端

​	可以使用OpenAI

​	可以使用智谱、文心一言

2.本地

​	使用Ollama完成本地模型

- 升检索精度的关键路径。

| **场景** | **模型**                                   |
| -------- | ------------------------------------------ |
| 中文通用 | `BAAI/bge-large-zh-v1.5` `GLM/embedding-3` |
| 中英混合 | `BAAI/bge-m3`                              |
| 轻量级   | `BAAI/bge-small-zh-v1.5`                   |
| 英文     | `sentence-transformers/all-MiniLM-L6-v2`   |

如果使用云端模型，推荐使用智谱的embedding-3

Embedding-3 是智谱AI 推出的第三代文本向量化模型，在前代基础上全面升级，提供更强的语义理解能力和更灵活的向量维度选择。该模型支持自定义向量维度，在保持高质量语义表示的同时，为不同应用场景提供了更优的性能和成本平衡。

https://docs.bigmodel.cn/cn/guide/models/embedding/embedding-3#python

示例代码：

下载依赖：pip install zai-sdk

编写代码，使用向量模型

> 提前申请api-key

```python
# 基于智谱的Embedding-3 实现向量化
from zai import ZhipuAiClient


# 创建向量模型
client = ZhipuAiClient(api_key="2d85764c442a496d93c9ec96d690ffca.lnp8YPh5DgVHHNyQ")
r1=client.embeddings.create(
    model="embedding-3", # 设置向量模型
    input=[
    "我爱北京天安门",
    "我讨厌学习数学",
    "很困，想睡觉了！"
])
print("文本向量化结果：")
print(r1)
```

## 1.6 向量数据库

向量数据库负责高效存储高维向量，并提供近似最近邻（ANN）搜索。

主流向量数据库选型矩阵：

| **数据库**                  | **核心特点**                             | **适用场景**                             | **开源/商业** |
| --------------------------- | ---------------------------------------- | ---------------------------------------- | ------------- |
| **Chroma**                  | 轻量、易用、持久化简单，Python原生支持好 | 原型验证、中小知识库、单机部署           | 开源          |
| **FAISS**                   | Facebook出品，内存计算性能极致，学术首选 | 高性能检索、算法验证、离线批量处理       | 开源          |
| **Milvus**                  | 功能全面，支持标量/向量混合查询，云原生  | 大规模生产系统、复杂过滤查询、企业级应用 | 开源/商业版   |
| **Pinecone** / **Weaviate** | 全托管云服务，开箱即用，无缝扩展         | 无运维团队、快速上线、需求动态变化       | 商业SaaS      |
| **PGVector**                | PostgreSQL扩展，向量与关系数据一体管理   | 已用PostgreSQL，强事务与关联查询需求     | 开源          |

比如使用Chroma向量数据库

1.下载

pip install langchain_chroma 

2.使用

```python
# 文档-切块-向量化-向量数据库-相关性查询
import os

from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import ZhipuAIEmbeddings
from pathlib import Path
chroma_db=None
# 验证是否存在向量库
# 验证 向量数据库文件夹是否存在
if Path("./data/chromatest.db").exists():
    # 存在就读取
    chroma_db=Chroma(
        persist_directory="./data/chromatest.db", 
    )
else:
    #不存在 就生成
    # 加载文档
    loader=PyPDFLoader("./data/AI大模型开发47Agent之Langchain.pdf")
    pages=loader.load()
    # 分块
    document_splitter=RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=51,
        separators=["\n\n","\n","。","，"," "]
    )
    chunks=document_splitter.split_documents(pages)
    # 向量化 向量模型
    embedder=ZhipuAIEmbeddings(
        model="embedding-3",
        api_key="2d85764c442a496d93c9ec96d690ffca.lnp8YPh5DgVHHNyQ",
        dimensions=1024
    )
    chroma_db=Chroma.from_documents(
        documents=chunks,
        embedding=embedder,
        persist_directory="./data/chromatest.db",
        collection_metadata={"hnsw:space": "cosine"}  # 计算 相关性的方式 余弦
    )
# 基于向量库 实现查询
res1=chroma_db.similarity_search(query="模型可以通过那两种进行使用？",k=3)
for r in res1:
    print(r)
```



> 需要提前准备数据--一本电子书（2万字--50万字以内）

# 2.综合练习

1.熟练使用RAG

文档-分块-向量化-向量数据库-搜索



# 3.今日总结

RAG 检索增强生成

创建私有知识库，大模型或Agent可以参考知识库的内容

文档读取-loader

文档分块-Spider

向量化-向量模型

向量数据库-Chroma、FAISS

相似性搜索、关键字搜索

> 明天：
>
> 实现一个Agent
>
> 1.0 实现完整功能
>
> 2.0 优化使用



# 4.作业

1.查漏补缺

