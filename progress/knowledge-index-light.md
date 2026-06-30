# 注入池A 轻量索引（knowledge-index → 晨考随机抽5题）

> 选号后去 `knowledge-index.md` grep 对应 ID 取答案正文
> 姊妹文件：`question-index.md`（Bank核心题库）、`questions-gpt-light.md`（注入池B）

---

## 抽题规则
- 每次晨考从本索引**完全随机**抽取 5 题（不限模块）
- 已在 `question-bank.md` 中的跳过（去重）
- 答完后入库 `question-bank.md`，来源标 `kb-{文件名}`
- 题目退役后从 `knowledge-index.md` 原料库补新题

---

## 索引

```
ID    问题                                               来源文件
─────────────────────────────────────────────────────────────────────────────
K001  Python 是什么类型的语言？                            kb-01环境搭建
K002  三大包管理器？                                       kb-01环境搭建
K003  如何验证Python安装？                                  kb-01环境搭建
K004  type() 的作用？核心数据类型？                          kb-02基础语法
K005  三个逻辑运算符的真值规则？                             kb-02基础语法
K006  input() 返回值类型？                                  kb-02基础语法
K007  三种格式化输出方式？                                   kb-02基础语法
K008  Python三元运算符语法？                                 kb-03分支循环
K009  case _ 含义？                                        kb-03分支循环
K010  range(start,end,step) 哪个参数不包含？                  kb-03分支循环
K011  如何避免while死循环？                                  kb-03分支循环
K012  continue vs break？                                  kb-04字符串容器
K013  字符串切片语法？                                       kb-04字符串容器
K014  tuple vs list 核心区别？                               kb-04字符串容器
K015  .strip() 做什么？                                     kb-04字符串容器
K016  set 三个特征？                                        kb-05综合练习
K017  集合交并差？                                          kb-05综合练习
K018  列表推导式语法？                                       kb-05综合练习
K019  凯撒密码越界怎么处理？                                  kb-05综合练习
K020  函数四种参数类型及顺序？                                kb-06函数
K021  lambda语法和用途？                                    kb-06函数
K022  return 两个作用？                                     kb-06函数
K023  递归函数必备什么？                                     kb-06函数
K024  with 语句写文件？                                     kb-06函数
K025  面向对象三种访问级别？                                  kb-07面向对象
K026  调用父类构造方法？                                     kb-07面向对象
K027  多态两种形式？                                        kb-07面向对象
K028  __str__ 触发时机和返回值要求？                          kb-07面向对象
K029  try-except-else-finally 完整结构？                     kb-07面向对象
K030  两种导入方式？                                        kb-08NumpyJSON
K031  JSON对象/数组语法？                                   kb-08NumpyJSON
K032  json.loads vs json.dumps？                            kb-08NumpyJSON
K033  标准API调用 vs 流式调用？                              kb-08NumpyJSON
K034  调大模型API用什么方法和头？                             kb-08NumpyJSON
K035  NumPy数组四个核心属性？                                kb-09NumPy
K036  广播 vs 向量化？                                      kb-09NumPy
K037  逆矩阵和行列式？                                       kb-09NumPy
K038  np.dot() 1D vs 2D？                                  kb-09NumPy
K039  reshape 约束？                                       kb-09NumPy
K040  Pandas两大核心数据结构？                                kb-10Pandas
K041  loc vs iloc？                                        kb-10Pandas
K042  读写CSV/Excel/JSON？                                 kb-10Pandas
K043  describe() 返回什么？                                 kb-10Pandas
K044  Matplotlib中文乱码怎么解决？                            kb-15可视化
K045  四种基本图用什么函数？                                  kb-15可视化
K046  Seaborn vs Matplotlib区别？                           kb-15可视化
K047  Pandas数据清洗常用操作？                                kb-15可视化
K048  四种保留小数方式？                                     kb-11串讲1
K049  Python命名规范？                                      kb-11串讲1
K050  == vs is？                                          kb-11串讲1
K051  for in range() vs for in list？                     kb-12串讲2
K052  *args vs **kwargs？                                 kb-12串讲2
K053  list.sort() 默认和反转？                              kb-12串讲2
K054  list转set的好处？                                    kb-12串讲2
K055  手机号正则？                                          kb-13串讲3
K056  re.match() 返回值？                                  kb-13串讲3
K057  Python包标志？                                       kb-13串讲3
K058  Git提交工作流命令？                                    kb-16GitMySQL
K059  .gitignore 排除什么？                                kb-16GitMySQL
K060  MySQL六大约束？                                      kb-16GitMySQL
K061  模糊查询+范围查询SQL？                                 kb-16GitMySQL
K062  LEFT/RIGHT/INNER JOIN 区别？                         kb-17SQLAlchemy
K063  SQLAlchemy 连接三组件？                               kb-17SQLAlchemy
K064  SQLAlchemy CRUD操作？                                kb-17SQLAlchemy
K065  EXPLAIN 作用？                                       kb-17SQLAlchemy
K066  FastAPI启动命令？                                     kb-18FastAPI
K067  三种参数传递方式？                                     kb-18FastAPI
K068  注册路由？                                            kb-18FastAPI
K069  请求体模型必须继承什么？                                kb-18FastAPI
K070  Depends() 作用？                                    kb-19前端AIDD
K071  async endpoint怎么定义？                             kb-19前端AIDD
K072  文件上传用什么类？                                     kb-19前端AIDD
K073  HTML基本标签？                                        kb-19前端AIDD
K074  CSS三种选择器语法？                                    kb-20前端CSSJS
K075  margin vs padding？                                 kb-20前端CSSJS
K076  JS 变量/常量声明？                                    kb-20前端CSSJS
K077  JS === vs ==？                                      kb-20前端CSSJS
K078  AI-DD(Vibe Coding)是什么？                            kb-20前端CSSJS
K079  四种机器学习类型？                                     kb-29ML一
K080  过拟合/欠拟合/偏差/方差定义？                            kb-29ML一
K081  ML六步标准流程？                                      kb-29ML一
K082  线性回归四个评估指标？                                  kb-29ML一
K083  sklearn LinearRegression系数在哪？                    kb-29ML一
K084  逻辑回归用什么函数转概率？                               kb-30ML二
K085  二分类损失函数？                                       kb-30ML二
K086  L1(Lasso) vs L2(Ridge)区别？                         kb-30ML二
K087  什么时候用多项式回归？                                  kb-30ML二
K088  Miniconda vs Anaconda？                             kb-31ML三
K089  决策树三种分裂算法？                                    kb-31ML三
K090  Gini vs Entropy区别？                                kb-31ML三
K091  防决策树过拟合？                                       kb-31ML三
K092  SVM核心思想？                                        kb-32ML四
K093  SVM四种核函数？                                      kb-32ML四
K094  朴素贝叶斯"朴素"在哪？                                 kb-32ML四
K095  sklearn贝叶斯四种及场景？                              kb-32ML四
K096  KNN为什么必须标准化？                                  kb-32ML四
K097  Tensor与NumPy关系？                                  kb-36DL三
K098  requires_grad=True 作用？                            kb-36DL三
K099  为什么每步zero_grad？                                 kb-36DL三
K100  图像batch标准4D形状？                                 kb-36DL三
K101  自定义网络必须实现哪两个方法？                            kb-38FC
K102  标准四步训练循环？                                     kb-38FC
K103  model.train() vs model.eval()？                     kb-38FC
K104  CNN关键层？                                          kb-38FC
K105  Transformer用什么激活替代ReLU？                        kb-38FC
K106  基础RNN的致命缺陷？                                    kb-40RNN
K107  LSTM三门及职责？                                      kb-40RNN
K108  GRU简化了什么？                                       kb-40RNN
K109  PyTorch RNN三件套？                                  kb-40RNN
K110  常用中文分词库？                                       kb-40RNN
K111  Transformer对RNN两大优势？                             kb-41Transformer
K112  Q-K-V 范式？                                        kb-41Transformer
K113  为什么除以√d_k？                                      kb-41Transformer
K114  多头注意力目的？                                       kb-41Transformer
K115  为什么需要位置编码？                                    kb-41Transformer
K116  FFN 结构？                                           kb-41Transformer
K117  残差+LayerNorm 作用？                                 kb-41Transformer
K118  HuggingFace 三大核心组件？                             kb-42Transformer
K119  Pipeline 支持的NLP任务？                              kb-42Transformer
K120  BERT微调学习率"甜区"？                                kb-42Transformer
K121  NER微调为什么要标签对齐？                               kb-42Transformer
K122  tokenizer三个常用参数？                               kb-42Transformer
K123  五种提示词技术？                                       kb-46提示词工程
K124  Context Engineering 黄金法则？                        kb-46提示词工程
K125  JupyterLab两种单元格？                                kb-46提示词工程
K126  LangChain 三大核心模块？                               kb-47LangChain
K127  Model 三种调用？                                     kb-47LangChain
K128  Tool函数文档注释为什么必须写？                           kb-47LangChain
K129  Agent 用的什么推理模式？                                kb-47LangChain
K130  频率派 vs 贝叶斯派核心分歧？                             kb-math概率论
K131  方差MLE估计为什么除以N有偏？                             kb-math概率论
K132  高斯分布线性变换定理？                                  kb-math概率论
K133  条件分布中条件方差含义？                                 kb-math概率论
K134  为什么单高斯不够？解决方案？                              kb-math概率论
K135  R1-Zero vs R1 核心区别？                              sk-DeepSeekR1
K136  GRPO 无Critic怎么算基线？                              sk-DeepSeekR1
K137  拒绝采样解决什么问题？                                  sk-DeepSeekR1
K138  LoRA参数量化公式？                                     sk-LoRA
K139  A随机B全零初始化原因？                                  sk-LoRA
K140  LoRA三个局限？                                        sk-LoRA
K141  CLIP零样本分类原理？                                   sk-CLIP
K142  CLIP用的什么损失？                                     sk-CLIP
K143  base-patch32 vs large-patch14？                      sk-CLIP
K144  迭代 vs 增量本质区别？                                  sk-软件开发模式
K145  敏捷宣言四大价值观？                                    sk-软件开发模式
K146  螺旋模型为什么适合高风险项目？                            sk-软件开发模式
K147  幻觉四大根源？                                        sk-幻觉
K148  RAG如何缓解幻觉？                                      sk-幻觉
K149  什么场景幻觉可容忍？                                    sk-幻觉
K150  蒸馏核心思想？                                        sk-蒸馏
K151  CoT蒸馏 vs 输出蒸馏？                                  sk-蒸馏
K152  蒸馏 vs 量化区别？                                     sk-蒸馏
K153  预训练→微调的关系？                                     kb-预训练模型生态与中文大模型
K154  Encoder/Decoder的注意力方向？                             kb-预训练模型生态与中文大模型
K155  BERT和GPT架构哪个说法错误？                               kb-预训练模型生态与中文大模型
K156  HF生态核心产品有哪些？                                   kb-预训练模型生态与中文大模型
K157  发展中文大模型的必要性原因？                               kb-预训练模型生态与中文大模型
K158  GDN/GQA的共同目标？                                     kb-预训练模型生态与中文大模型
K159  自注意力是预训练模型的核心创新？                             kb-预训练模型生态与中文大模型
K160  基座模型有chat_template吗？                              kb-预训练模型生态与中文大模型
K161  apply_chat_template什么作用？                             kb-预训练模型生态与中文大模型
K162  预训练和微调的区别与关系？                                 kb-预训练模型生态与中文大模型
K163  为什么对话模型需要apply_chat_template？                    kb-预训练模型生态与中文大模型
K164  MLM vs CLM（掩码语言模型 vs 因果语言模型）区别？               kb-模块一预训练模型生态与中文大模型
K165  为什么主流大模型都用Decoder-only？                            kb-模块一预训练模型生态与中文大模型
K166  RLHF在ChatGPT中起什么作用？                                  kb-模块一预训练模型生态与中文大模型
K167  涌现能力（Emergent Abilities）是什么？                         kb-模块一预训练模型生态与中文大模型
K168  attention_mask的作用是什么？                                  kb-模块一预训练模型生态与中文大模型
K169  GLM的Prefix-LM与GPT的Decoder-only有什么区别？                 kb-模块一预训练模型生态与中文大模型
K170  GDN为什么是O(n)？和Softmax Attention(O(n²))的核心区别？        kb-模块一预训练模型生态与中文大模型
K171  MoE（混合专家）的核心思想是什么？                               kb-模块一预训练模型生态与中文大模型
K172  BBPE（字节级BPE）与普通BPE的核心区别？                          kb-模块一预训练模型生态与中文大模型
K173  指令微调数据的标准格式（三个字段）？                              kb-模块一预训练模型生态与中文大模型
K174  T5的Text-to-Text统一范式是什么？                              kb-模块一预训练模型生态与中文大模型
K175  GPT系列从1到5.5的关键演进节点？                                kb-模块一预训练模型生态与中文大模型
K176  为什么需要模型压缩？                                           kb-模块二大模型压缩
K177  FP8和INT4的本质区别？为什么FP8能加速计算、INT4只能省显存？         kb-模块二大模型压缩
K178  对称量化 vs 非对称量化，各用在什么场景？                           kb-模块二大模型压缩
K179  PTQ/QAT/QLoRA三种量化做法的区别？                                kb-模块二大模型压缩
K180  量化时哪些层不量化？为什么？                                      kb-模块二大模型压缩
K181  AWQ核心原理？（激活感知量化）                                     kb-模块二大模型压缩
K182  GPTQ核心原理？（Hessian矩阵补偿）                                 kb-模块二大模型压缩
K183  数据蒸馏 vs 传统KL蒸馏，LLM时代主流做法？                          kb-模块二大模型压缩
K184  FP8 E4M3 vs E5M2两种格式区别？                                   kb-模块二大模型压缩
K185  不同场景怎么选压缩方案？（H100生产/4090本地/CPU/移动端）            kb-模块二大模型压缩
K186  BERT/GPT/XLNet三架构对比？双向理解+自回归生成怎么兼得？          kb-模块一+学员推导
K187  CSA和HCA的关系？DeepSeek-V4的混合注意力怎么配合？               kb-教师问卷06-24
K188  量化粒度 per-tensor/per-channel/per-group 区别？                 kb-教师问卷06-24
K189  为什么模型越大，量化损失越小？                                    kb-教师问卷06-24
K190  AWQ为什么要对重要通道乘放大系数s再量化？推理时怎么恢复？            kb-教师问卷06-24
K191  推理两阶段 Prefill vs Decode 区别？各看GPU什么指标？              kb-学员总结06-24
K192  KV Cache 跟模型哪些参数有关？跟参数量直接相关吗？                   kb-学员总结06-24
K193  GQA（分组查询注意力）一句话原理？为什么省显存？                      kb-学员总结06-24
K194  PagedAttention 核心思想？类比什么？                                 kb-学员总结06-24
K195  ZeRO-1/ZeRO-2/ZeRO-3 三级区别？各自拆什么？                         kb-学员总结06-24
K196  训练卡 vs 推理卡 区别？显卡三大指标口诀？                             kb-学员总结06-24
K197  LoRA低秩原理？为什么ΔW=B×A有效？秩到底是什么？                         kb-学员推导06-25
K198  MLA（多头潜在注意力）vs MHA vs GQA 三种注意力区别？                     kb-学员总结06-25
K199  Fine-grained MoE vs Hierarchical MoE 两条路线区别？                    kb-学员总结06-25
K200  RoPE为什么天然感知相对位置？（数学原理）                                 kb-学员总结06-25
K201  MTP（多Token预测）是什么？为什么能加速推理？                             kb-学员总结06-25
K202  位置编码演化线？Sin/Cos→可学习→RoPE→RoPE+YaRN？                         kb-学员总结06-25
K203  LLaMA Factory vs Unsloth 区别？各适合什么场景？                           kb-教师晨考06-26
K204  DeepSpeed ZeRO 选型策略？单卡放得下时该选什么？                            kb-教师晨考06-26
K205  train_on_responses_only 作用？为什么微调时要mask掉user部分？               kb-教师晨考06-26
K206  单卡24GB微调Qwen3.6-27B(BF16≈56GB)，全参/LoRA/QLoRA选哪个？               kb-教师晨考06-26
```

---

## 统计

| 来源 | 题数 |
|------|------|
| Knowledge_base/ (课件) | 167 |
| share_know/ (课外) | 18 |
| 教师问卷+晨考 | 8 |
| 学员总结+推导 | 13 |
| **总计** | **206** |
