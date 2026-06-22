# 注入池B 轻量索引（questions-gpt → 晨考随机抽5题）

> 选号后去 `questions-gpt.md` grep 对应题号取答案正文
> 姊妹文件：`question-index.md`（Bank核心题库）、`knowledge-index-light.md`（注入池A）

---

## 抽题规则
- 每次晨考从本索引**完全随机**抽取 5 题（不限模块）
- 已在 `question-bank.md` 中的跳过（去重）
- 答完后入库 `question-bank.md`，来源标 `gpt-`
- 题目退役后从 `questions-gpt.md` 原料库补新题

---

## 索引

```
ID    问题                                               来源段落
─────────────────────────────────────────────────────────────────────────────
G001  什么是过拟合？如何解决？（L1/L2/Dropout/Early Stop）      gpt-Q1
G002  Bias 和 Variance 的区别？高偏差/高方差怎么办？           gpt-Q2
G003  交叉熵损失 — 为什么分类用交叉熵而不用MSE？               gpt-Q3
G004  Softmax — 为什么用指数？为什么归一化？                   gpt-Q4
G005  梯度下降 — Batch GD / SGD / Mini-Batch GD 区别？        gpt-Q5
G006  Adam 和 AdamW 的区别？Weight Decay 与 L2 的关系？       gpt-Q6
G007  ROC、AUC 是什么？怎么解读？                             gpt-Q7
G008  Precision / Recall / F1 分别是什么？                   gpt-Q8
G009  KL散度是什么？                                         gpt-Q9
G010  JS散度是什么？与KL散度有什么区别？                       gpt-Q10
G011  信息熵是什么？                                          gpt-Q11
G012  贝叶斯公式是什么？                                      gpt-Q12
G013  最大似然估计 MLE 是什么？                               gpt-Q13
G014  神经网络为什么能拟合复杂函数？                            gpt-Q14
G015  反向传播 — 必须能画图解释                               gpt-Q15
G016  链式法则是什么？                                        gpt-Q16
G017  ReLU — Dead ReLU 是什么？怎么解决？                     gpt-Q17
G018  GELU — 为什么 Transformer 用 GELU 而不是 ReLU？         gpt-Q18
G019  BatchNorm 原理？                                       gpt-Q19
G020  LayerNorm — 为什么 Transformer 不用 BN 用 LN？          gpt-Q20
G021  Dropout 原理？训练和推理时有什么不同？                    gpt-Q21
G022  Xavier 初始化是什么？                                   gpt-Q22
G023  Kaiming 初始化是什么？                                  gpt-Q23
G024  梯度爆炸 — 原因和解决方案？                              gpt-Q24
G025  梯度消失 — 原因和解决方案？                              gpt-Q25
G026  Transformer 整体结构？（Encoder + Decoder）             gpt-Q26
G027  Attention 公式 — 能推导 Attention(Q,K,V)               gpt-Q27
G028  Q / K / V 分别是什么？（必问）                           gpt-Q28
G029  为什么除以 √d_k？                                       gpt-Q29
G030  Softmax 在 Attention 中的作用？                         gpt-Q30
G031  Self-Attention 原理？                                  gpt-Q31
G032  Multi-Head Attention 作用？                             gpt-Q32
G033  Position Encoding 是什么？                              gpt-Q33
G034  RoPE 原理？（现在非常高频）                               gpt-Q34
G035  LayerNorm 为什么放在那个位置？（Pre-LN vs Post-LN）      gpt-Q35
G036  残差连接为什么有效？                                     gpt-Q36
G037  Transformer 复杂度 O(n²) — 怎么推导？                   gpt-Q37
G038  FlashAttention 是什么？                                gpt-Q38
G039  KV Cache 是什么？                                      gpt-Q39
G040  长文本怎么解决？                                        gpt-Q40
G041  BERT 与 GPT 区别？（必会）                               gpt-Q41
G042  Encoder-Only 模型特点？                                gpt-Q42
G043  Decoder-Only 模型特点？                                gpt-Q43
G044  MLM（Masked Language Model）是什么？                    gpt-Q44
G045  Next Token Prediction 是什么？                         gpt-Q45
G046  为什么 GPT 适合生成？                                   gpt-Q46
G047  为什么 BERT 适合理解？                                  gpt-Q47
G048  InstructGPT 是什么？                                   gpt-Q48
G049  ChatGPT 训练流程？                                      gpt-Q49
G050  GPT-3 到 GPT-4 的演进？                                 gpt-Q50
G051  SFT（监督微调）是什么？                                  gpt-Q51
G052  全参数微调 vs 参数高效微调？                              gpt-Q52
G053  LoRA 原理？（必问）                                     gpt-Q53
G054  为什么 LoRA 省显存？                                    gpt-Q54
G055  低秩分解是什么？ΔW = A·B                                gpt-Q55
G056  LoRA 训练哪些参数？                                     gpt-Q56
G057  推理时 LoRA 怎么合并？                                  gpt-Q57
G058  QLoRA 是什么？                                         gpt-Q58
G059  为什么 4bit 还能训练？                                  gpt-Q59
G060  AdaLoRA — LoRA 和 AdaLoRA 区别？                       gpt-Q60
G061  Prefix Tuning 是什么？                                 gpt-Q61
G062  Prompt Tuning 是什么？                                 gpt-Q62
G063  P-Tuning 是什么？                                      gpt-Q63
G064  RLHF 流程？（Pretrain→SFT→RM→PPO）                      gpt-Q64
G065  Reward Model 是什么？                                  gpt-Q65
G066  PPO 是什么？                                           gpt-Q66
G067  DPO 是什么？（现在极高频）                                gpt-Q67
G068  DPO 为什么替代 PPO？                                    gpt-Q68
G069  RAG 整体流程？（文档→Chunk→Embedding→VectorDB→检索→LLM）  gpt-Q69
G070  Embedding 是什么？为什么能表达语义？                      gpt-Q70
G071  BGE 是什么？BGE 和 OpenAI Embedding 区别？               gpt-Q71
G072  余弦相似度 — 为什么适合 Embedding？范围是多少？            gpt-Q72
G073  欧氏距离 — 为什么不用欧氏距离？                           gpt-Q73
G074  为什么需要切块（Chunk）？                                gpt-Q74
G075  Chunk 大小怎么选？100/500/1000？                        gpt-Q75
G076  TopK 怎么选？                                          gpt-Q76
G077  向量数据库原理？                                        gpt-Q77
G078  FAISS 原理？                                          gpt-Q78
G079  Chroma 和 FAISS 区别？                                 gpt-Q79
G080  Milvus 和 FAISS 区别？                                 gpt-Q80
G081  Rerank 是什么？（近两年高频）                             gpt-Q81
G082  为什么仅 Embedding 检索不够？                            gpt-Q82
G083  BM25 是什么？                                          gpt-Q83
G084  Hybrid Search（混合检索）是什么？                         gpt-Q84
G085  如何提高 RAG 召回率？                                    gpt-Q85
G086  如何降低 RAG 幻觉？                                      gpt-Q86
G087  如何评估 RAG 效果？（Recall/MRR/NDCG/Hit Rate）           gpt-Q87
G088  Agent 是什么？Agent 和传统 ChatBot 区别？                 gpt-Q88
G089  Agent 和 RAG 区别？                                    gpt-Q89
G090  Tool Calling 原理？（必会）                              gpt-Q90
G091  Function Calling 原理？                                gpt-Q91
G092  Agent 为什么能调用工具？                                 gpt-Q92
G093  ReAct 框架？（Thought→Action→Observation）              gpt-Q93
G094  Agent 为什么会陷入死循环？怎么限制？                      gpt-Q94
G095  Agent Memory 是什么？Checkpointer 原理？                 gpt-Q95
G096  长期记忆和短期记忆区别？                                  gpt-Q96
G097  Agentic RAG 是什么？和传统 RAG 区别？                     gpt-Q97
G098  为什么 Agentic RAG 效果更好？                             gpt-Q98
G099  多轮检索是什么？                                        gpt-Q99
G100  Query Rewrite 是什么？                                 gpt-Q100
G101  Query Expansion 是什么？                               gpt-Q101
G102  Self-RAG 是什么？                                      gpt-Q102
G103  Reflection 是什么？                                    gpt-Q103
G104  Agent 如何判断检索结果不足？                              gpt-Q104
G105  Supervisor 模式是什么？和单 Agent 区别？                  gpt-Q105
G106  为什么要拆多个 Agent？                                  gpt-Q106
G107  多 Agent 协作流程？                                     gpt-Q107
G108  Calendar Agent 案例怎么设计？                           gpt-Q108
G109  Email Agent 案例怎么设计？                              gpt-Q109
G110  Research Agent 案例怎么设计？                           gpt-Q110
G111  多 Agent 有哪些问题？（成本/延迟/上下文同步）              gpt-Q111
G112  MCP 是什么？（Model Context Protocol）                  gpt-Q112
G113  MCP 解决什么问题？                                     gpt-Q113
G114  MCP 和 Tool Calling 区别？                             gpt-Q114
G115  MCP Client 和 Server 是什么？                          gpt-Q115
G116  MCP 为什么被称为"AI 时代 USB 协议"？                     gpt-Q116
G117  MCP 和 LangChain 是什么关系？                           gpt-Q117
G118  System Prompt 是什么？                                 gpt-Q118
G119  Prompt Injection 是什么？如何防范？                     gpt-Q119
G120  Few-Shot Prompt 是什么？                               gpt-Q120
G121  Chain of Thought（CoT）是什么？                         gpt-Q121
G122  Self-Consistency 是什么？                              gpt-Q122
G123  SFT 是什么？                                           gpt-Q123
G124  LoRA 是什么？                                          gpt-Q124
G125  为什么 LoRA 省显存？                                    gpt-Q125
G126  LoRA 训练哪些参数？                                     gpt-Q126
G127  QLoRA 是什么？                                         gpt-Q127
G128  RAG 和 LoRA 什么时候选哪个？（经典应用岗题）               gpt-Q128
G129  LangChain 作用？                                       gpt-Q129
G130  LangGraph 作用？                                       gpt-Q130
G131  LangGraph 和 LangChain 区别？                           gpt-Q131
G132  FastAPI 为什么适合 Agent 服务？                          gpt-Q132
G133  Docker 部署 Agent 注意什么？                             gpt-Q133
G134  如何做会话隔离？thread_id                                gpt-Q134
G135  Redis 在 Agent 系统里的作用？                            gpt-Q135
G136  向量库如何持久化？                                       gpt-Q136
G137  如何监控 Agent 调用链？                                  gpt-Q137
G138  LangSmith 有什么用？                                    gpt-Q138
G139  你做的 RAG 项目架构图是什么？                             gpt-Q139
G140  为什么选 BGE？为什么选 FAISS/Chroma？                    gpt-Q140
G141  Chunk 大小怎么确定？                                    gpt-Q141
G142  检索效果不好怎么优化？                                    gpt-Q142
G143  幻觉怎么解决？                                          gpt-Q143
G144  文档从 100 份增长到 100 万份怎么办？                      gpt-Q144
G145  Agent 调用错误工具怎么办？                               gpt-Q145
G146  如何设计一个企业知识库 Agent？                            gpt-Q146
G147  如何设计一个客服 Agent？                                 gpt-Q147
G148  如何设计一个多 Agent 办公助手？                           gpt-Q148
```

---

## 统计

| 来源 | 题数 |
|------|------|
| 第一层 机器学习 | 13 |
| 第二层 深度学习 | 12 |
| 第三层 Transformer | 15 |
| 第四层 BERT/GPT/LLM | 10 |
| 第五层 模型微调 | 14 |
| 第六层 RLHF | 5 |
| 第七层 RAG | 20 |
| 第八层 Agent | 7 |
| 第九层 Agentic RAG | 9 |
| 第十层 Multi-Agent | 9 |
| 第十一层 MCP | 6 |
| 第十二层 Prompt Engineering | 6 |
| 第十三层 微调（应用岗） | 6 |
| 第十四层 工程化 | 10 |
| 第十五层 项目拷打 | 10 |
| **总计** | **148** |
