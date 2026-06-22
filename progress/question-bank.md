# 晨间复习题库

> **最后更新**：2026-06-09
> 
> 四路汇入：① sessions/ ② Knowledge_base/ ③ share_know/ ④ tracker + code
> 
> **姊妹文件**：`knowledge-index.md` — 百科全书索引，课件+课外知识考点，不混入本库

---

## 🎯 抽题算法（新会话执行）

```
Step 1  从 🟢常规区 筛选"最近7天未问过"的题
Step 2  按标签优先级排序：
          🔬微认知阻塞点 > ⭐核心加固 > 🆕昨日巩固 > 📖远期防忘 > 🔥进度推进
Step 3  抽取：
          维度1 昨日巩固（2-3题）
          维度4 微认知穿透（1-2题）← 至少1题，无则从低分区补
          维度2 远期防忘（3-4题）
          维度3 核心加固（2-3题）← 至少1题
          维度5 进度推进（0-1题）
Step 4  每题间隔一问（stream模式），不批量抛出
Step 5  全部答完后更新"连对"计数 + "最后提问"日期
Step 6  常规区 < 10题时，从 🟡低分区或 knowledge-index.md 精选补充
```

---

## 📊 统计概览

| 指标 | 数值 |
|------|------|
| 总题数 | 96 |
| 🟢 常规区 | 86 |
| 🟡 低频区 | 7 |
| ⚫ 退役区 | 0 |
| 🔬 微认知阻塞点 | 11 |
| ⭐ 核心加固 | 20 |
| 💉 外部注入 | 10 |

| 模块 | 题数 | 说明 |
|------|------|------|
| A. Python 基础 | 9 | 变量作用域/返回值/面向对象/四种参数/访问级别 |
| F. ML/DL 基础 | 27 | 训练循环/PyTorch/Transformer/LoRA/GRPO/Gini/广播/CLIP/R1/ML流程 |
| B. RAG + HuggingFace | 21 | RAG概念/HF生态/显存/IMDB/RAG六站管道/Agentic RAG/Chunk/Embedding/Token/Pipeline |
| C. Agent + LangChain | 31 | Model/Tools/Agent/ReAct/消息流转/Middleware/Supervisor/死循环/LangGraph/Tool设计/MCP |
| D. 微调实战 | 4 | LoRA/QLoRA/DPO/GRPO |
| H. Git + 工具链 | 3 | Git操作/Conda/环境管理 |
| I. 前端基础 | 2 | HTML/CSS/JS架构 |
| 💉 外部注入 | 10 | knowledge-index 5 + questions-gpt 5（晨考随机注入）|
| share_know 课外 | 7 | 蒸馏/温度/开发模式/CLIP/LoRA/DeepSeek-R1/ML流程 |

---

## 🧠 题目列表

### 图例
- 区域：🟢常规 / 🟡低频 / ⚫退役
- 标签：🔬微认知 / ⭐核心加固 / 📖远期防忘 / 🆕昨日巩固 / 🔥进度推进

---

### A. Python 工程化基础

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| A001 | `print()` 和 `return` 的核心区别是什么？ | print=显示屏幕，return=交付值给调用者，函数默认返回None | 🟢 | 1 | 06-03 | session-06-01 | ⭐核心 |
| A002 | 什么是变量作用域？`global` 关键字的作用？ | 局部变量函数内隔离；global在函数内声明使用外部变量 | 🟢 | 1 | 06-03 | session-06-01 | ⭐核心 |
| A003 | `*args` 和 `**kwargs` 分别是什么？混合参数的正确顺序？ | 位置不定长/关键字不定长；顺序：位置→*args→关键字→**kwargs | 🟢 | 0 | 06-04 | session-06-01 | 📖远期 |
| A004 | 四种函数参数形式的顺序是什么？`*` 后面的参数有什么特殊规则？ | 位置→默认→*args→keyword-only；`*`后参数必须用关键字传 | 🟢 | 0 | — | session-06-01 | 📖远期 |
| A005 | `self` 是什么？为什么每个方法第一个参数是它？ | 形参+指针，指向调用对象本身；Python自动传入，不用手动传 | 🟢 | 0 | — | session-03-31 | 📖远期 |
| A006 | `__init__` 和 `__str__` 分别在什么时候触发？ | init=创建对象时自动执行；str=print()时自动触发 | 🟢 | 0 | — | session-05-12 | 📖远期 |
| A007 | 继承中 `super()` 的作用是什么？ | 调用父类方法，避免硬编码父类名，支持多继承MRO链 | 🟢 | 0 | — | session-03-31 | 📖远期 |
| A008 | 面向对象三大特性分别是什么？多态是什么意思？ | 封装/继承/多态；多态=同一方法不同子类不同实现，统一接口不同行为 | 🟢 | 0 | — | session-03-31 | 📖远期 |

---

### F. 机器学习/深度学习基础

#### F-1. 训练循环与PyTorch基础

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| F001 | `nn.Linear(3, 5)` 中 3 和 5 分别是什么？权重矩阵形状？行代表什么？ | 3=输入特征，5=输出神经元；W(5,3)；行=神经元，列=输入特征 | 🟢 | 1 | 06-03 | session-06-03 | 🔬微认知 |
| F002 | PyTorch 的 `nn.Linear` 为什么 W 存 (out, in) 而非 (in, out)？ | 矩阵乘法方向决定：`y=W@x` 要求W第一维=out；教材用 `x@W` 所以存(in,out) | 🟢 | 0 | 06-03 | session-06-03 | 🔬微认知 |
| F003 | 一个神经元本质是什么？`nn.Linear(768, 3072)` 每个神经元有多少权重？ | 一组权重+一个偏置，y=Σ(wx)+b；每个神经元768个权重 | 🟢 | 1 | 06-03 | session-06-03 | ⭐核心 |
| F004 | 训练循环五步口诀是什么？每步对应什么代码？ | "前损后步清"：forward→loss→backward→optimizer.step→zero_grad | 🟢 | 1 | 06-03 | session-06-01 | ⭐核心 |
| F005 | `CrossEntropyLoss` 内部自带什么？输出层应该怎么设计？ | 自带softmax+log+NLLLoss；输出层不加激活，直接出logits | 🟢 | 0 | 06-04 | tracker-漏洞 | 🔬微认知 |
| F006 | `optimizer.zero_grad()` 为什么必要？不写会怎样？ | 梯度默认累加不清零；不写=把多批梯度混在一起，训练崩溃 | 🟢 | 1 | 06-04 | session-06-01 | ⭐核心 |
| F007 | `view` 和 `reshape` 的区别？什么时候用哪个？ | view共享内存要求连续，reshape自动处理非连续；不确定时用reshape | 🟢 | 0 | — | tracker-漏洞 | 🔬微认知 |
| F008 | `dim=-1` 在二维张量和三维张量上分别指什么？ | 最后一维；二维=列方向，三维=最深维度；固定口诀"最后一维"不变 | 🟢 | 0 | — | tracker-漏洞 | 🔬微认知 |

#### F-2. 机器学习基础

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| F010 | `fit_transform()` 和 `transform()` 的核心区别？为什么不能全部 fit_transform？ | fit=学习统计量(均值/方差)，transform=用已学统计量转换；测试集fit会导致数据泄露 | 🟢 | 0 | — | session-05-23 | 🔬微认知 |
| F011 | Recall 和 Precision 分别回答什么问题？分母各是什么？ | Recall="真实对的里面抓到几个"→TP/(TP+FN)；Precision="预测对的里面几个真对"→TP/(TP+FP) | 🟢 | 1 | 06-03 | session-05-12 | ⭐核心 |
| F012 | 分类四指标分别是什么？哪个场景优先 Recall？ | Acc/Recall/Precision/F1；疾病筛查/流失预测优先Recall，垃圾邮件优先Precision | 🟢 | 1 | 06-04 | session-05-12 | ⭐核心 |
| F013 | 梯度下降中，梯度=正数时权重往哪个方向走？为什么？ | 往负方向；梯度=正→斜率为正→减小w才能降loss；梯度=导数=方向 | 🟢 | 0 | — | session-05-14 | ⭐核心 |
| F014 | sklearn ML标准五步模板是什么？ | 导库→加载→切分→标准化→选模型→fit→predict→评估 | 🟢 | 0 | — | session-05-17 | ⭐核心 |
| F015 | `class_weight='balanced'` 解决什么问题？原理是什么？ | 样本不均衡；少数类权重更高，惩罚更大，强制模型关注少数类 | 🟢 | 0 | — | session-05-12 | 📖远期 |

#### F-3. Transformer 与注意力

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| F020 | Transformer 自注意力 Q、K、V 分别是什么含义？ | Q=我要查什么，K=我身上有什么标签，V=我身上有什么有价值的信息 | 🟢 | 0 | 06-03 | session-05-25 | ⭐核心 |
| F021 | 自注意力计算五步流程？公式中为什么除以 `√d_k`？ | QK点积→缩放→softmax→加权V→输出；防止点积结果过大导致softmax梯度消失 | 🟢 | 0 | 06-03 | session-05-25 | ⭐核心 |
| F022 | 残差连接公式？解决什么问题？ | y=F(x)+x；梯度自动+1保底不消失，Transformer堆深全靠它 | 🟢 | 1 | 06-03 | session-05-28 | ⭐核心 |
| F023 | LayerNorm 和 BatchNorm 的核心区别？Transformer 为什么用 LayerNorm？ | LN=单个样本所有特征归一化；BN=批次同一维度归一化；NLP序列长度不一，BN不适用 | 🟢 | 1 | 06-03 | session-04-27 | 📖远期 |
| F024 | Transformer 先残差再加 Norm，还是先 Norm 再加残差？为什么？ | 先残差后Norm(Post-LN)；保证残差加的是原样信息；Pre-LN近年更稳定但Post-LN是原始设计 | 🟢 | 0 | — | session-05-28 | 📖远期 |
| F025 | 自注意力和交叉注意力的区别？Decoder 中各用在哪里？ | 自注意力QKV同源(Decoder自己)，交叉注意力Q来自Decoder、KV来自Encoder | 🟢 | 0 | — | session-05-28 | 📖远期 |

---

### F-4. LoRA / 微调 / GRPO

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| F030 | LoRA 核心公式？A 和 B 怎么初始化？为什么？ | ΔW=B×A；A随机初始化，B全零；B=0→ΔW=0→不破坏原模型，从零开始学 | 🟢 | 1 | 06-03 | session-05-27 | ⭐核心 |
| F031 | LoRA 的 r=8 时能省多少参数？（原 W 4096×4096） | 1600万→6.4万，省256倍。4096×8×2/(4096×4096)=8/4096×2≈1/256 | 🟢 | 0 | 06-04 | session-05-27 | 📖远期 |
| F032 | GRPO 和 PPO 的核心区别？GRPO 的 Advantage 怎么算？ | PPO需Critic模型评估，GRPO不用；Advantage=自己的奖励−同组16条平均奖励 | 🟢 | 0 | 06-03 | session-05-27 | 📖远期 |
| F033 | GRPO 奖励怎么得到？用的是人工标注还是模型打分？ | 规则奖励（数学题对错）+ 格式奖励（格式是否符合要求），不用人工标注 | 🟢 | 0 | — | session-05-27 | 📖远期 |

---

### B. 大模型推理与RAG

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| B001 | RAG 核心流程三步是什么？RAG 和微调的核心区别？ | 检索→增强→生成；RAG改知识(外部文档秒级更新)，微调改能力(训练权重) | 🟢 | 0 | — | session-06-02 | 📖远期 |
| B002 | Harness 是什么？它和 RAG/Agent 的关系？ | 大模型工程缰绳，覆盖推理→API→监控→安全全链路；RAG⊂Harness，Agent⊂Harness | 🟢 | 0 | — | session-06-02 | 📖远期 |
| B003 | 大模型推理显存估算公式？FP16/INT8/INT4 各占几个字节？ | 参数量×字节×1.2；FP16=2B，INT8=1B，INT4=0.5B。7B FP16≈16.8GB | 🟢 | 1 | 06-03 | session-06-01 | ⭐核心 |
| B004 | `DataCollatorWithPadding` 做什么？为什么 tokenizer 里 `padding=False` 后面又补？ | 动态批次填充，每条独立token化→组batch时统一填充到批次最长，不浪费计算 | 🟢 | 0 | — | torch_pre/transform_all | 🔬微认知 |
| B005 | HuggingFace 五大组件是什么？ | Transformers/Datasets/Evaluate/Accelerate/Hub | 🟢 | 0 | 06-04 | session-05-26 | 📖远期 |
| B006 | Tokenizer 四步处理流程？调用后 `return_tensors="pt"` 返回的三个关键字段？ | 标准化→预分词→模型分词→后处理；input_ids/attention_mask/token_type_ids | 🟢 | 0 | — | session-05-26 | 📖远期 |
| B007 | `fp16=True` 和 INT8 量化的区别？训练和推理分别用什么？ | fp16=半精度训练(改权重)，INT8=推理瘦身(不改权重)；训练用fp16，推理可用INT8/INT4 | 🟢 | 0 | — | session-06-01 | 📖远期 |
| B008 | 知识蒸馏的核心概念？软标签 vs 硬标签？温度 T 的作用？ | 老师模型→学生模型；硬标签=one-hot，软标签=概率分布；T>1平滑概率分布，提供更多类间信息 | 🟢 | 0 | — | session-05-26 | 📖远期 |

### B-2. RAG 实战（2026-06-05 新增）

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| B009 | RAG 从原始文档到 LLM 生成答案，完整六站管道是什么？ | 文档加载→文本分块→Embedding向量化→存入向量库→用户提问→检索→拼Prompt→LLM生成 | 🟢 | 0 | — | session-06-05 | 🆕昨日 |
| B010 | LangChain 的 Document 对象包含哪两个核心字段？分别装什么？ | page_content=文本内容(肉)，metadata=身份证(source/page/author) | 🟢 | 0 | — | session-06-05 | 🆕昨日 |
| B011 | 文本分块(Chunking)的两个原因是什么？不分块会有什么后果？ | ①超Embedding token上限被截断 ②粗粒度检索不精准(大海捞针)；chunk_overlap防关键信息被切断 | 🟢 | 0 | — | session-06-05 | ⭐核心 |
| B012 | RecursiveCharacterTextSplitter 的递归分隔符层级顺序是什么？ | \\n\\n(段落)→\\n(行)→。(句)→空格(词)→""(字符硬切)，层层下探直到不超chunk_size | 🟢 | 0 | — | session-06-05 | 🔬微认知 |
| B013 | Embedding 模型三种部署路线是什么？各举一个例子，哪种不联网不花钱？ | ①云端API(智谱/OpenAI)付费联网 ②Ollama本地(bge-m3)免费离线 ③HuggingFace直载(bge-small)最轻量；②③不联网不花钱 | 🟢 | 0 | — | session-06-05 | 🆕昨日 |
| B014 | Chroma 是什么？它和 Embedding 模型的区别？（常混淆） | Chroma=向量数据库(存向量+检索)，Embedding模型=生成向量(文本→数字)；口诀"Chrom存，BGE算" | 🟢 | 0 | — | session-06-05 | 🔬微认知 |
| B015 | 基础 RAG 检索链的代码三步是什么？ | retriever.invoke(q)检索→拼接context→llm.invoke(prompt+context)生成；防幻觉靠Prompt里写"不知道就说不知道" | 🟢 | 0 | — | session-06-05 | ⭐核心 |
| B016 | Agentic RAG 和基础 RAG 的本质区别是什么？ | 基础RAG=每次必查(条件反射)；Agentic RAG=Agent自主判断要不要查(自主决策)；retriever包装为@tool | 🟢 | 0 | — | session-06-05 | 🆕昨日 |

### B-3. RAG 项目进阶路线（2026-06-09 新增 · share_know）

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| B017 | 简历里最值得写的 3 个大模型应用项目是什么？覆盖了哪些技术栈？ | ①ChatPDF企业知识库RAG ②Agentic RAG(LangGraph) ③Multi-Agent智能客服(Supervisor)；覆盖RAG/Agent/Memory/Tool Calling/Multi-Agent | 🟢 | 0 | — | sk-rag项目 | 🆕昨日 |
| B018 | ChatPDF 项目面试能讲哪 5 个核心问题？ | ①为什么切块 ②Chunk Size怎么选 ③为什么用Embedding ④为什么余弦相似度 ⑤如何避免幻觉 | 🟢 | 0 | — | sk-rag项目 | ⭐核心 |

---

### F-5. CLIP / 零样本学习（2026-06-09 新增 · share_know）

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| F035 | 什么叫零样本学习（Zero-Shot）？CLIP 如何实现？ | 没见过该类别的训练样本也能识别；CLIP=双塔架构(图像编码器+文本编码器)→对比学习→图文对齐→用文本描述替代固定标签 | 🟢 | 0 | — | sk-OpenAI CLIP | 🆕昨日 |
| F036 | CLIP 训练 Loss（InfoNCE）的核心思想是什么？ | 双向对比学习：拉近匹配图文对(Pull)，推开不匹配的(Push)；同时计算图像→文本和文本→图像两个方向的损失 | 🟢 | 0 | — | sk-OpenAI CLIP | 🆕昨日 |
| F037 | CLIP 为什么 L2 归一化后点积=余弦相似度？ | 归一化后向量长度为1，a·b=|a||b|cosθ=cosθ，点积直接等于余弦相似度 | 🟢 | 0 | — | sk-OpenAI CLIP | 🆕昨日 |

### F-6. LoRA + DeepSeek-R1（2026-06-09 新增 · share_know）

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| F038 | LoRA 为什么叫"低秩"？rank(ΔW)上限是多少？ | ΔW=B×A，B(4096×r)×A(r×4096)，乘积矩阵秩不超过r；r=8时秩最多8，远小于4096→低秩 | 🟢 | 0 | — | sk-LoRA低秩微调 | 🆕昨日 |
| F039 | LoRA 的 A 和 B 怎么初始化？为什么这样初始化？ | A随机初始化，B全零初始化；B=0→BA=0→初始等价于原模型，不破坏预训练能力，从零开始学习修正 | 🟢 | 0 | — | sk-LoRA低秩微调 | ⭐核心 |
| F040 | DeepSeek-R1 四阶段训练分别是什么？每阶段核心目的？ | ①冷启动SFT→可读性 ②推理RL(GRPO)→推理能力 ③拒绝采样SFT→通用能力平衡 ④全场景RL→最终打磨；核心创新=GRPO不用Critic | 🟢 | 0 | — | sk-DeepSeek-R1 | 🆕昨日 |
| F041 | GRPO 的 Advantage 怎么算？为什么不需要 Critic 模型？ | Advantage=自己奖励−同组16条平均奖励；组内互评即基线，无需额外价值模型，省显存省训练 | 🟢 | 0 | — | sk-DeepSeek-R1 | 🆕昨日 |

---

### C. Agent 智能体开发

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| C001 | LangChain 三大核心模块是什么？ | Model(invoke/stream/batch) + Tools(@tool+文档注释) + Agent(create_agent组装) | 🟢 | 1 | 06-03 | session-06-02 | 🆕昨日 |
| C002 | Model 的三种调用方式及适用场景？ | invoke=一次性等结果；stream=逐token流式输出防等待；batch=批量并行处理 | 🟢 | 0 | 06-03 | session-06-02 | 🆕昨日 |
| C003 | ReAct 循环四步骤？一个用户请求最少几轮模型调用？ | 思考→调工具→观察结果→输出；最少两轮：第一轮决定工具，第二轮消化结果出答案 | 🟢 | 1 | 06-03 | session-06-02 | 🆕昨日 |
| C004 | `@tool` 装饰器和裸函数的区别？`#` 注释和 `"""docstring"""` 哪个 Agent 能读到？ | @tool显式标记为工具+提取签名/文档作工具说明；"""能读到(存在__doc__)，#运行时丢弃 | 🟢 | 1 | 06-03 | session-06-02 | 🆕昨日 |
| C005 | `create_agent()` 三个必传参数是什么？ | model=模型, tools=工具列表, system_prompt=角色设定 | 🟢 | 0 | — | session-06-02 | 🆕昨日 |
| C006 | `init_chat_model` 和 `ChatOpenAI` 的区别？ | init_chat_model=新版统一入口自动解析provider；ChatOpenAI=旧版逐provider指定 | 🟢 | 0 | — | session-06-02 | 🆕昨日 |
| C007 | Agent 和直接调大模型 API 的核心区别是什么？ | Agent=自主决策调工具(ReAct循环)；API=只能生成文本，不会用工具 | 🟢 | 0 | — | session-06-02 | 🆕昨日 |

### C-2. 中间件 Middleware（2026-06-03 新增）

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| C008 | 中间件的洋葱模型是什么意思？before 和 after 的执行顺序？ | before顺序执行(A→B→C)，after逆序执行(C→B→A)；每层在进出两个方向做手脚 | 🟢 | 1 | 06-04 | session-06-03 | 🆕昨日 |
| C009 | Middleware 和 Tool 最本质的区别是什么？谁看得见谁看不见？ | Tool=模型可见，给模型增加能力；Middleware=模型不可见，给开发者增加控制(刹车vs翅膀) | 🟢 | 1 | 06-04 | session-06-03 | ⭐核心 |
| C010 | `wrap_model_call` 和 `before_model` 的区别？动态换模型用哪个？ | before只能看不能换；wrap包裹全过程，能override换模型、缓存、熔断 | 🟢 | 0 | — | session-06-03 | 🔬微认知 |
| C011 | Agent 6 个生命周期钩子分别是什么？ | before_agent→before_model→wrap_model_call→after_model→wrap_tool_call→after_agent | 🟢 | 0 | — | session-06-03 | 🆕昨日 |
| C012 | 10 种内置中间件分哪三类？各举一个例子 | 省钱(Summarization/ContextEditing/LLMToolSelector)；安全(PII/HITL/ModelCallLimit)；容错(ModelFallback/ToolRetry) | 🟢 | 0 | — | session-06-03 | 🆕昨日 |

### C-3. 消息流转与 Superviser

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| C013 | Agent 消息流转四步是什么？AIMessage 的 content 什么时候为空？ | HumanMsg→AIMsg(content="",tool_calls)→ToolMsg(tool_call_id配对)→AIMsg(最终回答)；调工具时content=""=模型在操作工具不说话 | 🟢 | 0 | 06-04 | session-06-03 | 🆕昨日 |
| C014 | `tool_call_id` 为什么必须对应？ | 订单编号配对：多工具同时调用时，防止返回结果串台，Agent 靠 id 知道哪个结果对应哪个调用 | 🟢 | 0 | — | session-06-03 | 🔬微认知 |
| C015 | Supervisor 多 Agent 模式的本质是什么？和单 Agent 多工具的核心区别？ | 本质=拆开注意力不分散；单Agent一次性面对30个工具会选错，Supervisor每个子Agent只看自己3个 | 🟢 | 0 | — | session-06-03 | 🆕昨日 |

### C-4. LangGraph 核心概念（2026-06-08 新增）

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| C016 | LangGraph 的 State 是什么？`class State(TypedDict)` 是数据吗？ | State=数据格式说明书，不是数据本身；真正数据是`{"key":val}`；类比`name:str`→name变量str类型 | 🟢 | 0 | — | session-06-08 | 🔬微认知 |
| C017 | LangGraph 节点(Node)的规则是什么？返回什么？ | 输入State→输出dict；只返回修改的字段，没改的不用返回；什么都没改→return {} | 🟢 | 0 | — | session-06-08 | ⭐核心 |
| C018 | Tool 和 LLM 的本质区别是什么？ | LLM=大脑(思考/分类/生成)；Tool=手脚(执行具体动作)；Tool不知道State存在 | 🟢 | 0 | — | session-06-08 | ⭐核心 |
| C019 | ToolNode 是什么？什么时候不需要它？ | ToolNode=帮Agent执行工具的中间层；手动`llm.invoke()`的Node不需要ToolNode | 🟢 | 0 | — | session-06-08 | ⭐核心 |
| C020 | `MessagesState` 和 `HumanMessage` 的区别？ | MessagesState=聊天框(状态容器)；HumanMessage=用户发的一句话(一条消息) | 🟢 | 0 | — | session-06-08 | 🆕昨日 |

### C-5. Agent 工具函数设计（2026-06-09 新增 · share_know）

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| C021 | LLM 的三大固有缺陷是什么？工具函数分别怎么弥补？ | ①知识截止→搜索工具 ②计算弱→计算器/代码解释器 ③无法交互→API调用/文件读写 | 🟢 | 0 | — | sk-Agent工具函数 | 🆕昨日 |
| C022 | Agent 工具函数和普通 Python 函数的本质区别是什么？ | 调用者是LLM非人类；第一优先级是可被LLM理解；返回值必须是字符串；永远不抛异常 | 🟢 | 0 | — | sk-Agent工具函数 | ⭐核心 |
| C023 | Agent 工具函数三要素是什么？ | ①结构化参数定义(Pydantic) ②自然语言描述(能做什么/何时用/不能做什么) ③健壮实现(不抛异常) | 🟢 | 0 | — | sk-Agent工具函数 | 🆕昨日 |
| C024 | 工具函数"描述是灵魂"，好的描述和坏的描述有什么区别？ | 好：明确何时用+何时不用+"不要自己计算"；坏：只说"这是一个XX工具" | 🟢 | 0 | — | sk-Agent工具函数 | 🔬微认知 |
| C025 | 10 类核心 Agent 工具分别是什么？ | 计算器/代码解释器/网页搜索/文件读写/CSV处理/API调用/知识库检索(RAG)/记忆管理/时间工具 | 🟢 | 0 | — | sk-Agent工具函数 | 🆕昨日 |

### C-6. LangGraph 进阶 + MCP（2026-06-09 新增 · Knowledge_base 模块三）

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| C026 | LangChain 和 LangGraph 的核心区别？（用电脑类比） | LangChain=品牌成品电脑(固定管线)；LangGraph=DIY组装电脑(自由编排节点顺序)；核心公式：LangGraph=节点+边+状态 | 🟢 | 0 | — | kb-模块三LangGraph | ⭐核心 |
| C027 | LangGraph 条件边(Conditional Edge) 的作用是什么？路由函数返回什么？ | 根据当前State判断下一步去哪(岔路口)；路由函数读State返回节点名str(如"tools"或"__end__") | 🟢 | 0 | — | kb-模块三LangGraph | 🆕昨日 |
| C028 | `call_model` 节点 + `tool_node` + 条件边 如何形成 ReAct 循环？ | agent→条件边→(需要工具→tools→agent)形成循环、(不需要→END)；每次循环LLM重新判断 | 🟢 | 0 | — | kb-模块三LangGraph | 🆕昨日 |
| C029 | MCP（Model Context Protocol）是什么？解决什么问题？ | 大模型上下文协议；统一LLM与外部工具/数据源的连接标准；类似"USB-C统一接口"，一次对接所有MCP Server | 🟢 | 0 | — | kb-模块三LangGraph | 🆕昨日 |
| C030 | LangGraph 四步固定步骤是什么？ | ①定义State(TypedDict) ②定义Node(函数) ③构建图(add_node+add_edge) ④编译运行(compile+invoke) | 🟢 | 0 | — | kb-模块三LangGraph | ⭐核心 |
| C031 | AutoGPT 的核心循环顺序是？ | 观察(读state)→拆解(LLM生成任务列表)→执行(act取首任务)；think先看当前state再让LLM出牌，口诀"先看后想再动手" | 🟢 | 1 | 06-11 | session-06-11 | 🆕昨日 |
| C032 | AutoGPT 和 BabyAGI 的核心区别是什么？ | AutoGPT每次回到think由LLM重新生成任务列表；BabyAGI只对已有任务重排顺序(reprioritize) | 🟢 | 1 | 06-11 | session-06-11 | 🆕昨日 |
| C033 | AutoGPT 中 route 判断有剩余任务时返回什么？ | 返回 "think"（字符串），经path_map映射回think节点。口诀"route指向下一站，不是回头看" | 🟢 | 1 | 06-11 | session-06-11 | 🆕昨日 |
| C034 | BabyAGI 的"灵魂"是哪个环节？ | reprioritize：用LLM根据上一步执行结果动态重排剩余任务优先级，而非按初始顺序死执行 | 🟢 | 1 | 06-11 | session-06-11 | 🆕昨日 |
| C035 | BabyAGI 执行完一个任务后下一步做什么？ | 先由LLM重排剩余任务的优先级，再继续执行下一个任务 | 🟢 | 1 | 06-11 | session-06-11 | 🆕昨日 |
| C036 | AutoGPT act 节点执行完任务后对任务列表做了什么？ | 移除已执行的任务(tasks[1:])，并记录执行结果到result字段 | 🟢 | 1 | 06-11 | session-06-11 | 🆕昨日 |
| C037 | AutoGPT 和 BabyAGI 的循环结构，以下正确的有？[多选] | ABC：A.think→act→think循环 B.execute_next→reprioritize→execute_next循环 C.AutoGPT每次可增删改任务列表 | 🟢 | 1 | 06-11 | session-06-11 | 🆕昨日 |
| C038 | AutoGPT think 节点可能做哪些事？[多选] | ABD：A.根据目标初次拆解任务 B.根据执行结果调整剩余任务 D.必要时新增或删除任务；C(执行任务)是act节点的工作 | 🟢 | 1 | 06-11 | session-06-11 | 🆕昨日 |
| C039 | BabyAGI reprioritize 排序规则是写死在代码里的？[判断] | 错。每次由LLM根据执行结果动态重排，非硬编码规则 | 🟢 | 1 | 06-11 | session-06-11 | 🆕昨日 |
| C040 | AutoGPT think 每次从零重新生成任务列表？[判断] | 错。初次从零生成，再次根据上次执行结果(result)动态调整，可能增删改重排 | 🟢 | 1 | 06-11 | session-06-11 | 🆕昨日 |
| C041 | AutoGPT/BabyAGI 循环终止条件都是任务队列为空？[判断] | 对。两者都通过route判断tasks是否为空，为空→END | 🟢 | 1 | 06-11 | session-06-11 | 🆕昨日 |
| C042 | AutoGPT act 节点移除的是任务列表第几个任务？ | 第1个（tasks[0]），取tasks[1:]作为剩余任务列表 | 🟢 | 1 | 06-11 | session-06-11 | 🆕昨日 |
| C043 | think 节点"初次拆解"和"再次拆解"行为有什么不同？ | 初次：result为空→LLM从零拆解目标生成初始任务列表；再次：result有上次执行内容→LLM根据结果动态调整(增删改重排)而非推倒重来 | 🟢 | 1 | 06-11 | session-06-11 | 🆕昨日 |
| C044 | BabyAGI 为什么用LLM动态重排而非按初始顺序执行？ | 初始顺序基于不完整信息拍脑袋排的；每步执行后获得新信息(某路不通/某事变紧急)，需LLM用最新信息重新校准优先级。口诀"计划是死的，执行结果是活的，每走一步重新看牌" | 🟢 | 1 | 06-11 | session-06-11 | 🆕昨日 |
| C045 | MessagesState 中 messages 为什么必须是列表？覆盖和追加模式怎么区分？ | 聊天记录是多条消息按顺序存起来→list天然有序；`messages: list`=覆盖(黑板擦旧写新)；`Annotated[list, add_messages]`=追加(日记本写新页)；MessagesState默认追加模式 | 🟢 | 0 | — | kb-模块三LangGraph与MCP | 🆕昨日 |
| C046 | `Annotated[list, add_messages]` 中 `add_messages` 是什么？不写会怎样？ | add_messages是LangGraph内置规约器(Reducer)，将新消息追加到已有列表末尾而非替换；不写=普通list=覆盖模式，新消息冲掉旧消息，多轮对话历史丢失 | 🟢 | 0 | — | kb-模块三LangGraph与MCP | 🆕昨日 |
| C047 | 节点 return 时为什么要把单条消息包成 `[res]` 而不是直接返回 `res`？ | messages字段始终是列表类型，return时新消息也必须装在列表中；`{"messages": res}`报错，`{"messages": [res]}`正确。类比：快递站只收整箱，单个包裹也得装箱 | 🟢 | 0 | — | kb-模块三LangGraph与MCP | 🆕昨日 |
| C048 | LangGraph 中 Fan-out 和 Fan-in 分别指什么？代码怎么写？ | Fan-out=一个节点指向多个节点(并行分发)：`add_edge(A,B)+add_edge(A,C)`；Fan-in=多个节点指向同一个节点(汇聚等待)：`add_edge(B,D)+add_edge(C,D)`，D等B和C都完成才执行 | 🟢 | 0 | — | kb-模块三LangGraph与MCP | 🆕昨日 |
| C049 | 层级主管(Hierarchical)模式的核心流程是什么？ | 主管拆任务→Fan-out并行分发给多个专家→各专家独立执行→Fan-in汇聚到主管→主管汇总输出。口诀"分而治之：主管管分配+汇总，专家管执行" | 🟢 | 0 | — | kb-模块三LangGraph与MCP | 🆕昨日 |
| C050 | 协作辩论(Collaborative)模式和层级主管模式的核心区别？ | 主管=一人分派多人干活(分工)；辩论=多人从不同立场给观点(集思广益)。辩论结构：正方+反方+中立三方并行→裁决者综合判断。主管是"分工"，辩论是"碰撞" | 🟢 | 0 | — | kb-模块三LangGraph与MCP | 🆕昨日 |
| C051 | 条件边如何实现循环？route 函数返回什么？ | route返回前面节点的名字(如"take_exam")，图就跳回去重新执行那个节点。这是普通边做不到的——条件边=循环+分流两能力合一 | 🟢 | 0 | — | kb-模块三LangGraph与MCP | 🆕昨日 |
| C052 | MCP 的 C/S 架构中，Server 和 Client 分别负责什么？ | Server=定义工具(等人调用)，用`@mcp.tool()`注册函数；Client=主动发起请求，发现工具→调用工具→获取结果。类比：Server是餐厅后厨(备菜等单)，Client是服务员(接单催菜) | 🟢 | 0 | — | kb-模块三LangGraph与MCP | 🆕昨日 |
| C053 | MCP 三种传输模式（stdio/SSE/Streamable HTTP）的区别？ | stdio=本地子进程通信(客户端自动拉起服务端，最常用)；SSE=HTTP单向推送(需手动启动Server)；Streamable HTTP=HTTP双工流(实时双向)。上层API(ClientSession)完全一致，只改transport参数切换 | 🟢 | 0 | — | kb-模块三LangGraph与MCP | 🆕昨日 |
| C054 | MCP 调用工具的完整三步流程是什么？ | ①初始化连接(建立ClientSession) ②发现工具(list_tools获取Server注册的工具列表) ③调用工具(call_tool传入工具名+参数获取结果) | 🟢 | 0 | — | kb-模块三LangGraph与MCP | 🆕昨日 |
| C055 | FastMCP 是什么？`@mcp.tool()` 装饰器的作用？ | FastMCP是mcp库提供的高阶封装，简化MCP Server编写，底层自动处理JSON-RPC协议细节；`@mcp.tool()`把普通Python函数注册为MCP工具，Agent可通过MCP协议发现并调用 | 🟢 | 0 | — | kb-模块三LangGraph与MCP | 🆕昨日 |
| C056 | interrupt() / MemorySaver / thread_id 三者的关系是什么？ | interrupt()=暂停点(挂起等唤醒)；MemorySaver=检查点(保存暂停时的状态+位置，必须配)；thread_id=会话ID(区分不同对话互不干扰)。三位一体：MemorySaver存状态+thread_id区分会话+interrupt暂停点=可恢复的工作流 | 🟢 | 0 | — | kb-模块三LangGraph与MCP | 🆕昨日 |
| C057 | LangGraph 多 Agent 三种模式（流水线/主管/辩论）各适用于什么场景？ | Sequential=有明确先后顺序(流水线)；Hierarchical=需任务分解+专家分工(主管分配)；Collaborative=需多角度评审决策(辩论碰撞)。选型口诀"顺序明确走流水，分工协作找主管，观点碰撞上辩论" | 🟢 | 0 | — | kb-模块三LangGraph与MCP | 🆕昨日 |
| C058 | Human-in-the-Loop 的核心原则是什么？什么时候该加 interrupt？ | 机器能决定的事让它做，需要人决策的地方必须interrupt。典型场景：AI生成代码→等你点Apply；AI要执行危险命令→等你授权。原则：可控的自动化，非完全自动 | 🟢 | 0 | — | kb-模块三LangGraph与MCP | 🆕昨日 |
| C059 | MCP 的核心价值是什么？"传输与协议分离"是什么意思？ | 不管底层用什么传输方式(stdio/SSE/HTTP)，上层调用代码(ClientSession)完全一致。类比USB-C统一充电接口——换传输方式只需改一行transport参数，业务代码不动 | 🟢 | 0 | — | kb-模块三LangGraph与MCP | 🆕昨日 |
| C060 | MessagesState 可以用自己定义的类替代吗？本质是什么？ | 可以。MessagesState本质就是TypedDict，只定义了一个字段`messages: Annotated[list, add_messages]`；完全可以自己写一个同样结构的类替代它，LangGraph不强制用MessagesState | 🟢 | 0 | — | kb-模块三LangGraph与MCP | 🆕昨日 |

---

### H. Git 与工具链

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| H001 | `git add` / `commit` / `push` 的区别？ | add=暂存区，commit=本地仓库快照，push=推到远程 | 🟡 | 3 | 06-03 | session-04-25 | 📖远期 |
| H002 | conda / pip / venv 三个环境管理工具的区别？ | conda=跨语言包+环境二合一，pip=纯Python包，venv=轻量隔离仅Python | 🟢 | 0 | — | session-05-30 | 📖远期 |
| H003 | `json.dumps` / `json.loads` / `json.dump` / `json.load` 两对四兄弟的区分？ | 带s=字符串操作(dumps→json字符串, loads←json字符串)；不带s=文件操作 | 🟢 | 0 | — | session-04-01 | 📖远期 |

---

### I. 前端开发基础

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| I001 | 前后端分离架构中，HTML/CSS/JS 各自负责什么层？ | HTML=内容结构(有什么)，CSS=样式(长什么样)，JS=交互行为(做什么) | 🟡 | 3 | 06-03 | session-04-21 | 📖远期 |
| I002 | CSS 三种使用方式？id 选择器和 class 选择器的语法和区别？ | style标签/style属性/link导入；#id(唯一不重复)，.class(可重复多标签共用) | 🟡 | 3 | 06-03 | session-04-21 | 📖远期 |

---

### S. share_know 课外知识

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| S001 | 主流软件开发模式有哪些？瀑布模型和敏捷开发的核心区别？ | 瀑布=需求→设计→开发→测试→上线(线性串行)；敏捷=迭代增量+持续反馈(Scrum/看板) | 🟡 | 3 | 06-03 | share-know-主流开发模式 | 📖远期 |
| S002 | 大模型蒸馏的核心思想？温度 T 为什么能传递暗知识？ | 老师输出概率→学生模仿；T>1拉平分布，让学生看到"第二候选"的相似度信息 | 🟢 | 0 | — | share-know-蒸馏 | 📖远期 |
| S003 | 大模型温度参数 `temperature` 的作用？T=0 和 T=1 有什么区别？ | 控制随机程度；T→0=确定性输出(贪心)，T=1=原始分布，T>1=更随机更发散 | 🟢 | 0 | — | share-know-温度 | 📖远期 |
| S004 | 传统 ML 和深度学习在流程上最大的区别是什么？ | ML=人工特征工程最耗时(从日期提取"是否周末")；DL=弱化人工特征，让网络自己学特征，海量数据驱动 | 🟢 | 0 | — | sk-机器学习深度学习流程 | 🆕昨日 |
| S005 | CNN 的核心流程是什么？池化层(Pooling)的作用？ | 卷积(提取局部特征)→激活(ReLU)→池化(降维+防过拟合)→展平→全连接→输出；池化=保留最重要特征+减少计算量 | 🟢 | 0 | — | sk-机器学习深度学习流程 | 🆕昨日 |
| S006 | LSTM 的三个门分别做什么？和 RNN 的根本区别在哪？ | 遗忘门(丢弃旧信息)+输入门(添加新信息)+输出门(输出当前隐藏状态)；多了Cell State长期记忆通道，解决RNN梯度消失 | 🟢 | 0 | — | sk-机器学习深度学习流程 | ⭐核心 |

---

### J. 外部注入题库（晨考随机注入，与 Bank 统一生命周期）

> 2026-06-06 首发注入，knowledge-index 5 + questions-gpt 5，完全随机抽取不限模块。

#### J-1. knowledge-index 注入

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| J001 | Python 类的三种访问级别分别是什么？语法怎么写？ | public(self.x)/protected(self._x约定)/private(self.__x名字改写_类名__x) | 🟢 | 0 | 06-06 | kb-07面向对象 | 💉注入 |
| J002 | NumPy 广播和向量化的区别？ | 向量化=批量运算(C层一次算完)；广播=形状不同时自动对齐(3,4)+(4,)→(3,4) | 🟢 | 0 | 06-06 | kb-09Pandas | 💉注入 |
| J003 | 决策树 Gini 和 Entropy 有什么区别？sklearn 默认用哪个？ | Gini计算快不涉及对数→树浅；Entropy信息论更精准→树深；sklearn默认Gini(CART) | 🟢 | 0 | 06-06 | kb-31机器学习三 | 💉注入 |
| J004 | HuggingFace Pipeline 支持哪些 NLP 任务？至少说 5 个 | 情感分析/文本分类/生成/QA/NER/翻译/摘要/零样本；口诀"情分生翻摘问答" | 🟢 | 0 | 06-06 | kb-42Transformer二 | 💉注入 |
| J005 | 基础 RNN 的致命缺陷是什么？LSTM 如何解决的？ | BPTT梯度消失→长程遗忘(0.8^100≈0)；LSTM用Cell State+三门提供稳定梯度传播路径 | 🟢 | 1 | 06-06 | kb-40RNN | 💉注入 |

#### J-2. questions-gpt 注入

| ID | 题目 | 答案要点 | 区域 | 连对 | 最后提问 | 来源 | 标签 |
|----|------|---------|------|------|---------|------|------|
| J006 | 什么是 Token？中文和英文 Token 一样吗？1000 Token 约多少汉字？ | LLM最小处理单元；中英文token不一样(中文1-2字/token)；1000Token≈600-800汉字 | 🟢 | 1 | 06-06 | gpt-Q1 | 💉注入 |
| J007 | Chroma 和 FAISS 有什么区别？ | Chroma存磁盘持久化适合中小；FAISS纯内存极致速度(Meta)适合百万级向量 | 🟢 | 0 | 06-06 | gpt-Q19 | 💉注入 |
| J008 | Agent 为什么会陷入死循环？怎么限制？ | 调工具→不满意→再调→循环；ModelCallLimitMiddleware限制最大调用轮数 | 🟢 | 0 | 06-06 | gpt-Q35 | 💉注入 |
| J009 | Embedding 是什么？为什么它能表达语义？ | 文本→数字向量；语义相近→向量空间靠得近→cos相似度高；国王-男+女≈女王 | 🟢 | 1 | 06-06 | gpt-Q2 | 💉注入 |
| J010 | RAG 中 Chunk 大小怎么确定？太大或太小各有什么问题？ | 黄金经验~512；太小=信息碎片化上下文不完整；太大=噪音多检索不精准+超token上限 | 🟢 | 1 | 06-06 | gpt-Q87 | 💉注入 |

---

## 🔬 微认知阻塞点专项

> 这些题体量极小但理解成本极高，未贯通时阻塞下游大片模块。出题时追问「为什么」而非仅验证「是什么」。

| ID | 微认知点 | 一句话描述 | 未贯通后果 | 首次暴露 |
|----|---------|-----------|-----------|---------|
| F001 | nn.Linear 行列方向 | 权重矩阵行=神经元还是列=神经元？ | Transformer 源码所有投影层无法阅读 | 06-03 |
| F002 | PyTorch W 存 (out,in) 原因 | 矩阵乘法 `W@x` vs `x@W` 决定存储方向 | 看不懂任何模型的 weight.shape | 06-03 |
| F005 | CrossEntropyLoss 内置 softmax | 输出层不能加 softmax，loss 内部已处理 | 训练不收敛或 NaN，排查半天不知原因 | 待暴露 |
| F007 | view vs reshape | view 共享内存要求连续，reshape 自动处理 | 梯度断链、反向传播报错，找不到原因 | 待暴露 |
| F008 | dim=-1 在不同维度下的行为 | 最后一维永远是最后一维，但二维/三维上具体操作不同 | 所有 tensor 操作写法靠猜 | 待暴露 |
| F010 | fit_transform vs transform | 数据泄露的根源：测试集不能 fit | 模型评估虚高，上线后效果暴跌 | 05-23 |
| B004 | DataCollatorWithPadding 存在理由 | padding=False 后面又补，为什么绕一圈？ | 看不懂 HuggingFace Trainer 数据处理链路 | 待暴露 |
| C016 | State=数据格式说明书 vs 数据 | `class State(TypedDict)` 不是数据本身，只是结构说明 | LangGraph/Agent 所有代码无法独立写出 | 06-08 |

---

## 📝 生命周期操作日志

| 日期 | 操作 | 题目ID | 变更说明 |
|------|------|--------|---------|
| 2026-06-03 | 创建 | — | 题库初始化，首批50题，覆盖A/F/B/C/H/I/S七模块 |
| 2026-06-03 | 新增 | C008-C015 | 中间件(5题) + 消息流转(2题) + Supervisor(1题)，C模块7→15题 |
| 2026-06-03 | 标记微认知 | C010/C014 | wrap_model_call vs before_model + tool_call_id配对 |
| 2026-06-04 | 晨间提问 | 9题 | C008/C009/F006/F012 连对+1，A003/B005/F005/F031/C013 需加固，最后提问日期全更新 |
| 2026-06-05 | 新增 | B009-B016 | RAG实战8题（六站管道/Document/分块/Embedding三路线/Chroma/检索链/Agentic RAG） |
| 2026-06-05 | 晨间提问 | 9题 | RAG概念/分块/完整链路/递归分隔符/参数顺序/HF五件套/LoRA/thread_id/Embedding路线 |
| 2026-06-05 | 标记微认知 | B012/B014 | 递归分隔符层级 + Chroma≠Embedding混淆点 |
| 2026-06-06 | 晨间双层考试 | 20题（Bank 10 + 注入 10） | 首发双层机制；Bank层10题（6✅/2⚠️/2❌），注入层10题（5✅/1⚠️/4❌） |
| 2026-06-06 | 新增 | J001-J010 | 外部注入10题首发入库（kb-5题 + gpt-5题），来源标记 💉注入 |
| 2026-06-06 | CLUADE.md | — | 题库架构v2.0：双层晨考（Bank 8-10 + 随机注入各5），注入不限模块，错题入session |
| 2026-06-08 | 新增 | C016-C020 | LangGraph五题：State本质/TypedDict说明书/Node规则/Tool≠LLM/ToolNode/MessagesState |
| 2026-06-08 | 标记微认知 | C016 | State=数据格式说明书 vs 数据本身，学员原话类比贯通 |
| 2026-06-09 | 新增 | C021-C030 | Agent工具函数(5题) + LangGraph进阶/MCP(5题)，来源：share_know+Knowledge_base模块三 |
| 2026-06-09 | 新增 | B017-B018 | RAG项目路线(2题)，来源：share_know/rag项目.md |
| 2026-06-09 | 新增 | F035-F041 | CLIP零样本(3题) + LoRA/R1(4题)，来源：share_know |
| 2026-06-09 | 新增 | S004-S006 | ML→DL→Transformer流程(3题)，来源：share_know |
| 2026-06-09 | 标记微认知 | C024 | 工具描述是灵魂 — 好描述vs坏描述的根本差异 |
| 2026-06-11 | 新增 | C031-C044 | AutoGPT/BabyAGI 课件测验14题入库（选择题/多选/判断/填空/简答全覆盖） |
| 2026-06-11 | 新增 | C045-C060 | 模块三HTML课件提取16题：MessagesState机制/Fan-out-Fan-in/多Agent模式/MCP传输与协议 |
