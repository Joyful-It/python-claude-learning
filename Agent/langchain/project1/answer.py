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
    model_kwargs={"device": "cpu"}       # 用 CPU 跑，不吃显卡
)

# ─── 第4步：存入向量数据库 ───────────────────────────────
# Chroma = 轻量级本地向量库
#   from_documents() 做了两件事：
#     ① 调 embedding 把每个 chunk 变成向量
#     ② 把向量 + 原文一起存到磁盘
# persist_directory = 存盘路径，下次直接加载，不用重新 Embedding
# Chroma ≠ Embedding 模型！口诀: "Chrom 存，BGE 算"
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,                      # 用哪个模型把文本变成向量
    persist_directory="./chroma_chatpdf_db"   # 存到磁盘，重启不丢
)
print(f"✅ 向量库已构建: {len(chunks)} 条向量 → ./chroma_chatpdf_db/")

# ─── 第5步：创建检索器 ───────────────────────────────────
# as_retriever() = 把向量库包装成"问一句→返回相关文档"的接口
# k=3 = 每次检索返回最相关的 3 个文本块
# search_type="similarity" = 默认余弦相似度检索（和 Transformer 自注意力 Q@K^T 同操作）
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# ─── 第6步：初始化 LLM ──────────────────────────────────
llm = init_chat_model(
    model="deepseek-v4-flash",
    model_provider="deepseek",
    api_key="sk-20200342f04849fd955dc4cfb0e9ae6b",
    temperature=0   # RAG 问答需要稳定输出，0=不随机
)

# ─── 第7步：定义 RAG Prompt 模板 ──────────────────────────
# {context} = 检索出来的文档片段（由 retriever 自动填入）
# {question} = 用户输入的问题
rag_prompt = ChatPromptTemplate.from_template("""
你是文档助手，请根据以下参考资料回答用户问题。

【参考资料】
{context}

【用户问题】
{question}

回答要求：
- 如果参考资料中有答案，准确引用并注明来源页码
- 如果参考资料中没有相关信息，明确说"文档中未找到相关内容"
- 不要编造资料中没有的信息
""")

print("\n📚 ChatPDF 初始化完成！输入 'quit' 退出\n")


# ╔══════════════════════════════════════════════════════════╗
# ║              交互层 — while True 循环                    ║
# ╚══════════════════════════════════════════════════════════╝

while True:
    # ① 接收用户输入
    user_input = input("👤 你：")
    if user_input.lower() in ("quit", "exit", "q"):
        print("👋 再见！")
        break

    # ② 检索相关文档块
    retrieved_docs = retriever.invoke(user_input)

    # ③ 拼接上下文（带来源标注）
    context = "\n\n".join(
        f"[来源: {d.metadata['source']} 第{d.metadata['page']}页]\n{d.page_content}"
        for d in retrieved_docs
    )

    # ④ 填充 Prompt → LLM 生成
    messages = rag_prompt.invoke({"context": context, "question": user_input})
    answer = llm.invoke(messages)

    print(f"🤖 {answer.content}\n")
