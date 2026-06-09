# ========== 第4章：文档加载 ==========
# 国内访问 HuggingFace 用镜像站
import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

from pypdf import PdfReader
from langchain_core.documents import Document

# 用 pypdf 读取 PDF，每页手动包装成 Document 对象
reader = PdfReader("Knowledge_base/LangChain.pdf")
print(f"总页数: {len(reader.pages)}")

docs = []
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        docs.append(Document(
            page_content=text,
            metadata={"source": "LangChain.pdf", "page": i + 1}
        ))

print(f"创建了 {len(docs)} 个 Document 对象")
print(f"\n=== 第1个Document ===")
print(f"内容前150字: {docs[0].page_content[:150]}")
print(f"元数据: {docs[0].metadata}")

# Document = page_content + metadata
#   → page_content: 文本"肉"
#   → metadata:     身份证（来源/页数/作者）

# ========== 第5章：文本分块 ==========
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # 每块最多500字符
    chunk_overlap=50,    # 相邻块重叠50字符（防止关键信息被切断）
    separators=["\n\n", "\n", "。", ". ", " ", ""],  # 逐级分隔符
)

chunks = text_splitter.split_documents(docs)
print(f"\n分块前: {len(docs)} 个Document（每页一个）")
print(f"分块后: {len(chunks)} 个Document（每段一个）")
print(f"\n=== 第1个分块 ===")
print(f"内容: {chunks[0].page_content[:200]}")
print(f"元数据: {chunks[0].metadata}")
print(f"\n=== 第2个分块（和上一块有50字重叠）===")
print(f"内容: {chunks[1].page_content[:200]}")

# ========== 第6章：Embedding + 向量库 ==========
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# ========== 第6章：Embedding + 向量库 ==========
#
# Embedding 模型的三种部署路线：
#
# ┌─────────────────┬──────────────┬──────────────────┬──────────────────┐
# │ 路线             │ 例子          │ 优点              │ 缺点              │
# ├─────────────────┼──────────────┼──────────────────┼──────────────────┤
# │ ① 云端 API       │ 智谱/OpenAI   │ 不占本地资源        │ 花钱、数据出站      │
# │                  │ /DeepSeek    │ 模型最新最强       │ 有网络延迟         │
# ├─────────────────┼──────────────┼──────────────────┼──────────────────┤
# │ ② 本地 Ollama    │ bge-m3 /     │ 免费、数据不出本机   │ 需提前下载模型      │
# │                  │ nomic-embed  │ 离线可用           │ 吃内存/显存        │
# ├─────────────────┼──────────────┼──────────────────┼──────────────────┤
# │ ③ 本地直接加载    │ bge-small /  │ 最轻量，一行代码     │ 模型较小，效果不如  │
# │ (HuggingFace)   │ all-MiniLM   │ 纯 CPU 可跑        │ 前两种             │
# └─────────────────┴──────────────┴──────────────────┴──────────────────┘
#
# 当前代码用路线③（最简单，不依赖额外服务），注释里附了①②的写法。

# ====== 路线③：本地直接加载（当前使用） ======
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5",  # BGE 中文轻量版，仅 95MB
    model_kwargs={"device": "cpu"},        # cpu模式，不要求显卡
)
#   ↑ 模型首次运行自动下载到本地缓存，之后不再下载

# ====== 路线②：Ollama 本地部署（备选，需先 ollama pull bge-m3）======
# from langchain_ollama import OllamaEmbeddings
# embedding = OllamaEmbeddings(model="bge-m3")  # 效果更好，需 2GB 内存

# ====== 路线①：云端 API（备选，需 API Key）======
# from langchain_openai import OpenAIEmbeddings        # OpenAI 兼容接口
# embedding = OpenAIEmbeddings(
#     model="text-embedding-3-small",                  # OpenAI 官方
#     api_key="sk-xxx"
# )
# # 或者智谱：
# # embedding = ZhipuAIEmbeddings(model="embedding-2")

# ----- 向量数据库：Chroma -----
# Chroma = 轻量级向量库，数据存本地磁盘，适合学习和中小规模项目
# 大规模生产可升级到 Milvus（分布式）或 FAISS（纯内存，超快）
vector_store = Chroma.from_documents(
    documents=chunks,                    # 85 个文本块
    embedding=embedding,                 # Embedding 模型 → 把文本变成向量
    persist_directory="./chroma_agent_db",  # 存到磁盘，下次直接加载，不用重新 Embedding
)
print(f"\n向量库已创建，共 {len(chunks)} 条向量，保存在 ./chroma_agent_db/")

# ----- 检索测试 -----
# retriever = 检索器，as_retriever 把向量库包装成"问一句→返回相关文档"的接口
retriever = vector_store.as_retriever(search_kwargs={"k": 3})  # k=3 → 只取最相关的前3块
test_question = "怎么创建 Agent？"
retrieved_docs = retriever.invoke(test_question)

print(f"\n=== 检索测试 ===")
print(f"问题: {test_question}")
for i, doc in enumerate(retrieved_docs):
    print(f"\n--- 第{i+1}名（余弦相似度最高）---")
    print(f"来源: {doc.metadata['source']} 第{doc.metadata['page']}页")
    print(f"内容: {doc.page_content[:150]}")

# 检索原理一句话：
#   用户问 → Embedding → 向量 Q
#   库里的85个块向量里 → 找 cos(Q, D_i) 最大的前k个
#   这和 Transformer 自注意力 Q@K^T 是同一个数学操作

# ========== 第7章：RAG 检索链（检索 + LLM 生成）==========
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

# ----- 1. 初始化 LLM -----
llm = init_chat_model(
    model="deepseek-v4-flash",
    model_provider="deepseek",
    api_key="sk-20200342f04849fd955dc4cfb0e9ae6b",
    temperature=0,  # RAG 问答不需要创意，0=稳定输出
)

# ----- 2. 定义 RAG Prompt 模板 -----
# {context} = 检索出来的文档内容，{question} = 用户问题
rag_prompt = ChatPromptTemplate.from_template("""
你是 LangChain 技术专家，请根据以下参考资料回答用户问题。

【参考资料】
{context}

【用户问题】
{question}

回答要求：
- 如果参考资料中有答案，请准确引用
- 如果参考资料中没有相关信息，请明确说"根据现有资料无法回答"
- 不要编造参考资料中没有的信息
""")

print(f"\n=== RAG 问答测试 ===")
questions = [
    "怎么创建 Agent？",
    "Middleware 有哪些类型？",
    "今天天气怎么样？",  # 故意问一个资料里没有的，测试防幻觉
]

for q in questions:
    # Step 1: 检索相关文档
    docs = retriever.invoke(q)
    # Step 2: 把文档拼成 context 字符串
    context = "\n\n".join(
        f"[来源: {d.metadata['source']} 第{d.metadata['page']}页]\n{d.page_content}"
        for d in docs
    )
    # Step 3: 填充 Prompt → LLM 生成
    messages = rag_prompt.invoke({"context": context, "question": q})
    answer = llm.invoke(messages)
    print(f"\n{'─'*50}")
    print(f"👤 问题: {q}")
    print(f"🤖 回答: {answer.content[:300]}")

# RAG 完整链路（和第3章全景图对应）：
#   用户问 → 向量检索(第6章) → 获取文档块 → 拼入Prompt(第7章) → LLM生成 → 返回答案
#   这就是课件第3页那两条流中的"用户检索流（在线）"

# ========== 第8章：Agentic RAG — 让 RAG 拥有自主决策能力 ==========
#
# 【核心哲学：从"条件反射"到"自主判断"】
#
#   传统 RAG（第7章）：用户问 → 必须检索 → 拼 Prompt → 生成回答
#     → 流程固定，无论问题是否需要检索，都有开销
#     → 就像一个只会"闻到饭香就流口水"的巴甫洛夫狗
#
#   Agentic RAG（本章）：用户问 → Agent 思考 → 自己决定"查不查？查什么？查几次？"
#     → Agent 判断：技术问题→检索，问候→跳过，常识→直接答
#     → 课件原文：「将传统流水线升级为智能任务工作流」
#
# 【Agent 的 4 步决策循环（课件 8.1 节）】
#   ① 问题理解：这是技术问题？闲聊？计算？
#   ② 能力映射：知识库能答吗？需要外部工具吗？
#   ③ 决策执行：先搜A→再算B→最后总结
#   ④ 反思验证：中间结果对吗？需要再搜一次吗？
#
# 【两种 Agent 模式】
#   模式一：单任务决策（当前代码）→ get_agent 只判断"要不要检索"
#   模式二：ReAct 模式 → 思考→行动→观察 循环，适合需要多步推理的复杂任务
#   模式三：StateGraph 编排 → 多个 Agent 协作，适合条件分支多的长流程

from langchain.agents import create_agent
from langchain.tools import tool

# ----- Step 1: 把检索器包装成 Tool -----
# 关键：Agent 只能调用 Tool，不能直接调用 retriever
# 所以把 retriever.invoke() 包一层 @tool，让 Agent "看见"这个能力
@tool
def search_knowledge(question: str) -> str:
    """【工具说明书——给模型看的】
    在 LangChain 知识库中搜索技术文档。
    适用场景：用户问 LangChain / Agent / Middleware / Tools / create_agent 等技术问题时。
    不适用场景：问候、闲聊、常识、非技术问题。
    返回：相关的文档片段及来源页码。
    """
    docs = retriever.invoke(question)
    return "\n\n".join(
        f"[来源: {d.metadata['source']} 第{d.metadata['page']}页]\n{d.page_content[:300]}"
        for d in docs
    )
#   ↑ 注意：@tool 的 docstring（三引号）Agent 能读到，# 注释读不到
#     所以工具说明书必须写在 docstring 里，这是给 Agent 看的"使用手册"

# ----- Step 2: 创建 Agentic RAG Agent -----
# 和 chenkao.py 的 create_agent 完全一样，只是 tools 里放的是 search_knowledge
agentic_rag = create_agent(
    model=llm,
    tools=[search_knowledge],          # Agent 的技能：会查知识库
    system_prompt="""你是 LangChain 技术专家助手。

决策规则（按优先级）：
1. 技术问题（Agent / Tools / Middleware / LangChain / RAG）→ 必须先用 search_knowledge 查资料，再基于资料回答
2. 问候 / 闲聊 / 心情 / 常识问题 → 直接回答，绝对不要检索
3. 如果查到的资料不足以回答，明确说"根据现有资料无法完全确定"，不要编造
4. 回答时注明信息来源（出处页码）

你的核心价值：不是知道一切，而是知道什么时候该查资料。
""",
)
# system_prompt = Agent 的"人设 + 行为准则"，决定 Agent 的决策倾向
# 【对比】第7章的 rag_prompt 只是模板，Agent 每次都填进去检索
#         本章的 system_prompt 是 Agent 的"大脑"，它决定自己调不调工具

# ----- Step 3: 对比测试 — 基础 RAG vs Agentic RAG -----
print(f"\n{'='*60}")
print("第8章：Agentic RAG 测试 — Agent 自主决定是否检索")
print(f"{'='*60}")

test_pairs = [
    ("怎么创建 Agent？",            "技术问题 → Agent 应主动检索"),
    ("你好，早上好！",               "问候 → Agent 应跳过检索，直接答"),
    ("Python 是什么？",             "常识 → Agent 应跳过检索，直接答"),
]

for q, expected in test_pairs:
    print(f"\n{'─'*50}")
    print(f"👤 {q}")
    print(f"💡 预期: {expected}")
    result = agentic_rag.invoke(
        {"messages": [{"role": "user", "content": q}]}
    )
    # 从消息列表里提取最后一条 AI 回复
    msgs = result.get("messages", [])
    answer = msgs[-1].content if msgs else "无回答"
    print(f"🤖 {answer[:250]}")

    # 检查 Agent 是否调了 search_knowledge
    # 原理：遍历所有消息，看有没有 AIMessage 的 tool_calls 字段非空
    #       如果有 → Agent 决定检索了；如果没有 → Agent 直接回答
    tool_called = any(
        hasattr(m, "tool_calls") and m.tool_calls for m in msgs
    )
    print(f"🔧 Agent 是否检索: {'是 ✅' if tool_called else '否 — 直接回答'}")

# ----- 三种 RAG 方案对比 -----
# ┌────────────┬──────────────────┬──────────────────┬────────────────────┐
# │            │ 第6章 纯检索       │ 第7章 基础RAG      │ 第8章 Agentic RAG  │
# ├────────────┼──────────────────┼──────────────────┼────────────────────┤
# │ 怎么工作    │ retriever.invoke  │ 检索→固定拼Prompt │ Agent 自主决定查不查  │
# │ 检索时机    │ 调用方决定         │ 每次都查           │ Agent 自己判断       │
# │ 灵活性      │ 低               │ 中               │ 高                  │
# │ 浪费检索    │ 取决于调用方       │ 是（问候也查）     │ 否（Agent 判断跳过）  │
# │ 适用场景    │ 底层组件           │ 简单问答机器人      │ 复杂多工具智能助手    │
# └────────────┴──────────────────┴──────────────────┴────────────────────┘
#
# 【核心要点】
#   一句总结：Agentic RAG = Agent + search_knowledge 工具
#   和 chenkao.py 的区别：chenkao 的工具是 ask_airport / book_hotel（业务API）
#                      本章的工具是 search_knowledge（知识库检索）
#   本质相同：都是让 Agent 自主决定"何时用哪个工具"
