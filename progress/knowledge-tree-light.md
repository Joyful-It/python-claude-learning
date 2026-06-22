# 知识树轻量索引（Knowledge Tree Light）

> 新会话只读此文件（~200行）定位树结构+题号，按需去完整版取题干
> 完整版：`knowledge-tree.md`（1243行，含重要度/Teach-Agent等级/题源/描述）

---

## ① Agent 智能体开发

### 1.1 Prompt
- System Prompt → G118
- Prompt Injection → G119

### 1.2 Tool Calling
- Function Calling → G090 G091 G092
- Tool定义三要素 → C004 C021 C022 C023 C024 C025
- Tool vs Agent vs LLM → C007 C018
- LangChain三大核心 → C001 C002 C005 C006

### 1.3 ReAct
- ReAct框架 → G093 C003 C013
- Reflection → G103
- AutoGPT/BabyAGI循环 → C031 C032 C033 C034 C035 C036 C037 C038 C039 C040 C041 C042 C043 C044
- 死循环防护 → G094 J008

### 1.4 Memory
- 短期vs长期记忆 → G095 G096
- Checkpointer/thread_id → G134 C056

### 1.5 LangGraph
- State/TypedDict/MessagesState → C016 C020 C045 C046 C060
- Node返回规则 → C017 C019 C047
- Edge/ConditionalEdge → C027 C028 C051
- Fan-out/Fan-in → C048 C049
- LangGraph四步搭建 + 与LangChain区分 → C026 C030 G129 G130 G131
- HITL人工介入 → C056 C058
- Middleware → C008 C009 C010 C011 C012

### 1.6 Multi-Agent
- Supervisor模式 → G105 C015 C049
- 三模式(Sequential/Hierarchical/Collaborative) → C050 C057 G107
- 多Agent vs 单Agent+多工具 → G106
- 案例设计 → G108 G109 G110 G147 G148
- 多Agent问题 → G111

### 1.7 MCP
- MCP概念/架构 → G112 G113 G116 C029
- Client/Server → G115 C052 C054
- MCP vs Tool Calling → G114
- MCP与LangChain → G117
- 传输模式 → C053 C055 C059

### 1.8 Agent评估
- 死循环/ModelCallLimit → J008
- LangSmith/监控 → G137 G138
- 错误处理 → G145

---

## ② RAG

### 2.1 RAG基础
- RAG核心概念 → B001 G069
- RAG vs 微调 → G128
- 六站管道 → B009 B015 B018
- Harness → B002
- HF五大组件 → B005

### 2.2 文档处理
- Document对象 → B010
- 分块/RecursiveCharSplit → B011 B012
- Chunk大小 → G074 G075 G141 J010
- DataCollator → B004

### 2.3 Embedding
- Embedding原理 → G070 J009
- 模型选择(BGE/OpenAI) → G071 G140 B013
- 余弦相似度vs欧氏距离 → G072 G073

### 2.4 向量库
- 向量库原理 → G077
- Chroma → B014
- FAISS → G078
- Milvus → G080
- 对比选型 → G079 G080 J007
- 持久化 → G136

### 2.5 检索
- TopK → G076
- BM25/混合检索 → G083 G084
- Rerank → G081 G082

### 2.6 生成与防幻觉
- Prompt拼接 → B015
- 幻觉/防幻觉 → G086 G143 K147 K148 K149

### 2.7 RAG优化
- Query Rewrite/Expansion → G100 G101
- 评估指标 → G087
- 召回率/规模扩展 → G085 G142 G144

### 2.8 Agentic RAG
- Agentic RAG vs 传统RAG → B016 B017 G097 G098
- Self-RAG/Reflection/多轮检索 → G099 G102 G103 G104
- 项目设计 → G139 G146 B017 B018

---

## ③ Python工程

### 3.1 基础语法
- 解释型/变量/type → K001 K004 K006 A001 A002
- 分支循环/逻辑运算符 → K005 K008 K009 K010 K011 K012
- 字符串/切片/strip → K013 K015 K048 K050
- 列表/元组/集合/字典/列表推导式 → K014 K016 K017 K018 K053 K054
- 格式化/命名/正则 → K007 K019 K049 K055 K056
- 文件/导入/包标志 → K024 K030 K057
- 环境管理 → K002 K003 K088 H002

### 3.2 函数
- 四种参数类型/顺序 → K020 K052 A003 A004
- lambda → K021
- return vs print/作用域/递归 → K022 K023 A001 A002

### 3.3 OOP
- 类/对象/__init__/self → A005 A006
- 继承/super/MRO → K026 A007
- 封装(三种访问级别) → K025 J001
- 多态(重写+鸭子类型) → K027 A008
- __str__/三大特性 → K028 A008

### 3.4 异常处理
- try-except-else-finally → K029

### 3.5 NumPy/Pandas/可视化
- NumPy数组属性/reshape/dot/逆矩阵 → K035 K037 K038 K039
- 广播vs向量化 → K036 J002
- Pandas(Series/DataFrame/loc/iloc/describe) → K040 K041 K042 K043
- 数据清洗 → K047 F010
- Matplotlib/Seaborn → K044 K045 K046

### 3.6 JSON/API
- JSON操作(dumps/loads) → K031 K032 H003
- 大模型API调用 → K033 K034

### 3.7 FastAPI
- 路由/参数(Path/Query/Body) → K066 K067 K068
- Pydantic/Depends → K069 K070
- async/UploadFile → K071 K072
- FastAPI适合Agent → G132

### 3.8 工程化
- Git → H001 K058 K059
- Docker → G133
- Redis → G135
- 项目结构/VibeCoding/JupyterLab → K057 K078 K125

---

## ④ LLM基础（精选）

### 4.1 神经网络基础
- 神经元/万能近似 → F003 G014
- 激活函数(ReLU/GELU/Sigmoid) → G017 G018 K105
- 反向传播/链式法则 → G015 G016
- 训练循环五步 → F004 F006 K099 K102
- ML类型/六步流程/模型家族 → K079 K081 F014
- 过拟合/正则化(L1/L2/Dropout) → G001 G002 G021 K080 K086
- Tensor/NumPy/requires_grad → K097 K098 F001 F002 F007 F008
- 图像4D/自定义网络/train vs eval → K100 K101 K103
- CNN/RNN/LSTM/GRU → K104 K106 K107 K108 K109 S005 S006 J005

### 4.2 损失函数与优化器
- 交叉熵(内置三件套) → F005 G003 K085
- Softmax(eˣ→求和→÷) → G004 F021
- 梯度下降(SGD/Adam/AdamW) → G005 G006 F013
- 梯度消失/爆炸 → G024 G025
- class_weight → F015
- BatchNorm/LayerNorm/Dropout → G019 G020 G021
- 权重初始化(Xavier/Kaiming) → G022 G023
- 决策树(Gini/Entropy) → K089 K090 K091 J003

### 4.3 Transformer核心
- 整体架构(Encoder+Decoder) → G026
- Self-Attention五步 → G031 F021
- Q/K/V角色 → G028 F020 K112
- Attention公式(√dₖ/softmax) → G027 G029 G030 K113
- Multi-Head → G032 K114
- FFN结构 → G036 K116
- 残差连接 → F022 K117
- 复杂度O(n²)/对RNN优势 → G037 K111

### 4.4 位置编码
- 为什么需要 → G033 K115
- Sinusoidal/RoPE → G034

### 4.5 归一化
- LayerNorm vs BatchNorm → G020 F023
- Pre-LN vs Post-LN → G035 F024 F025 K117

### 4.6 GPT/BERT
- Encoder/Decoder/Encoder-Only/Decoder-Only → G041 G042 G043
- BERT(MLM) → G044 G047
- GPT(Next Token) → G045 G046
- GPT演进/InstructGPT/ChatGPT → G048 G049 G050
- CLIP(双塔/对比学习) → F035 F036 F037 K141 K142 K143
- Scaling Law/幻觉根源 → K147
- HF三大核心/Pipeline → K118 K119 J004

### 4.7 分词
- Tokenizer四步 → B006 K122
- 中文分词/Token概念 → K110 J006

### 4.8 Prompt Engineering
- 五种提示词技术 → K123 G120 G121 G122
- Context Engineering/temperature → K124 S003
- 幻觉场景 → K149

### 4.9 推理优化
- KV Cache → G039
- FlashAttention → G038
- 长文本 → G040

### 4.10 评估指标
- 分类四指标(Acc/Recall/Precision/F1) → F011 F012 G007 G008
- ROC/AUC/回归评估 → G007 K082 K083 K084

---

## ⑤ 微调与部署

### 5.1 SFT
- SFT/InstructGPT/ChatGPT训练 → G048 G049 G051 G123
- 全参vs高效(PEFT) → G052
- RAG vs LoRA选型 → G128
- BERT微调实践 → K120 K121

### 5.2 LoRA/QLoRA
- LoRA原理(ΔW=B×A/省256倍) → G053 G054 G055 G124 G125 F030 F031 F038 F039 K138 K139 K140
- 训练参数/推理合并 → G056 G057 G126
- QLoRA(4bit微调) → G058 G059 G127
- AdaLoRA/Prefix/Prompt/P-Tuning → G060 G061 G062 G063

### 5.3 RLHF/DPO
- RLHF流程 → G064 G065 G066
- DPO(替代PPO) → G067 G068
- GRPO/DeepSeekR1/拒绝采样 → K135 K136 K137 F032 F033 F040 F041

### 5.4 蒸馏与量化
- 蒸馏(T→S/软标签/温度T) → K150 K151 B008 S002
- 蒸馏vs量化 → K152
- 量化(FP16/INT8/INT4) → G059 B003 B007

### 5.5 推理部署
- 显存评估 → B003
- vLLM/Ollama → (待补)

### 5.6 传统ML补充
- SVM/朴素贝叶斯/KNN → K092 K093 K094 K095 K096
- 逻辑/多项式/线性回归 → K084 K087
- 数据泄露(fit_transform) → F010
- 传统ML vs DL → S004

---

## ⑥ 计算机基础

### 6.1 数据库
- MySQL(约束/JOIN/模糊查询/EXPLAIN) → K060 K061 K062 K065
- SQLAlchemy(CRUD) → K063 K064
- Redis → G135

### 6.2 前端
- HTML/CSS/JS基础 → K073 K074 K075 K076 K077 I001 I002

### 6.3 软件工程
- Git工作流 → H001 K058 K059
- 迭代/敏捷/螺旋 → K144 K145 K146 S001
- VibeCoding → K078 K057

### 6.4 数学
- 概率论(贝叶斯/高斯/频率vs贝叶斯) → G012 G013 K130 K131 K132 K133 K134
- 信息论(熵/KL/JS) → G009 G010 G011

### 6.5 环境与工具
- 包管理器/Miniconda → K002 K088 H002
- JupyterLab → K125

---

## 面试项目题

### ChatPDF(RAG知识库)
→ G139 G140 G141 G142 G143 G144 B017 B018

### teach-agent(智能家教)
→ G145 G146 G147 G148

### 多Agent协作
→ G108 G109 G110 G107

---

> 总行数：~200行（vs 完整版1243行，省~85%）
> 使用方法：新会话先读此文件确定树位置 → 按题号去原文件取题干
