# ==================== ChatPDF — 智能 PDF 问答助手 ====================
# 架构：初始化层（执行一次）+ 交互层（while True 循环）
#
# 数据流：
#   PDF文件 → PdfReader加载 → Document包装 → 递归分块
#   → Embedding向量化 → 存入Chroma向量库 → Retriever检索接口
#   → 用户提问 → 检索相关块 → 拼Prompt → LLM生成答案

import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"  # 国内 HF 镜像，必加

# ─── 导入 ───────────────────────────────────────────
from pypdf import PdfReader                                  # PDF 读取（手动挡）
from langchain_core.documents import Document                # LangChain 原子单位
from langchain_text_splitters import RecursiveCharacterTextSplitter  # 递归文本分块
from langchain_huggingface import HuggingFaceEmbeddings      # Embedding 模型
from langchain_chroma import Chroma                          # 向量数据库
from langchain.chat_models import init_chat_model            # LLM 统一入口
from langchain_core.prompts import ChatPromptTemplate        # Prompt 模板


# ╔══════════════════════════════════════════════════════════╗
# ║              初始化层 — 只执行一次                        ║
# ╚══════════════════════════════════════════════════════════╝

# ─── 第1步：加载 PDF ──────────────────────────────────────
# PdfReader = Python 原生 PDF 解析器，不需要 langchain_community
# 每页提取文本后手动包装成 Document 对象
# Document = LangChain 世界里的"原子单位"，一切操作（分块/向量化/检索）都基于它
reader = PdfReader("c:/project/python/Knowledge_base/LangChain.pdf")
print(f"📄 总页数: {len(reader.pages)}")


# Python enumerate() 函数详解
# enumerate() 是 Python最常用的内置函数之一，核心作用是：
# 遍历可迭代对象（列表、元组、字符串等）时，同时获取「元素的索引」和「元素本身」，
docs = []  # 准备装所有页的 Document

for i, page in enumerate(reader.pages):                       
    
    text = page.extract_text()            # 提取当前页的纯文本
    if text:                      
 # 跳过空白页（纯图片页会返回空）if text:什么意思？
 # 其实是：if text != "":的简写。
        docs.append(  #加入docs列表
            Document(#langchain 文件文档
                page_content=text,         # 【肉】文本正文 — 检索时匹配的就是它
                metadata={                 # 【身份证】记录来源 — 回答时能溯源
                    "source": "LangChain.pdf",
                    "page": i + 1          # enumerate 从 0 开始，+1 变自然页码
                }
            )
        )
print(f"✅ 创建了 {len(docs)} 个 Document 对象（每页一个）")

# ─── 第2步：文本分块 ──────────────────────────────────────
# 为什么分块？
#   ① 一页可能很长，超过 Embedding 模型的 token 上限会被截断
#   ② 粗粒度检索不精准 — 大海捞针 vs 精准定位
# RecursiveCharacterTextSplitter = 递归逐级分隔符分块
#   不会在中间硬切段落，而是按优先级一层层往下找切割点：
#   \n\n(段落) → \n(行) → 。(句) → " "(词) → ""(字符硬切)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,        # 每块最多 500 字符，适合大多数中文 Embedding 模型
    chunk_overlap=50,      # 相邻块重叠 50 字符，防止关键信息刚好被切在边界
    separators=["\n\n", "\n", "。", ". ", " ", ""]  # 分隔符层级：从大到小
)
chunks = text_splitter.split_documents(docs)
print(f"✅ 分块完成: {len(docs)} 页 → {len(chunks)} 个文本块")
# ─── 第3步：Embedding 向量化 ─────────────────────────────
# Embedding 模型 = 把文本变成数字向量
#   语义相近的文本 → 向量在空间中靠得近 → cos 相似度就高
# bge-small-zh-v1.5 = BGE 中文轻量版，仅 95MB，CPU 可跑
#   首次运行自动下载到本地缓存，之后不再下载

embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5",
    model_kwargs={"device":"cpu"}
)
# ─── 第4步：存入向量数据库 ───────────────────────────────
# Chroma = 轻量级本地向量库
#   from_documents() 做了两件事：
#     ① 调 embedding 把每个 chunk 变成向量
#     ② 把向量 + 原文一起存到磁盘
# persist_directory = 存盘路径，下次直接加载，不用重新 Embedding
# Chroma ≠ Embedding 模型！口诀: "Chrom 存，BGE 算"
vector_score = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="./chroma_chatpdf_db"
)
print(f"向量库以构建：{len(chunks)}条向量")
# ─── 第5步：创建检索器 ───────────────────────────────────
# as_retriever() = 把向量库包装成"问一句→返回相关文档"的接口
# k=3 = 每次检索返回最相关的 3 个文本块
# search_type="similarity" = 默认余弦相似度检索（和 Transformer 自注意力 Q@K^T 同操作）
retriever = vector_score.as_retriever(
    search_type="similarty",
    search_kwargs={"k":3}
)
# ─── 第6步：初始化 LLM ──────────────────────────────────
llm=init_chat_model(
    api_key="",
    model="deepseek-v4-flash",
    model_provider="deepseek",
    temperture=0
)






