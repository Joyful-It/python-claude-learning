# 学习会话记录 - 2026-06-05

## 今日理解跃迁

> 从"RAG就是查知识库" → "RAG是完整的六站管道（加载→分块→向量化→检索→生成→Agent决策），Agentic RAG把固定流程升级为自主判断"

---

## 会话概览

- **日期**：2026-06-05
- **核心主题**：基于 LangChain 实现 RAG 完整教程（第1-8章精讲 + 9-12章速览）+ 晨间复习9题
- **课件**：`Knowledge_base/基于 LangChain 实现 RAG 完整技术教程.pdf`（59页）
- **代码文件**：`Agent/langchain/rag_document1.py`（完整RAG管道）、`Agent/langchain/rag_document2.py`（PyPDFLoader版）、`Agent/langchain/chenkao.py`

---

## 学员提出的问题（原文）

- "文件太大了吗，document文件就是刚才代码输出的那些东西吧"
- "递归的意思是一层套一层，直到条件吻合"
- "一个将文件的信息返回出来，包括内容，页码，作者。普通的就是pdf文件的内容"
- "RAG是对知识库进行检索，agent对模型进行提升"
- "最大不同是决定怎么查资料"
- "相乘呗，就像transformer一样，话说这个思想他们两个是谁先提出的"
- "chorma 在线比如智谱，或者ollam本地部署"（混淆了Chroma向量库和Embedding模型）
- "检索增强输出"（差Generation）
- "第七章什么意思，是写提示词吗"

---

## 概念与教学内容

### 1. 第4章：文档加载（Document Loading）

**Document 对象** = LangChain 的原子单位：
- `page_content` → 文本内容（"肉"）
- `metadata` → 身份证信息（source/page/author/date）

**两种加载方式**：
- PyPDFLoader（自动挡）→ 一行代码，但导入链可能触发 transformers 依赖问题
- pypdf + 手动包装（手动挡）→ 绕过依赖，更可控

**多格式支持**：PDF/网页(WebBaseLoader)/Markdown/代码仓库/CSV/JSON

### 2. 第5章：文本分块（Text Splitting）

**为什么分块**：①超token上限截断 ②粗粒度检索不精准

**RecursiveCharacterTextSplitter**：递归逐级分隔符
```
\n\n（段落）→ \n（行）→ 。（句）→ " "（词）→ ""（字符硬切）
```

**关键参数**：
- `chunk_size=500`：每块最大字符数
- `chunk_overlap=50`：相邻块重叠，防关键信息被切断
- 35页 PDF → 85个分块

### 3. 第6章：Embedding + 向量数据库

**Embedding 三种部署路线**：

| 路线 | 例子 | 联网 | 花钱 | 数据出站 |
|------|------|:--:|:--:|:--:|
| ① 云端 API | 智谱/OpenAI | ✅ | ✅ | ✅ |
| ② Ollama 本地 | bge-m3 | ❌ | ❌ | ❌ |
| ③ HuggingFace 直载 | bge-small-zh | ❌ | ❌ | ❌ |

**Chroma 向量库**：轻量级，数据存磁盘（persist_directory），适合学习和中小规模。

**检索原理**：用户问→Embedding→向量Q，库里85个向量→cos(Q,Di)取最大→返回top-k
→ 和 Transformer 自注意力 Q@K^T 同一数学操作！

### 4. 第7章：基础 RAG 检索链

**三步走**：
```python
docs = retriever.invoke(q)           # ① 检索
context = 拼接文档                   # ② 拼上下文
answer = llm.invoke(prompt+context)  # ③ LLM生成
```

**防幻觉关键**：Prompt中明确说"根据现有资料无法回答"——但测试发现LLM有时仍会编造（天气问题说"资料中有北京上海天气"）

### 5. 第8章：Agentic RAG

**核心哲学**：从"条件反射"到"自主判断"
- 传统RAG：每次必查，固定流程
- Agentic RAG：Agent自己决定要不要查、查几次

**Agent 四步决策**：①问题理解→②能力映射→③决策执行→④反思验证

**实现方式**：把 retriever 包装成 @tool → Agent 自主决定是否调用

**对比测试**：技术问题(检索✅)/问候(跳过)/常识(跳过)

### 6. 第9-12章速览

- **混合检索**：向量检索(语义)+BM25(精确关键词)，加权融合
- **重排序**：粗筛top20→Cross-Encoder精排→返回top3
- **查询重写**：补全指代（"它支持多少？"→"LangChain Middleware支持多少？"）
- **LangChain vs LlamaIndex**：前者管"找到后怎么办"，后者管"怎么找"
- 第10章 Docker/监控 → 工程化阶段再看

---

## 今日核心理解

学员对 RAG 完整管道的理解：
> "文件加载，分块，向量化，存入向量库。用户提问，agent识别问题，调用工具或rag，结合llm生成答案"

学员对分块递归机制：
> "对每个符号进行优先级分级，先分大的再分优先级小的"

学员对 PyPDFLoader vs pypdf：
> "一个将文件的信息返回出来，包括内容，页码，作者。普通的就是pdf文件的内容"

学员对 Embedding vs 向量库的混淆：
> "chorma 在线比如智谱，或者ollam本地部署"（纠正：Chroma是向量库，智谱/Ollama是Embedding）

---

## 踩坑与纠正

| 错误 | 纠正 | 原因 |
|------|------|------|
| transformers 再次导入失败 | 降级 tokenizers 0.23.1→0.22.2 + HF镜像站 | 版本冲突 + 国内无法访问HF |
| HF 模型下载失败 | 加 `os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"` | GFW阻断 |
| f-string 引用 `chunk_overlap` | 改为硬编码 "50字重叠" | 变量在参数作用域，非全局 |
| 混淆 Chroma 和 Embedding | Chroma=存向量，BGE/智谱=生成向量 | 向量库 ≠ Embedding 模型 |
| "检索增强输出" | 纠正为 "检索增强生成(Generation)" | 强调LLM自主生成，非简单拼接输出 |

---

## 知识漏洞

- HF 五件套连续三次只记住 4/5（缺 Accelerate）🔴
- 函数参数顺序缺 keyword-only（`*args` 后 `c` 必须关键字传）
- Embedding 模型 vs 向量数据库概念混淆 🆕
- RAG 三字母答成"检索增强输出"（应为Generation）

---

## 关键总结

**RAG 六站管道**：
> 文档加载 → 文本分块 → Embedding 向量化 → 存入向量库 → 检索 → LLM 生成

**Embedding 三路线口诀**：
> 云端花钱省心，Ollama免费吃显存，HuggingFace轻量CPU跑

**RAG vs Agentic RAG**：
> 传统RAG=巴甫洛夫狗(闻到饭香→流口水)，Agentic RAG=有大脑的人(先想：我需要吃吗？)

**递归分块口诀**：
> 段落→行→句→词→字符，层层下探，不超限为止

**Chroma ≠ Embedding 口诀**：
> Chrom存，BGE算——向量库管存储，Embedding管生成

**Document = 双件套**：
> page_content(肉) + metadata(身份证)

---

## 完成的练习

- `Agent/langchain/rag_document1.py`：完整RAG管道（4-8章代码，含详细注释）
- `Agent/langchain/rag_document2.py`：PyPDFLoader版文档加载
- 晨间复习 9 题
- 第9-12章概念速览

---

## 学习效果评估

| 考点 | 前值 | 后值 | 备注 |
|------|------|------|------|
| RAG 完整流程 | 10% | 70% | 六站管道完整理解，能独立说出步骤 |
| 文档加载 Document对象 | 0% | 80% | page_content+metadata 双件套清楚 |
| 文本分块 RecursiveCharSplit | 0% | 75% | 递归分隔符层级理解，能解释为什么要 chunk_overlap |
| Embedding 三路线 | 0% | 65% | 云端/Ollama/HF直载，但 Chroma≠Embedding 混淆待巩固 |
| 基础 RAG 检索链 | 0% | 70% | retrieve→拼Prompt→LLM生成 三步清楚 |
| Agentic RAG | 0% | 60% | 概念清楚(自主判断查不查)，代码已写但未跑通 |
| 混合检索/重排序 | 0% | 30% | 概念速览，未实操 |
| B 模块 RAG | 5% | 35% | 从基本概念到完整管道 |
| C 模块 Agent | 22% | 28% | Agentic RAG 打通 Agent+RAG 联合 |
