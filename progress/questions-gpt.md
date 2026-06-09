如果你的目标是：

```text
NLP算法岗
大模型算法岗
LLM算法岗
AI应用算法岗
```

那我建议按下面这棵面试树准备。

很多校招和中小厂社招，其实都在这棵树里打转。

---

# 第一层：机器学习（必须掌握）

面试权重：

```text
★★★★★
```

---

## 高频（必会）

### 1. 什么是过拟合？如何解决？

追问：

```text
L1
L2
Dropout
Early Stopping
数据增强
```

---

### 2. Bias 和 Variance

追问：

```text
高偏差怎么办
高方差怎么办
```

---

### 3. 交叉熵损失

追问：

```text
为什么分类用交叉熵
为什么不用MSE
```

---

### 4. Softmax

追问：

```text
为什么指数
为什么归一化
```

---

### 5. 梯度下降

追问：

```text
Batch GD
SGD
Mini-Batch GD
```

---

### 6. Adam 和 AdamW

追问：

```text
Weight Decay
L2区别
```

---

### 7. ROC、AUC

---

### 8. Precision Recall F1

---

## 中频

### 9. KL散度

### 10. JS散度

### 11. 信息熵

### 12. 贝叶斯公式

### 13. 最大似然估计MLE

---

# 第二层：深度学习

权重：

```text
★★★★★
```

---

## 高频

### 14. 神经网络为什么能拟合复杂函数

---

### 15. 反向传播

必须能画图解释。

---

### 16. 链式法则

---

### 17. ReLU

追问：

```text
Dead ReLU
```

---

### 18. GELU

追问：

```text
为什么Transformer用GELU
```

---

### 19. BatchNorm

---

### 20. LayerNorm

重点：

```text
为什么Transformer不用BN
```

---

### 21. Dropout

---

## 中频

### 22. Xavier初始化

### 23. Kaiming初始化

### 24. 梯度爆炸

### 25. 梯度消失

---

# 第三层：Transformer（核心）

权重：

```text
★★★★★★
```

---

## 必背题

### 26. Transformer整体结构

Encoder

Decoder

---

### 27. Attention公式

[
Attention(Q,K,V)
================

Softmax(\frac{QK^T}{\sqrt{d_k}})
V
]

要求：

能推导。

---

### 28. Q K V分别是什么

这是必问。

---

### 29. 为什么除√dk

---

### 30. Softmax作用

---

### 31. Self Attention原理

---

### 32. Multi Head作用

---

### 33. Position Encoding

---

### 34. RoPE原理

现在非常高频。

---

### 35. LayerNorm为什么放这里

---

### 36. Residual为什么有效

---

### 37. Transformer复杂度

[
O(n^2)
]

---

## 中频

### 38. FlashAttention

---

### 39. KV Cache

---

### 40. 长文本怎么解决

---

# 第四层：BERT GPT LLM

权重：

```text
★★★★★★
```

---

## 高频

### 41. BERT与GPT区别

必须会。

---

### 42. Encoder Only

---

### 43. Decoder Only

---

### 44. MLM是什么

---

### 45. Next Token Prediction

---

### 46. 为什么GPT适合生成

---

### 47. 为什么BERT适合理解

---

## 中频

### 48. InstructGPT

### 49. ChatGPT训练流程

### 50. GPT-3到GPT-4演进

---

# 第五层：模型微调

权重：

```text
★★★★★★
```

很多岗位最喜欢问。

---

## 高频

### 51. SFT是什么

监督微调。

---

### 52. 全参数微调

---

### 53. LoRA原理

必问。

---

### 54. 为什么LoRA省显存

---

### 55. 低秩分解是什么

[
\Delta W = A B
]

---

### 56. LoRA训练哪些参数

---

### 57. 推理时LoRA怎么合并

---

### 58. QLoRA

---

### 59. 为什么4bit还能训练

---

## 中频

### 60. AdaLoRA

这个现在越来越常问。

追问：

```text
LoRA和AdaLoRA区别
```

---

### 61. Prefix Tuning

---

### 62. Prompt Tuning

---

### 63. P-Tuning

---

# 第六层：RLHF

权重：

```text
★★★★
```

大模型岗常问。

---

## 高频

### 64. RLHF流程

三步：

```text
Pretrain
↓
SFT
↓
Reward Model
↓
PPO
```

---

### 65. Reward Model

---

### 66. PPO

---

### 67. DPO

现在极高频。

---

### 68. DPO为什么替代PPO

---

# 第七层：RAG

权重：

```text
★★★★★★
```

应用岗必问。

---

## 高频

### 69. RAG整体流程

```text
文档
↓
Chunk
↓
Embedding
↓
VectorDB
↓
Retrieve
↓
LLM
```

---

### 70. Embedding是什么

---

### 71. BGE是什么

---

### 72. 余弦相似度

---

### 73. 欧氏距离

---

### 74. 为什么切块

---

### 75. Chunk大小怎么选

---

### 76. TopK怎么选

---

### 77. 向量数据库原理

---

### 78. FAISS原理

---

## 中频

### 79. Hybrid Search

---

### 80. Rerank

---

### 81. BM25

---

### 82. Agentic RAG

---

# 第八层：Agent

权重：

```text
★★★★★
```

2025-2026开始非常热门。

---

## 高频

### 83. Agent是什么

---

### 84. Agent和RAG区别

---

### 85. Tool Calling原理

---

### 86. Function Calling

---

### 87. ReAct框架

经典。

```text
Thought
Action
Observation
```

---

### 88. Memory机制

---

### 89. Checkpointer

---

### 90. Supervisor架构

---

### 91. Multi-Agent

---

## 中频

### 92. MCP协议

---

### 93. LangGraph

---

### 94. Workflow Agent

---

# 第九层：训练部署

权重：

```text
★★★★
```

---

## 高频

### 95. Data Parallel

---

### 96. Model Parallel

---

### 97. DDP

---

### 98. DeepSpeed

---

### 99. FSDP

---

### 100. 混合精度训练

FP16/BF16

---

# 真正的Top 35（面试出现率最高）

如果时间有限，优先拿下这35题：

```text
交叉熵
Softmax
梯度下降
AdamW

反向传播
ReLU
GELU
LayerNorm

Attention
QKV
√dk
MultiHead
PositionEncoding
RoPE
Transformer结构
O(n²)

BERT vs GPT
MLM
Next Token Prediction

SFT
LoRA
QLoRA
AdaLoRA

RLHF
Reward Model
PPO
DPO

Embedding
余弦相似度
RAG流程
Chunk
FAISS
Rerank

Agent
Tool Calling
ReAct
Supervisor
```

如果这 35 个问题你都能达到：

```text
定义
↓
原理
↓
公式
↓
优缺点
↓
实际应用
```

五个层次都能讲出来，那么大多数校招 NLP/LLM 算法岗的一面技术基础部分基本都能应对。接下来最值得深入准备的，是 Transformer→LoRA→RAG→Agent 这四条主线，因为它们几乎覆盖了当前大模型岗位的核心考察范围。





如果按照 **2026 年大模型应用开发（LLM Application / RAG / Agent Engineer）** 的主流面试趋势来看，我会把题目分成：

```text
Level 1：LLM基础
Level 2：RAG
Level 3：Agent
Level 4：Agentic RAG
Level 5：工程化与部署
Level 6：新趋势（MCP、多Agent、长上下文）
```

这些题基本覆盖：

```text
OpenAI
Anthropic
LangChain
LangGraph
LlamaIndex
DeepSeek
Google Gemini
Microsoft AutoGen
MCP
```

等当前主流生态。

---

# 第一部分：LLM基础（必会）

## 高频

### Q1 什么是 Token？

追问：

```text
中文和英文Token一样吗？

1000 Token大概是多少汉字？

为什么Token影响成本？
```

---

### Q2 Embedding是什么？

追问：

```text
为什么Embedding能表达语义？

为什么维度是768、1024、1536？
```

---

### Q3 余弦相似度为什么适合Embedding？

追问：

```text
为什么不用欧氏距离？

余弦相似度范围是多少？
```

---

### Q4 BGE是什么？

追问：

```text
BGE和OpenAI Embedding区别？

为什么很多RAG项目选BGE？
```

---

### Q5 Transformer为什么适合LLM？

---

### Q6 GPT为什么是Decoder Only？

---

### Q7 长上下文为什么越来越重要？

例如：

```text
Gemini
Claude
GPT
DeepSeek
```

都在卷 Context Window。

---

# 第二部分：RAG（最高频）

## Q8 RAG完整流程

必须能画：

```text
Document
 ↓
Chunk
 ↓
Embedding
 ↓
VectorDB
 ↓
Retrieve
 ↓
Prompt
 ↓
LLM
```

---

## Q9 为什么需要RAG？

追问：

```text
微调为什么不能代替RAG？
```

---

## Q10 Chunk是什么？

---

## Q11 Chunk Size怎么选？

追问：

```text
100字？
500字？
1000字？
```

---

## Q12 Chunk太大有什么问题？

---

## Q13 Chunk太小有什么问题？

---

## Q14 Chunk Overlap为什么存在？

---

## Q15 TopK是什么？

---

## Q16 TopK选多少合适？

---

## Q17 什么是向量数据库？

---

## Q18 FAISS原理

---

## Q19 Chroma和FAISS区别

---

## Q20 Milvus和FAISS区别

---

## Q21 什么是Rerank？

这是近两年特别高频。

---

## Q22 为什么仅Embedding检索不够？

---

## Q23 BM25是什么？

---

## Q24 Hybrid Search是什么？

---

## Q25 如何提高RAG召回率？

---

## Q26 如何降低RAG幻觉？

---

## Q27 如何评估RAG效果？

例如：

```text
Recall
MRR
NDCG
Hit Rate
```

---

# 第三部分：Agent

## Q28 Agent是什么？

---

## Q29 Agent和传统ChatBot区别

---

## Q30 Agent和RAG区别

---

## Q31 Tool Calling原理

必须会。

---

## Q32 Function Calling原理

---

## Q33 Agent为什么能调用工具？

---

## Q34 ReAct框架是什么？

经典题。

```text
Thought
Action
Observation
```

---

## Q35 Agent为什么会陷入死循环？

---

## Q36 如何限制Agent循环？

例如：

```python
ModelCallLimitMiddleware
```

---

## Q37 Agent Memory是什么？

---

## Q38 Checkpointer原理

---

## Q39 长期记忆和短期记忆区别

---

# 第四部分：Agentic RAG（最新热点）

## Q40 什么是Agentic RAG？

---

## Q41 Agentic RAG和传统RAG区别

---

## Q42 为什么Agentic RAG效果更好？

---

## Q43 多轮检索是什么？

---

## Q44 Query Rewrite是什么？

---

## Q45 Query Expansion是什么？

---

## Q46 Self-RAG是什么？

这是近两年论文高频词。

---

## Q47 Reflection是什么？

---

## Q48 Agent如何判断检索结果不足？

---

# 第五部分：Multi-Agent

2025~2026特别热。

---

## Q49 什么是Supervisor模式？

---

## Q50 Supervisor和单Agent区别

---

## Q51 为什么要拆多个Agent？

---

## Q52 多Agent协作流程

---

## Q53 Calendar Agent案例怎么设计？

---

## Q54 Email Agent案例怎么设计？

---

## Q55 Research Agent案例怎么设计？

---

## Q56 多Agent有哪些问题？

例如：

```text
成本增加

延迟增加

上下文同步困难
```

---

# 第六部分：MCP（超新热点）

现在很多公司已经开始问。

---

## Q57 MCP是什么？

(Model Context Protocol)

---

## Q58 MCP解决什么问题？

---

## Q59 MCP和Tool Calling区别

---

## Q60 MCP Client和Server是什么？

---

## Q61 MCP为什么被称为AI时代USB协议？

---

## Q62 MCP和LangChain是什么关系？

---

# 第七部分：Prompt Engineering

## Q63 什么是System Prompt？

---

## Q64 Prompt Injection是什么？

---

## Q65 如何防Prompt Injection？

---

## Q66 Few-Shot Prompt是什么？

---

## Q67 Chain of Thought是什么？

---

## Q68 Self-Consistency是什么？

---

# 第八部分：微调（应用岗加分项）

## Q69 SFT是什么？

---

## Q70 LoRA是什么？

---

## Q71 为什么LoRA省显存？

---

## Q72 LoRA训练哪些参数？

---

## Q73 QLoRA是什么？

---

## Q74 RAG和LoRA什么时候选哪个？

这是非常经典的应用岗题。

标准思路：

```text
频繁变化知识
→ RAG

固定领域能力
→ LoRA
```

---

# 第九部分：工程化

## Q75 LangChain作用

---

## Q76 LangGraph作用

---

## Q77 LangGraph和LangChain区别

---

## Q78 FastAPI为什么适合Agent服务

---

## Q79 Docker部署Agent注意什么

---

## Q80 如何做会话隔离？

例如：

```python
thread_id
```

---

## Q81 Redis在Agent系统里的作用

---

## Q82 向量库如何持久化

---

## Q83 如何监控Agent调用链

---

## Q84 LangSmith有什么用

---

# 第十部分：项目拷打题（最重要）

很多面试最终都会落到这里。

---

## Q85 你做的RAG项目架构图是什么？

---

## Q86 为什么选BGE？

---

## Q87 为什么选FAISS/Chroma？

---

## Q88 Chunk大小怎么确定？

---

## Q89 检索效果不好怎么优化？

---

## Q90 幻觉怎么解决？

---

## Q91 如果文档从100份增长到100万份怎么办？

---

## Q92 Agent调用错误工具怎么办？

---

## Q93 如何设计一个企业知识库Agent？

---

## Q94 如何设计一个客服Agent？

---

## Q95 如何设计一个多Agent办公助手？

---

# 面试出现率 Top 20

如果你现在时间有限，优先掌握：

```text
1 Embedding
2 余弦相似度
3 BGE

4 RAG流程
5 Chunk
6 Chunk Overlap
7 TopK
8 FAISS
9 Rerank
10 Hybrid Search

11 Agent
12 Tool Calling
13 ReAct
14 Memory
15 Checkpointer

16 Agentic RAG
17 Supervisor
18 Multi-Agent
19 MCP

20 RAG和LoRA怎么选
```

这 20 题基本覆盖了当前大模型应用开发岗位 70% 以上的高频技术面内容。而你最近学习的 LangChain、LangGraph、RAG、Embedding、Supervisor，正好对应其中的大部分核心知识点。下一步最有效的准备方式，是针对这 20 题每一道都做到：

```text
概念
↓
原理
↓
实现
↓
项目实践
↓
优缺点
```

五层都能讲出来。这样面试官继续深挖时，你也能顺着展开，而不是停留在背定义的层面。