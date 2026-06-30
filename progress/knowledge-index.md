# 百科全书索引

> **最后更新**：2026-06-03
> **用途**：课件+课外知识考点索引，不与个人实战题库混淆
> **桥接规则**：考点需经"学员实际接触过"（课堂讨论/提问/练习暴露）方可晋升至 `question-bank.md`

---

## 📊 统计概览

| 来源 | 文件数 | 考点数 | 状态 |
|------|--------|--------|------|
| Knowledge_base/ | 32 `.md` | ~140 | ✅ 已提取 |
| Knowledge_base/ | 3 `.pdf` | — | ⬜ 待提取（需PDF工具） |
| share_know/ | 6 `.md` | 18 | ✅ 已提取 |
| share_know/ | 1 `.md` | 0 | 空文件（大模型里的温度.md） |

---

## 一、Knowledge_base 课件索引

### 01-07: Python 基础阶段

**文件**：`AI大模型开发—01环境搭建和Hell World.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | Python 是什么类型的语言？ | 解释型语言，推荐3.12+ |
| 2 | 三大包管理器？ | pip/conda/uv |
| 3 | 如何验证Python安装？ | `python -V` / `pip -V` |

**文件**：`AI大模型开发—02Python基础语法.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | `type()` 的作用？核心数据类型？ | 返回数据类型；int/float/bool/str/complex + 容器 |
| 2 | 三个逻辑运算符的真值规则？ | and(全True)、or(全False)、not(反转) |
| 3 | `input()` 返回值类型？ | 始终返回字符串，需 int()/float() 转换 |
| 4 | 三种格式化输出方式？ | f-string / %格式化 / print(sep, end) |

**文件**：`AI大模型开发—03Python分支循环.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | Python三元运算符语法？ | `Y if X else Z`，非C风格 `X?Y:Z` |
| 2 | `case _` 含义？ | match-case 中的通配默认分支 |
| 3 | `range(start, end, step)` 哪个参数不包含？ | end 不包含 |
| 4 | 如何避免while死循环？ | 循环体内更新条件变量 |

**文件**：`AI大模型开发—04字符串和容器类型.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | `continue` vs `break`？ | continue=跳过本次；break=终止整个循环 |
| 2 | 字符串切片语法？ | `str[start:end:step]`，负数从末尾数 |
| 3 | tuple vs list 核心区别？ | tuple不可变用()，list可变用[] |
| 4 | `.strip()` 做什么？ | 去除首尾空白 |

**文件**：`AI大模型开发—05综合练习和容器数据类型二.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | set 三个特征？ | 无序、不可重复、可变 |
| 2 | 集合交并差？ | union/intersection/difference |
| 3 | 列表推导式语法？ | `[expression for var in iterable if condition]` |
| 4 | 凯撒密码越界怎么处理？ | ord()+偏移→超'z'/122减26→chr() |

**文件**：`AI大模型开发—06函数.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | 函数四种参数类型？ | 普通→默认值→*args(元组)→**kwargs(字典) |
| 2 | lambda语法和用途？ | `lambda params: expression`，匿名单行函数 |
| 3 | return 两个作用？ | 返回值 + 终止函数执行 |
| 4 | 递归函数必备什么？ | base case 退出条件 |
| 5 | with 语句写文件？ | `with open("f","w",encoding="utf-8") as f: f.write(content)` |

**文件**：`AI大模型开发—07面向对象.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | 三种访问级别？ | public(self.x) / protected(self._x) / private(self.__x，名称改写) |
| 2 | 调用父类构造方法？ | `super().__init__(args)` |
| 3 | 多态两种形式？ | 方法重写 + 子类对象自动向上转型 |
| 4 | `__str__` 触发时机和返回值要求？ | print(obj)自动调用，必须返回str |
| 5 | try-except-else-finally 完整结构？ | try→except→else(无异常)→finally(始终执行) |

---

### 08-15: 数据分析阶段

**文件**：`AI大模型开发—08数据分析Numpy.md`（注：实际为模块/JSON/requests）
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | 两种导入方式？ | `import module as alias` / `from module import item` |
| 2 | JSON对象/数组语法？ | 对象`{"key":"value"}`键必须双引号；数组`[elem,...]` |
| 3 | json.loads vs json.dumps？ | loads=字符串→Python对象；dumps=Python对象→字符串 |
| 4 | 标准API调用 vs 流式调用？ | 标准等全部；流式stream=True逐行返回 |
| 5 | 调大模型API用什么方法和头？ | POST + Authorization: Bearer + Content-Type: application/json |

**文件**：`AI大模型开发—09数据分析Pandas.md`（注：实际为NumPy）
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | NumPy数组四个核心属性？ | size/shape/ndim/dtype |
| 2 | 广播 vs 向量化？ | 广播=自动扩展小数组形状匹配；向量化=标量应用到每个元素 |
| 3 | 逆矩阵和行列式？ | `np.linalg.inv()` / `np.linalg.det()` |
| 4 | `np.dot()` 1D vs 2D？ | 1D=内积；2D=矩阵乘法 |
| 5 | reshape 约束？ | 总元素数不变 |

**文件**：`AI大模型开发—10数据分析Matplotlib.md`（注：实际为Pandas）
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | Pandas两大核心数据结构？ | Series(1D) / DataFrame(2D) |
| 2 | `loc` vs `iloc`？ | loc=标签访问；iloc=整数位置访问 |
| 3 | 读写CSV/Excel/JSON？ | read_csv/excel/json；to_csv/excel/json(Excel需openpyxl) |
| 4 | `describe()` 返回什么？ | count/mean/std/min/25%/50%/75%/max |

**文件**：`AI大模型开发—15数据分析Matplotlib和Seaborn.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | Matplotlib中文乱码怎么解决？ | `plt.rcParams['font.sans-serif']=['SimHei']` |
| 2 | 四种基本图用什么函数？ | plot(线)/bar(柱)/pie(饼)/scatter(散点) |
| 3 | Seaborn vs Matplotlib区别？ | Seaborn更高层API，更好默认样式，复杂统计图 |
| 4 | Pandas数据清洗常用操作？ | isnull/fillna/dropna/drop_duplicates/astype |

---

### 11-13: 知识串讲

**文件**：`AI大模型开发—11知识串讲.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | 四种保留小数方式？ | `"%.2f"%num` / `f"{num:.2f}"` / `format()` / `round()` |
| 2 | Python命名规范？ | 类=PascalCase，函数=snake_case，常量=UPPER_SNAKE |
| 3 | `==` vs `is`？ | ==值相等，is同一对象(内存地址) |

**文件**：`AI大模型开发—12知识串讲Python语法.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | `for in range()` vs `for in list`？ | range生成整数序列；list返回元素本身 |
| 2 | `*args` vs `**kwargs`？ | *args→元组(位置)；**kwargs→字典(关键字) |
| 3 | `list.sort()` 默认和反转？ | 默认升序；`reverse=True`降序 |
| 4 | list转set的好处？ | `set(list)`自动去重 |

**文件**：`AI大模型开发—13知识串讲Python语法进阶.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | 手机号正则？ | `^1[3-9][\d]{9}$` |
| 2 | `re.match()` 返回值？ | 匹配=Match对象；不匹配=None |
| 3 | Python包标志？ | 含`__init__.py`的目录(Python3.3+非必需) |

---

### 16-18: Git/MySQL/FastAPI

**文件**：`AI大模型开发—16Git和Mysql一.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | Git提交工作流命令？ | init→add→commit -m→status→log |
| 2 | `.gitignore` 排除什么？ | venv/、.idea/、__pycache__/、.env |
| 3 | MySQL六大约束？ | PRIMARY KEY/FOREIGN KEY/NOT NULL/UNIQUE/DEFAULT/AUTO_INCREMENT |
| 4 | 模糊查询+范围查询SQL？ | `WHERE name LIKE '张%' AND age BETWEEN 18 AND 30` |

**文件**：`AI大模型开发—17Mysql二和SQLAlchemy.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | LEFT/RIGHT/INNER JOIN 区别？ | INNER=交集；LEFT=左全+右NULL；RIGHT=右全+左NULL |
| 2 | SQLAlchemy 连接三组件？ | create_engine + sessionmaker + Base |
| 3 | SQLAlchemy CRUD操作？ | C=add+commit；R=query.filter.all()；U=改属性+commit；D=delete+commit |
| 4 | `EXPLAIN` 作用？ | 分析查询执行计划，ALL=全表扫描=差 |

**文件**：`AI大模型开发—18FastApi.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | FastAPI启动命令？ | `uvicorn main:app --reload` |
| 2 | 三种参数传递方式？ | Query(URL键值) / Path({param}在路径) / Body(JSON需Pydantic BaseModel) |
| 3 | 注册路由？ | `app.include_router(router_module.router)` |
| 4 | 请求体模型必须继承什么？ | `pydantic.BaseModel` |

---

### 19-20: 前端 + AI-DD

**文件**：`AI大模型开发—19前端和AI-DD.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | `Depends()` 作用？ | FastAPI依赖注入，常用在数据库session管理 |
| 2 | async endpoint怎么定义？ | `async def` + 内部用 `await` |
| 3 | 文件上传用什么类？ | `fastapi.UploadFile`，多文件=`list[UploadFile]` |
| 4 | HTML基本标签？ | table/tr/td、input/select/textarea、ol/ul/li |

**文件**：`AI大模型开发—20前端css和js和AI-DD.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | CSS三种选择器语法？ | 标签(p)、id(#id)、class(.class) |
| 2 | margin vs padding？ | margin=外边距(不影响尺寸)；padding=内边距(影响尺寸) |
| 3 | JS 变量/常量声明？ | `let`(可变) / `const`(不可变) |
| 4 | JS `===` vs `==`？ | ===严格相等(值+类型)；==宽松相等(类型转换) |
| 5 | AI-DD(Vibe Coding)是什么？ | AI驱动的开发，用自然语言生成60-80%代码 |

---

### 29-32: 机器学习阶段

**文件**：`AI大模型开发—29机器学习一.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | 四种机器学习类型？ | 监督/无监督/半监督/强化学习 |
| 2 | 过拟合/欠拟合/偏差/方差定义？ | 过=记训练噪声；欠=太简单；偏差=系统误差；方差=对训练数据敏感度 |
| 3 | ML六步标准流程？ | 加载→EDA→预处理→训练→评估→特征分析 |
| 4 | 线性回归四个评估指标？ | MSE/RMSE/MAE/R² |
| 5 | sklearn LinearRegression系数在哪？ | `model.coef_`(权重) / `model.intercept_`(偏置) |

**文件**：`AI大模型开发—30机器学习二.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | 逻辑回归用什么函数转概率？ | sigmoid: `σ(z)=1/(1+e^(-z))` |
| 2 | 二分类损失函数？ | 交叉熵: `-Σ(y·log(p)+(1-y)·log(1-p))/n` |
| 3 | L1(Lasso) vs L2(Ridge)区别？ | L1=加绝对值→可压到0→特征选择；L2=加平方→缩小但不为0 |
| 4 | 什么时候用多项式回归？ | 特征与目标非线性关系，用PolynomialFeatures转换后接LinearRegression |

**文件**：`AI大模型开发—31机器学习三.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | Miniconda vs Anaconda？ | Miniconda~50MB轻量；Anaconda~3GB含250+预装包 |
| 2 | 决策树三种分裂算法？ | ID3(信息增益)/C4.5(信息增益率)/CART(Gini/MSE)，sklearn=CART |
| 3 | Gini vs Entropy区别？ | Gini计算快、树浅；Entropy慢、树深，效果相近 |
| 4 | 防决策树过拟合？ | 预剪枝(max_depth/min_samples_split/leaf)；后剪枝(CCP)；集成 |

**文件**：`AI大模型开发—32机器学习四.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | SVM核心思想？ | 求最大化间隔的超平面，支撑向量=最近的点 |
| 2 | SVM四种核函数？ | Linear/Polynomial/RBF(Gaussian)/Sigmoid |
| 3 | 朴素贝叶斯"朴素"在哪？ | 假设所有特征条件独立（实践中常不成立但有效） |
| 4 | sklearn贝叶斯四种及场景？ | GaussianNB(连续)/MultinomialNB(文本计数)/BernoulliNB(二值)/ComplementNB(不均衡文本) |
| 5 | KNN为什么必须标准化？ | 距离度量对特征量级敏感，不标准化会被大数值特征主导 |

---

### 36-42: 深度学习 + Transformer 阶段

**文件**：`AI大模型开发—36深度学习三PyTorch框架.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | Tensor与NumPy关系？ | `torch.from_numpy()`创建，共享内存 |
| 2 | `requires_grad=True` 作用？ | 标记为叶节点，跟踪运算，backward后存于.grad |
| 3 | 为什么每步zero_grad？ | PyTorch默认累加梯度，不清零会跨batch混在一起 |
| 4 | 图像batch标准4D形状？ | `[batch_size, channels, height, width]` |

**文件**：`AI大模型开发之38PyTorch全连接神经网络.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | 自定义网络必须实现哪两个方法？ | `__init__()`(定义层) + `forward(self,x)`(前向流程) |
| 2 | 标准四步训练循环？ | data.to→forward+loss→zero_grad+backward→step |
| 3 | `model.train()` vs `model.eval()`？ | train=启用Dropout/BN更新；eval=关闭+配合no_grad |
| 4 | CNN关键层？ | Conv2d→ReLU→MaxPool2d→Flatten→Linear |
| 5 | Transformer用什么激活替代ReLU？ | GELU（更平滑，BERT后标配） |

**文件**：`AI大模型开发之40RNN.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | 基础RNN的致命缺陷？ | BPTT梯度消失/爆炸→长程遗忘 |
| 2 | LSTM三门及职责？ | 遗忘门(丢弃旧信息)/输入门(存新信息)/输出门(暴露多少) |
| 3 | GRU简化了什么？ | 2门：更新门(合并遗忘+输入)+重置门；合并C和h |
| 4 | PyTorch RNN三件套？ | `nn.RNN` / `nn.LSTM` / `nn.GRU` |
| 5 | 常用中文分词库？ | jieba/jiagu/snownlp/thulac/LAC |

**文件**：`AI大模型开发之41Transformer一.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | Transformer 对 RNN 两大优势？ | 并行计算 + 直接长程依赖(O(1)距离) |
| 2 | Q-K-V 范式？ | Q="找什么" K="有什么标签" V="内容是什么" |
| 3 | 为什么除以√d_k？ | 防止点积过大→softmax梯度消失 |
| 4 | 多头注意力目的？ | 不同头关注不同表示子空间（语法/语义等） |
| 5 | 为什么需要位置编码？ | 注意力本身无序，"猫吃鱼"和"鱼吃猫"得分相同 |
| 6 | FFN 结构？ | 先升4倍(768→3072)→激活(GELU)→压回(3072→768) |
| 7 | 残差+LayerNorm 作用？ | 残差防梯度消失；LN稳定训练 |

**文件**：`AI大模型开发之42Transformer二.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | HuggingFace 三大核心组件？ | Tokenizer / Model / Pipeline |
| 2 | Pipeline 支持的NLP任务？ | 情感分析/文本分类/生成/QA/NER/翻译/摘要/零样本 |
| 3 | BERT微调学习率"甜区"？ | 2e-5 ~ 5e-5 |
| 4 | NER微调为什么要标签对齐？ | BERT子词拆分→标签需对齐：首子词=原标签，后续子词=-100 |
| 5 | tokenizer三个常用参数？ | padding/truncation/return_tensors |

---

### 46-47: 提示词工程 + LangChain

**文件**：`AI大模型开发46之Jupyter和提示词工程.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | 五种提示词技术？ | Zero-shot/Few-shot/CoT(一步步思考)/ToT(多分支)/ReAct(推理+行动) |
| 2 | Context Engineering 黄金法则？ | 最重要信息放上下文开头和结尾（模型注意力最高） |
| 3 | JupyterLab两种单元格？ | Code(执行Python) / Markdown(写文档) |

**文件**：`AI大模型开发47Agent之Langchain.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | LangChain 三大核心模块？ | Model + Tools + Agent |
| 2 | Model 三种调用？ | invoke(同步)/stream(流式)/batch(并行) |
| 3 | Tool函数文档注释为什么必须写？ | LLM读取docstring决定何时调用该工具 |
| 4 | Agent 用的什么推理模式？ | ReAct（思考↔工具调用循环） |

---

### 数学基础

**文件**：`math-foundations/ch01-概率论基础与高斯分布.md`
| # | 考点 | 答案要点 |
|---|------|---------|
| 1 | 频率派 vs 贝叶斯派核心分歧？ | 频率=θ是固定未知常数(MLE)；贝叶斯=θ是随机变量(Bayes更新,MAP) |
| 2 | 方差MLE估计为什么除以N有偏？ | 用同数据估计均值和方差→损失1自由度→无偏估计用N-1 |
| 3 | 高斯分布线性变换定理？ | x~N(μ,Σ) → y=Ax+b ~ N(Aμ+b, AΣA^T) |
| 4 | 条件分布中条件方差含义？ | 观测x_a后对x_b不确定性减少：新方差=原方差−被x_a解释的方差 |
| 5 | 为什么单高斯不够？解决方案？ | 单峰→多峰数据用GMM(高斯混合模型) |

---

## 二、share_know 课外知识索引

**文件**：`DeepSeek-R1 完整训练流程：从实验到成品.md`
| # | 考点 | 答案要点 | 是否已在题库 |
|---|------|---------|------------|
| 1 | R1-Zero vs R1 核心区别？ | Zero=纯RL实验(无SFT)；R1=四阶段产品(冷启动SFT→推理RL→拒绝采样SFT→全场景RL) | 部分(F032/F033) |
| 2 | GRPO 无Critic怎么算基线？ | 同组16条回答均分作基线，Advantage=自己−平均 | 已入库 |
| 3 | 第三阶段"拒绝采样"解决什么问题？ | 第二阶段后模型成"偏科专家"，拒绝采样=生成多条→只保留正确的→混通用数据再做SFT | 未入库 |

**文件**：`LoRA低秩微调知识点总结.md`
| # | 考点 | 答案要点 | 是否已在题库 |
|---|------|---------|------------|
| 1 | LoRA 参数量化公式？ | r=8时4096×4096仅训~65K参数，省~256倍 | 已入库(F031) |
| 2 | A随机B全零初始化原因？ | B=0→BA=0→初始不破坏原模型 | 已入库(F030) |
| 3 | LoRA三个局限？ | 基础模型弱不行/新任务差异太大不行/rank r需要调 | 未入库 |

**文件**：`OpenAI CLIP.md`
| # | 考点 | 答案要点 | 是否已在题库 |
|---|------|---------|------------|
| 1 | CLIP零样本分类原理？ | 双塔(图像+文本编码器)→共享嵌入空间→余弦相似度→最高分标签 | 未入库 |
| 2 | CLIP用的什么损失？ | 双向InfoNCE：图文互检索，正对拉近负对推远 | 未入库 |
| 3 | base-patch32 vs large-patch14？ | base轻量(CPU可跑)/large精细(小文字)，量vs质取舍 | 未入库 |

**文件**：`主流软件开发模式.md`
| # | 考点 | 答案要点 | 是否已在题库 |
|---|------|---------|------------|
| 1 | 迭代 vs 增量本质区别？ | 迭代=同功能反复打磨；增量=架构不变逐步加功能 | 未入库 |
| 2 | 敏捷宣言四大价值观？ | 个体互动>流程工具/可工作软件>文档/客户合作>合同/响应变化>遵循计划 | 已入库(S001) |
| 3 | 螺旋模型为什么适合高风险项目？ | 每圈核心=风险分析，持续评估+缓解，航空航天/金融用 | 未入库 |

**文件**：`大模型幻觉知识分享.md`
| # | 考点 | 答案要点 | 是否已在题库 |
|---|------|---------|------------|
| 1 | 幻觉四大根源？ | 训练数据不足过时/概率生成机制/上下文误解/缺外部验证 | 未入库 |
| 2 | RAG如何缓解幻觉？ | 检索→向量库→相关文档注入prompt→回答有据可依 | 未入库 |
| 3 | 什么场景幻觉可容忍？ | 创意写作/头脑风暴(幻觉=创造力)；医疗/法律零容忍 | 未入库 |

**文件**：`大模型蒸馏.md`
| # | 考点 | 答案要点 | 是否已在题库 |
|---|------|---------|------------|
| 1 | 蒸馏核心思想？ | 大老师→小学生，学生学老师的软标签(类间关系) | 未入库 |
| 2 | CoT蒸馏 vs 输出蒸馏？ | 输出蒸馏只学答案；CoT蒸馏学完整推理链(R1-Distill做法) | 未入库 |
| 3 | 蒸馏 vs 量化区别？ | 蒸馏=减参数(70B→7B)；量化=降精度(FP16→INT4)，参数数不变 | 已入库(S002部分) |

**文件**：`大模型里的温度.md`
| 状态 | 说明 |
|------|------|
| ⚠️ 空文件 | 0字节，无内容可提取 |

---

## 🔗 桥接晋升规则

knowledge-index 中的考点晋升至 `question-bank.md` 需满足：

1. **课堂接触**：学员在对话中讨论过、提问过、或用代码验证过
2. **练习暴露**：做练习时因该考点出错或卡顿
3. **主动标记**：学员明确说"这个记一下"或"这个重要"

晋升后在 question-bank.md 来源字段标注 `kb-{文件名}` 或 `sk-{文件名}`。
当 question-bank 🟢常规区 < 10 题时，CLAUDE.md 授权从本索引精选补充。

---

### K153 预训练→微调的关系？（单选）

> 学生先在海量互联网文本上"通读"学会语言通用规律，再针对对话任务进行专门训练，最终得到一个能聊天的大模型。这种"先通读再专训"的范式体现了哪两个核心阶段的关系
> A. 预训练→推理 B. 预训练→微调 C. 微调→预训练 D. 推理→微调
> **答案：B** | 通读=预训练，专训=微调

### K154 Encoder/Decoder的注意力方向？（单选+判断）

> Q1: Transformer架构中，负责双向理解上下文的组件是
> A. Encoder B. Decoder C. Embedding D. Self-Attention
> **答案：A** | Encoder双向理解，Decoder单向生成
>
> Q2: 以下关于Transformer架构的说法，正确的是
> A. Encoder单向/Decoder双向 B. Encoder双向/Decoder单向 C. 都双向 D. 都单向
> **答案：B** | 口诀：编双解单

### K155 BERT和GPT架构哪个说法错误？（单选）

> 以下关于BERT和GPT架构的说法，错误的是
> A. BERT使用Encoder-only B. GPT使用Decoder-only C. BERT适合文本生成 D. GPT用因果掩码自回归生成
> **答案：C** | BERT擅长理解，不擅长生成；GPT擅长生成

### K156 HF生态核心产品有哪些？（多选）

> 以下哪些是HuggingFace生态中的核心产品
> A. Transformers B. PyTorch C. Datasets D. Tokenizers E. PEFT
> **答案：ACDE** | PyTorch是Meta的，不属于HF生态

### K157 发展中文大模型的必要性原因？

> 以下哪个不是发展中文大模型的必要性原因
> A. 中文语法语义与英文差异大 B. 中文互联网内容占比最高，无需英文数据 C. 独特文化背景 D. 需专门清洗
> **答案：B** | 该表述本身错误，中文占比并非全球最高，也需英文语料补充

### K158 GDN/GQA的共同目标？

> GDN(Gated Delta Net)和GQA(Grouped Query Attention)优化技术的共同目标是
> A. 增加参数量 B. 提升推理速度 C. 增大上下文窗口 D. 支持多模态
> **答案：B** | 二者均为推理优化技术，核心目标是提速降本

### K159 自注意力是预训练模型的核心创新？（判断）

> 预训练模型的核心创新是自注意力机制(Self-Attention)
> **答案：错误** | 自注意力是Transformer的核心创新，不是预训练模型的核心创新

### K160 基座模型有chat_template吗？（判断）

> 基座模型(如GPT-2)没有对话模板，因此tokenizer.chat_template输出为None
> **答案：正确** | 只有经过对话微调的模型才有对话模板

### K161 apply_chat_template什么作用？（填空）

> 使用Qwen对话模型时，需要调用 `____` 方法将messages列表自动转换为模型训练时使用的对话格式
> **答案：apply_chat_template**

### K162 预训练和微调的区别与关系？（简答）

**区别**：①目标不同：预训练学通用规律；微调适配特定任务 ②数据不同：预训练用海量无标注文本；微调用小规模任务标注数据 ③成本不同：预训练极高；微调低(可LoRA进一步降) ④训练方式不同：预训练从零训全参数；微调可全参可部分

**关系**：预训练是微调的能力底座，微调是预训练的场景落地。二者构成"通用能力习得→专项能力适配"的核心范式

### K163 为什么对话模型需要apply_chat_template？（简答）

① 对话模型需训练推理格式对齐：训练时用了固定对话格式，推理时输入必须和训练完全一致才能正确区分角色；apply_chat_template自动完成格式转换，保证输入分布一致

② 基座模型没有对话格式预设：仅完成通用预训练，未学对话角色/格式，输入就是普通文本，不需要对话模板

### K164 MLM vs CLM 区别？

> MLM（掩码语言模型）：遮住句中某些词让模型预测。双向上下文都可见。"今天 [MASK] 气很好"→预测"天"。BERT用。
> CLM（因果语言模型）：只看左边预测下一个词。"今天天"→预测"气"。GPT用。
> **核心区别**：MLM双向填空、BERT专长；CLM单向续写、GPT专长

### K165 为什么主流大模型都用Decoder-only？

> ① 扩展性好：单塔结构简单，Scaling Law表现更优
> ② ICL自然涌现：因果掩码天然适合上下文学习
> ③ 泛用性强：生成任务可覆盖理解任务，反之不行
> ④ KV Cache友好：单塔推理快
> ⑤ 对话天生匹配：因果LM与对话续写天然一致
> **一句话**：Decoder-only在"大力出奇迹"下性价比最高，涌现能力最实用

### K166 RLHF在ChatGPT中起什么作用？

> RLHF（Reinforcement Learning from Human Feedback）：人类标注员对模型回答打分→用强化学习训练模型生成更符合人类偏好的回答。
> **为什么关键**：预训练只让模型"会说话"，RLHF让模型"会说人话"——这是ChatGPT从GPT-3质变的核心

### K167 涌现能力是什么？

> 当模型参数大到一定程度（约100B+），突然展现出小模型没有的能力——如上下文学习（ICL）、思维链（CoT）。这些能力没有显式训练，是规模触发"跳变"。
> **面试关键**：涌现=量变→质变，Scale是必要条件但不充分

### K168 attention_mask的作用？

> 处理批次内不同长度文本。短文本需padding到统一长度，attention_mask标记1=真实内容/0=填充占位→让模型计算注意力时忽略填充位。
> **单条推理时全为1，批量推理/训练时至关重要**——否则填充位的噪声会混入注意力计算

### K169 GLM Prefix-LM vs GPT Decoder-only？

> GPT：1套Decoder Block，全部因果掩码（单向）
> GLM：1套Transformer Block，输入部分双向注意（像BERT）、生成部分因果掩码（像GPT）——单塔切换角色
> T5：2套Block（Encoder+Decoder），双塔
> **口诀**：GPT=一个人只往前看，GLM=一个人听的时候全局看/说的时候按顺序，T5=两个人各司其职

### K170 GDN为什么是O(n)？

> Softmax Attention：每新token跟所有旧token两两比较(Q·Kᵀ)→O(n²)
> GDN：不做两两比较，旧token信息浓缩成"状态向量"，新token只跟状态合并一次→O(n)
> **类比**：Softmax=新来的人跟全屋人挨个握手，GDN=新人只跟记录员对个眼神
> Qwen3.5用75%GDN+25%Full Attention混合

### K171 MoE（混合专家）核心思想？

> 每层放多个"专家"子网络，每个token只激活部分专家（路由选择）。总参数量大但激活参数少→同等质量下推理算力只需1/10。
> **类比**：公司不全是全才，按需叫对口专家——284B总参数但干活只叫13B
> DeepSeek-V4、GLM-4.7、Qwen3.6均用MoE

### K172 BBPE vs 普通BPE？

> 普通BPE：以字符为最细粒度→词表没有的字符变[UNK]
> BBPE：以UTF-8字节为最细粒度→任何Unicode字符都能拆成1-4字节→不存在[UNK]
> **代价**：序列长度略增（如🐹=4字节tokens），但彻底消灭OOV

### K173 指令微调数据标准格式？

> 三个字段：① instruction（指令）② input（输入/可选）③ output（期望输出）
> 让模型学会"听指令办事"而非只"续写文本"
> 例：`{"instruction":"翻译成英文", "input":"今天天气好", "output":"The weather is nice today."}`

### K174 T5的Text-to-Text统一范式？

> 所有NLP任务统一为"输入文本→输出文本"。翻译/摘要/分类/问答——同一个模型、同一种格式。
> "translate English to German: How are you?"→"Wie geht es dir?"
> GPT的Decoder-only后来证明同样统一且更简洁

### K175 GPT系列关键演进节点？

> GPT-1(2018/1.17亿)：证明生成式预训练有效
> GPT-2(2019/15亿)：零样本能力初现
> GPT-3(2020/1750亿)：涌现能力+上下文学习
> GPT-3.5(2022)：ChatGPT诞生+RLHF引入
> GPT-4(2023)：多模态+推理飞跃
> GPT-5(2025)：统一架构+内置推理
> GPT-5.5(2026)：全新预训练+Agent能力飞跃

### K176 为什么需要模型压缩？

> 百亿级模型部署极贵：Qwen3.5-397B FP16需794GB显存→至少5×H100。
> 压缩目标：在尽量不损失能力的前提下，把模型塞进更少显存。
> 四大收益：省钱、提速度(更高吞吐)、降功耗、设备适配(移动端/IoT/消费级GPU)

### K177 FP8和INT4的本质区别？

> **INT4**：浮点→整数，需scale/zero_point映射→推理时反量化回FP16计算→**只省显存不加速**（还是走FP16运算单元）
> **FP8**：高精度浮点→低精度浮点，自带指数位→H100 Tensor Core原生支持FP8矩阵乘法→**既省显存又加速2倍**
> **类比**：INT4=翻译（格式变了需来回转换），FP8=缩印（字体不变大小减半，直接能读）

### K178 对称量化 vs 非对称量化？

> **对称量化**：zero_point=0，假设权重对称分布（如[-3.2,3.2]→INT4[-8,7]）→计算快，适合作权重
> **非对称量化**：zero_point≠0，充分利用整数范围（如[0,6.3]→UINT8[0,255]）→精度高，适合作激活值（ReLU/GELU后非负）
> **面试关键**：权重≈对称（均值≈0），激活≈非对称（非负分布）

### K179 PTQ/QAT/QLoRA三种量化做法的区别？

> | 做法 | 时机 | 是否重训 | 代表 |
> |------|------|---------|------|
> | **PTQ** | 训练后量化 | ❌ 几小时 | AWQ/GPTQ/FP8(主流) |
> | **QAT** | 训练时模拟量化 | ✅ 需重训 | LLM-QAT(极端压缩) |
> | **QLoRA** | 加载时量化 | 训练时反量化 | bitsandbytes NF4(消费级GPU微调) |

### K180 量化时哪些层不量化？为什么？

> - **Embedding/LM Head**：词表大(10万+)，量化掉点严重；查表操作量化反慢
> - **LayerNorm/Softmax**：数值敏感（归一化、exp函数对精度敏感）
> - **首尾Transformer层**：激活分布最不稳定，容易出现outlier
> - **口诀**：查表的、归一化的、头尾不稳定的——保持FP16

### K181 AWQ核心原理？

> AWQ（Activation-Aware Weight Quantization）：**量化前保护**。跑校准数据统计每通道激活值→重要通道的权重提前乘scale放大→量化时相对误差变小→推理时÷s校正回来。
> **类比例子**：重要的人用放大镜看（放大→量化误差比例减小→复原），其他正常量化。
> **特点**：无需反向传播，量化速度快（9B模型~5分钟），质量优于GPTQ约+0.5%

### K182 GPTQ核心原理？

> GPTQ：**量化后补偿**。逐行量化权重→算Hessian矩阵=X^T·X→量化误差通过调整同行剩余权重补偿。
> **类比例子**：捏橡皮泥——w1被捏小了一块(量化损失δ)，从w2/w3/w4上挤一点补回来。
> **vs AWQ**：AWQ=事前保护，GPTQ=事后补偿。两者互补，AWQ质量略好且更快

### K183 数据蒸馏 vs 传统KL蒸馏？

> **传统KL蒸馏（BERT时代/已淘汰）**：教师学生同时跑→学生模仿教师softmax分布(KL散度)→需要真实标签+软标签→慢且LLM场景差
> **数据蒸馏（LLM时代主流）**：教师模型单独生成文本(API调用)→存为数据集→用SFT微调学生模型。和普通SFT流程完全一样。
> **一句话**：现在工业界的"蒸馏"=用GPT/Claude等强模型造数据+SFT微调小模型。DeepSeek/Qwen的蒸馏标注都是这意思

### K184 FP8 E4M3 vs E5M2？

> E4M3(权重+激活)：4位指数+3位尾数→精度优先→范围±448→像"精简版FP16"
> E5M2(梯度+KV Cache)：5位指数+2位尾数→范围优先→范围±57344→像"精简版BF16"
> **口诀**：E4M3像FP16(精)，E5M2像BF16(广)。权重存值用精，梯度防崩用广

### K185 不同场景怎么选压缩方案？

> | 场景 | 方案 | 理由 |
> |------|------|------|
> | H100生产部署 | FP8(vLLM) | 几乎无损+速度翻倍 |
> | RTX4090本地 | AWQ INT4 | 省显存，质量损失<2% |
> | 想用小模型 | 数据蒸馏(SFT) | 大模型造数据→微调小模型 |
> | 无GPU纯CPU | GGUF Q4_K_M | llama.cpp本地推理 |
> | 极端压缩 | 量化+蒸馏 | 两者互不冲突可叠加 |
> | 剪枝 | ❌ 不推荐 | LLM涌现能力对参数减少敏感 |

### K186 BERT/GPT/XLNet三架构对比？双向理解+自回归生成如何兼得？

> BERT（Encoder-only/MLM）：双向注意→看整句→完形填空预测被遮词→擅长理解，不擅长生成
> GPT（Decoder-only/CLM）：因果掩码→只看左边→自回归预测下一个词→擅长生成，不擅长双向理解
> XLNet（Permutation LM）：**词位置不动，随机打乱预测顺序**。表面上做自回归生成(GPT框架)，实质上每个词被预测时能看到前后文(BERT效果)→双向理解+生成能力兼得
> **核心**：打乱的是"预测顺序"不是"词的位置"。类比：桌上一张纸写着4个字不动，但算法决定先看第3个再回头看第1个

### K187 CSA和HCA的关系？DeepSeek-V4的混合注意力怎么配合？

> CSA（压缩稀疏注意力）：把每m个token压缩成一条再稀疏选512条细看 + 滑动窗口保局部依赖
> HCA（重度压缩注意力）：更高压缩比（每128个token捆成一捆），扫全局大局
> **关系**：两者互补——CSA细看关键处、HCA扫大局、滑动窗口保临近细节。三者配合让1M上下文跑得动
> 正确答案：A（CSA处理局部细节，HCA扫全局大局，互补）

### K188 量化粒度 per-tensor/per-channel/per-group 区别？

> | 粒度 | 分组方式 | 精度 | 速度 |
> |------|---------|------|------|
> | per-tensor | 整个矩阵共享1组量化参数 | 最差 | 最快 |
> | per-channel | 每行共享1组 | 中等 | 中等 |
> | per-group(128) | 每128个权重共享1组 | 最好 | 略慢 |
> **一句话**：越细越准但越慢。AWQ/GPTQ默认per-group(128)

### K189 为什么模型越大，量化损失越小？

> 大模型有更多**冗余参数**——单个权重的轻微扰动被其他参数分担了，对最终输出影响被稀释。小模型参数紧张，每个都"各司其职"，量化误差集中打击。
> **例**：397B模型INT4损失-0.5%，9B模型INT4损失-1.5%
> 口诀："胖子的赘肉减一点看不出来，瘦子的肌肉不能碰"

### K190 AWQ为什么要对重要通道乘放大系数s再量化？

> ① **为什么放大**：重要通道与高激活值相乘，权重误差被激活值放大→对输出影响大。直接量化→精度损失集中在重要通道。
> ② **放大作用**：乘s(s>1)后数值范围变大→相同量化步长下，相对误差（步长/权重幅值）变小→重要通道精度被保护。
> ③ **推理恢复**：对应输入激活值÷s，保证(权重×s)×(激活÷s)=权重×激活，数学完全等价，无损。
> ④ **直觉**："保重点、放次要"——把量化误差从重要通道转移到次要通道。

### K191 推理两阶段 Prefill vs Decode 区别？

> | | Prefill | Decode |
> |------|---------|--------|
> | 做什么 | 一次性算全部Token的QKV，建KV Cache | 逐Token生成，只算新Token的Q |
> | GPU看什么 | 计算密集→**算力**(Tensor Core) | 带宽密集→**显存带宽** |
> **类比**：Prefill=读题通盘思考，Decode=逐字写答案

### K192 KV Cache 跟哪些因素有关？

> **相关**：层数、隐藏维度、上下文长度。公式：KV Cache = 2×Layers×SeqLen×HiddenSize×Bytes
> **不相关**：模型参数量。KV Cache只存K/V，不存权重。
> **长上下文吃显存**：SeqLen翻倍→KV Cache翻倍

### K193 GQA（分组查询注意力）一句话原理？

> 多个Query Head共享同一组Key和Value。MHA=32Q+32K+32V，GQA=32Q+8K+8V。
> KV Cache减少4倍→推理更快显存更省。Llama3/Qwen3.5/DeepSeek/Gemma都在用

### K194 PagedAttention 核心思想？

> KV Cache**分页管理**——切成Page，页表记录每个请求用哪些Page。
> **类比**：KV Cache版虚拟内存。解决连续存储碎片多利用率低的问题，支持高并发

### K195 ZeRO-1/2/3 三级区别？

> | 级别 | 拆分内容 | 记忆口诀 |
> |------|---------|---------|
> | ZeRO-1 | Optimizer State | P完整 G完整 O拆分 |
> | ZeRO-2 | Optimizer + Gradient | P完整 G拆分 O拆分 |
> | ZeRO-3 | Optimizer + Gradient + Parameter | P拆分 G拆分 O拆分（最强）|

### K196 训练卡 vs 推理卡？显卡三大指标？

> | | 推理卡(4090) | 训练卡(A100/H100) |
> |------|------|------|
> | 特点 | 算力强/价格低/显存小 | 显存大/带宽高/NVLink |
> | 适合 | 部署/Agent/LoRA | 全参训练/高并发 |
> **三大指标口诀**：容量→能跑多大模型 / 算力→训练多快(Prefill) / 带宽→生成多快(Decode)


### K197 LoRA低秩原理？为什么ΔW=B×A有效？

> **秩**=矩阵中有效独立信息的数量。10000个格子但秩=8→只有8个独立方向，其余是冗余。
> LoRA假设微调时ΔW是低秩的(r=8)，分解为B(1024×8)×A(8×1024)——两个秩最多8的小矩阵乘起来=大矩阵最核心的8维变化。
> **类比**：公司1000人真正出主意的只有8人。满秩=重装全房每面墙，低秩=只调8根承重柱。
> 参数节省：(1024×8)×2 / (1024×1024) ≈ 1/64，省256倍（r=8时）

### K198 MLA vs MHA vs GQA 三种注意力区别？

> | | MHA | GQA | MLA(DeepSeek) |
> |------|-----|-----|------|
> | KV数量 | Q=K=V=32头 | Q=32, K=V=8(共享) | K/V压到极低维潜在向量 |
> | 思路 | 标准多头 | 多Q共享KV | 压缩KV本身 |
> | KV Cache | 大 | 省4倍 | 极致省(远小于GQA) |
> | 代表 | 原始Transformer | Qwen3.5, GLM-5.2, Llama3 | DeepSeek-V4 |
> **一句话**：GQA是共享KV头，MLA是压缩KV向量——前者"合本子"，后者"缩印"

### K199 Fine-grained MoE vs Hierarchical MoE 两条路线？

> **Fine-grained(DeepSeek)**：64大专家→256小专家+共享专家。解决"专家太粗、知识共享不足"
> **Hierarchical(GLM-5.2)**：先选组再选专家，两层路由。解决"专家太多、路由计算太贵"
> **为什么DeepSeek不选Hierarchical**：后来发现GPU通信和负载均衡才是瓶颈，不是Router打分
> **类比**：Fine-grained=大部门拆成专业小组，Hierarchical=先选学院再选导师

### K200 RoPE为什么天然感知相对位置？

> 普通Attention：Q·K^T（无位置信息）
> RoPE：(R_m·Q)·(R_n·K)^T，展开后=Q^T·R_(m-n)·K
> **关键**：绝对位置m和n消失了，只剩m-n。位置10和11→差1，位置100和101→也是差1→结果相同！
> **本质**：RoPE还是sin/cos，只是不构造向量加输入，而构造旋转角度去旋转Q/K→内积自带相对距离
> 长文本优势：旋转角度可以无限转，不像可学习PE超长就崩

### K201 MTP（多Token预测）是什么？

> MTP=Multi-Token Prediction。不只预测t+1，同时预测t+2、t+3。
> 训练时：所有预测头都算loss→增强全局规划能力
> 推理时：辅助头用于**投机解码**(Speculative Decoding)→一次生成多个候选→验证→加速2-3倍
> **谁在用**：DeepSeek-V4、Qwen3.7
> **口诀**："不只猜下一个，提前多想两步"

### K202 位置编码演化线？

> Transformer(2017)：Sin/Cos绝对位置→加到输入Embedding
> GPT-2(2019)：可学习位置表→好处灵活/问题长度锁死
> LLaMA/Qwen/DeepSeek(2023+)：RoPE→旋转Q/K→天然感知相对位置
> 最新(2025+)：RoPE+YaRN/NTK→长上下文扩展
> **趋势**：绝对→相对；加到输入→嵌入Attention计算；固定→可外推


| 日期 | 操作 | 说明 |
|------|------|------|
### K203 LLaMA Factory vs Unsloth 区别？

> | | LLaMA Factory | Unsloth |
> |------|------|------|
> | 优势 | 通用性好、多卡/多硬件(AMD/华为)、WebUI零代码 | 手写算子优化、2x速度、省50%显存、代码极简 |
> | 适合 | 多卡分布式、不会代码的用户 | 单卡极致效率 |
> | 场景 | 生产级多卡训练 | 个人/实验快速微调 |
> | 底层 | 都依赖 HuggingFace PEFT 库 |

### K204 DeepSpeed ZeRO 选型策略？

> **原则**：单卡放得下 → DDP(ZeRO-0)；单卡不够 → 逐级升级
> | 方案 | 何时选 | 原因 |
> |------|--------|------|
> | DDP(ZeRO-0) | 单卡显存够 | 不切分无需跨卡通讯，效率最高 |
> | ZeRO-1 | 优化器状态太吃显存 | 只切O，通讯开销小/性价比最高 |
> | ZeRO-2 | ZeRO-1还不够 | 切O+G |
> | ZeRO-3 | 模型权重也放不下 | 全切省最多但通讯最高，非首选 |
> **口诀**："单卡够→DDP，不够→从1到3逐级升，不跳级"

### K205 train_on_responses_only 作用？

> 指令微调时只对 assistant 回答部分计算 loss，mask 掉 system/user 部分。
> **为什么**：防止模型学习"如何提问"——如果连用户输入也算loss，模型会模仿用户说话而不是学习回答。让 loss 只打在模型生成的回答上。
> **口诀**："模型只学回答不学提问"

### K206 单卡24GB微调Qwen3.6-27B选什么方案？

> BF16权重≈56GB。全参：56GB+梯度+优化器>>24GB ❌
> LoRA：仍需加载完整56GB权重→OOM ❌
> QLoRA：4bit压缩≈15GB，唯一单卡可行方案 ✅
> **判断流程**：算模型BF16→全参/全量≈×6~8→LoRA看看BF16能不能放进显存→放不进就QLoRA。


| 日期 | 操作 | 说明 |
|------|------|------|
| 2026-06-03 | 创建 | 提取 Knowledge_base 32篇~140考点 + share_know 6篇18考点 |
| — | 待办 | 提取 Knowledge_base 3个PDF（需PDF工具） |
