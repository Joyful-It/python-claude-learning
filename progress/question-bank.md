# 晨间复习题库

> **最后更新**：2026-06-08
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
| 总题数 | 81 |
| 🟢 常规区 | 71 |
| 🟡 低频区 | 7 |
| ⚫ 退役区 | 0 |
| 🔬 微认知阻塞点 | 10 |
| ⭐ 核心加固 | 18 |
| 💉 外部注入 | 10 |

| 模块 | 题数 | 说明 |
|------|------|------|
| A. Python 基础 | 9 | 变量作用域/返回值/面向对象/四种参数/访问级别 |
| F. ML/DL 基础 | 21 | 训练循环/PyTorch/Transformer/LoRA/GRPO/Gini/广播 |
| B. RAG + HuggingFace | 21 | RAG概念/HF生态/显存/IMDB/RAG六站管道/Agentic RAG/Chunk/Embedding/Token/Pipeline |
| C. Agent + LangChain | 21 | Model/Tools/Agent/ReAct/消息流转/Middleware/Supervisor/死循环/LangGraph |
| D. 微调实战 | 4 | LoRA/QLoRA/DPO/GRPO |
| H. Git + 工具链 | 3 | Git操作/Conda/环境管理 |
| I. 前端基础 | 2 | HTML/CSS/JS架构 |
| 💉 外部注入 | 10 | knowledge-index 5 + questions-gpt 5（晨考随机注入）|
| share_know 课外 | 1 | 蒸馏/温度/开发模式/CLIP |

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
