# 30天 Agent 开发面试冲刺计划

> **起止日期**：2026-06-18 ~ 2026-07-17
> **每日投入**：~3小时（晨考30min + 主线90min + 项目映射30min + 自由补洞30min）
> **目标岗位**：Agent开发工程师 > 大模型应用开发工程师 > AI应用工程师
> **优先级**：Agent > RAG > LLM精选 > Python工程 > 微调精选 > 计算机基础

---

## 30天分配

| 阶段 | 主线 | 天数 | 日期 |
|------|------|------|------|
| 1 | ① Agent | 10 | Day 1-10 (6/18-6/27) |
| - | 🔥 周输出1 | 1 | Day 7 (6/24) |
| 2 | ② RAG | 4 | Day 11-14 (6/28-7/01) |
| - | 🔥 周输出2 | 1 | Day 15 (7/02) |
| 3 | ④ LLM精选 | 4 | Day 16-19 (7/03-7/06) |
| 4 | ③ Python工程 | 4 | Day 20-23 (7/07-7/10) |
| - | 🔥 周输出3 | 1 | Day 23 (7/10) |
| 5 | ⑤ 微调精选 | 3 | Day 24-26 (7/11-7/13) |
| 6 | ⑥ 计算机基础 | 2 | Day 27-28 (7/14-7/15) |
| 7 | 🔥 冲刺 | 2 | Day 29-30 (7/16-7/17) |

---

## 每天训练流程（3小时）

```
A层 晨考 ~30min
  18题抽题 → 每题标注树路径 → 答错记录薄弱点

B层 主线面试训练 ~90min
  阶段一 知识点提问（30min）
  阶段二 连接提问（40min）
  阶段三 面试表达（20min）

C层 项目映射 ~30min
  每个知识点追问：在Teach-Agent哪里体现？

D层 自由补洞 ~30min
  当天暴露的薄弱点 → 快速巩固
```

---

## 阶段1：Agent（Day 1-10）

### Day 1-2：Prompt + Tool Calling
- System Prompt / Prompt Injection
- Function Calling 原理 / Tool 定义三要素
- Tool vs Agent vs LLM
- LangChain 三大核心
- **面试表达**："从System Prompt讲到Tool定义三要素"
- **项目映射**：teach-agent的System Prompt设计 / Tool封装

### Day 3-4：ReAct
- ReAct 四步循环 / 消息流转
- AutoGPT / BabyAGI 循环
- 死循环防护
- **面试表达**："请讲AutoGPT think→act→route循环"
- **项目映射**：teach-agent的ReAct循环设计

### Day 5-6：Memory + LangGraph 核心
- 短期/长期记忆 / Checkpointer / thread_id
- State/TypedDict/MessagesState / Node返回规则
- LangGraph 四步搭建 / vs LangChain
- **面试表达**："从State讲到compile+invoke"
- **项目映射**：teach-agent的State/Checkpointer设计

### Day 7-8：LangGraph 进阶 + Multi-Agent
- 条件边 / Fan-out/Fan-in / HITL / Middleware
- Supervisor / 三种模式 / 多Agent vs 单Agent
- **面试表达**："从单Agent讲到多Agent Supervisor"
- **项目映射**：teach-agent需要HITL吗？需要多Agent吗？

### 🔥 Day 7：Agent周输出（不看资料，连续15分钟）
主题：什么是Agent → 为什么Agent → Prompt → Tool → ReAct → Memory → LangGraph → Multi-Agent

### Day 9-10：MCP + Agent评估 + Agent线完整串联
- MCP 概念/架构/传输 / vs Tool Calling
- LangSmith / 错误处理
- **面试表达**："从Prompt讲到Multi-Agent+MCP"（10分钟完整输出）
- **项目映射**：teach-agent用MCP还是@tool？

---

## 阶段2：RAG（Day 11-14）

### Day 11：RAG 基础
- RAG 核心概念 / 六站管道 / vs 微调 / HF组件
- **面试表达**："请讲RAG六站管道"

### Day 12：文档处理 + Embedding
- Document / 分块 / Chunk大小
- Embedding原理 / 模型选择 / 余弦相似度
- **面试表达**："Chunk大小怎么定？为什么选BGE？"

### Day 13：向量库 + 检索
- Chroma / FAISS / Milvus 对比
- TopK / BM25 / 混合检索 / Rerank
- **面试表达**："从检索到Rerank的完整策略"

### Day 14：防幻觉 + Agentic RAG + RAG线串联
- 幻觉/防幻觉 / Query Rewrite / 评估
- Agentic RAG / Self-RAG / 多轮检索
- **面试表达**："从RAG讲到Agentic RAG"

### 🔥 Day 15：RAG+Agent 周输出（不看资料，连续15分钟）
主题：RAG全链路 + Agentic RAG + 与Agent结合

---

## 阶段3：LLM精选（Day 16-19）

### Day 16：神经网络基础 + 损失函数
- 神经元/激活函数/反向传播
- 训练循环五步 / Softmax / 交叉熵
- **面试表达**："请讲训练循环五步"

### Day 17：Transformer + Attention
- Self-Attention五步 / QKV / √dₖ
- Multi-Head / FFN / 残差
- **面试表达**："请手推Attention公式"

### Day 18：GPT/BERT + Prompt Engineering
- Encoder/Decoder / BERT(MLM) / GPT(Next Token)
- 五种提示词技术 / Context Engineering
- **面试表达**："BERT和GPT核心区别"

### Day 19：位置编码 + 归一化 + 推理优化
- Sinusoidal/RoPE / Pre-LN vs Post-LN / KV Cache
- **面试表达**："Pre-LN和Post-LN为什么GPT选Pre-LN？"

---

## 阶段4：Python工程（Day 20-23）

### Day 20：函数 + OOP
- 四种参数 / *args/**kwargs / lambda
- 类/继承/多态/封装
- **面试表达**："*args/**kwargs顺序 + OOP三大特性"

### Day 21：NumPy/Pandas + JSON/API
- 广播vs向量化 / DataFrame操作 / 数据清洗
- JSON/dumps-loads / API调用
- **面试表达**："数据清洗标准流程"

### Day 22：FastAPI
- 路由/参数 / Pydantic / Depends / async
- **面试表达**："FastAPI为什么适合Agent服务？"

### Day 23：工程化
- Git / Docker / Redis / 项目结构
- 🔥 **技术栈总结**（不看资料，连续20分钟）

---

## 阶段5：微调精选（Day 24-26）

### Day 24：SFT + LoRA/QLoRA
- SFT / 全参vs高效 / LoRA原理(ΔW=B×A)
- QLoRA / 训练参数/推理合并
- **面试表达**："LoRA原理+为什么省显存"

### Day 25：RLHF/DPO + 蒸馏量化
- RLHF流程 / DPO替代PPO / GRPO
- 蒸馏/量化对比
- **面试表达**："DPO为什么替代PPO"

### Day 26：推理部署 + 微调线串联
- 显存评估 / vLLM/Ollama
- RAG vs LoRA 选型决策
- **面试表达**："RAG还是微调？决策标准"

---

## 阶段6：计算机基础（Day 27-28）

### Day 27：数据库
- MySQL / SQLAlchemy / Redis

### Day 28：前端+软件工程+数学
- HTML/CSS/JS / Git/敏捷 / 概率论/信息论

---

## 阶段7：冲刺（Day 29-30）

### Day 29：综合模拟面试
- 随机主线，连续追问20分钟
- 模拟真实面试节奏

### 🔥 Day 30：Teach-Agent 项目完整演示
- 15-20分钟项目陈述
- 架构→数据流→技术选型→踩坑→优化
- 面试官追问应对

---

## 高频面试节点清单

| 节点 | 知识树路径 | 面试必问理由 |
|------|-----------|---------|
| Tool Calling原理 | ①→1.2 | 90% Agent JD第一问 |
| ReAct循环 | ①→1.3 | Agent核心机制 |
| LangGraph State/Node/Edge | ①→1.5 | 项目技术栈高频 |
| Multi-Agent Supervisor | ①→1.6 | 架构设计必问 |
| RAG六站管道 | ②→2.1 | 知识库项目标配 |
| Embedding/向量库选型 | ②→2.3/2.4 | 项目技术决策 |
| Attention公式手推 | ④→4.3 | Transformer面试第一题 |
| GPT vs BERT | ④→4.6 | 基础区分 |
| Prompt Engineering | ④→4.8 | Agent底层能力 |
| LoRA原理ΔW=B×A | ⑤→5.2 | 微调高频 |
| OOP三大特性 | ③→3.3 | Python基础必问 |
| FastAPI参数类型 | ③→3.7 | 后端基础 |

---

## Teach-Agent 项目重点映射

| 树节点 | 在项目中哪里 | 面试时怎么说 |
|--------|---------|---------|
| ① 1.1 System Prompt | 定义角色/教学理念 | "我在System Prompt注入了苏格拉底教学法" |
| ① 1.2 Tool Calling | 检索+出题工具 | "家教有两个Tool：retrieve和quiz" |
| ① 1.3 ReAct | 提问→检索→思考→回答 | "每次学生提问走完整ReAct循环" |
| ① 1.4 Memory | Checkpointer+thread_id | "MemorySaver做多学生隔离" |
| ① 1.5 LangGraph | State/Node/ConditionalEdge | "ConditionalEdge按理解程度分流" |
| ① 1.6 Multi-Agent | Supervisor分派子Agent | "三个子Agent完成教学闭环" |
| ② 2.8 Agentic RAG | Agent自主决定检索 | "Agent判断知识型还是对话型" |
| ③ 3.7 FastAPI | 后端API层 | "FastAPI+Pydantic做接口验证" |
| ④ 4.8 Prompt Engineering | 引导式提问 | "Few-Shot控制引导风格" |

---

> 📅 开始日期：2026-06-18（Day 1）
> ⚠️ 铁律：不再大改计划。看到新JD/新框架/新学习法，先记下来，30天后再优化。
