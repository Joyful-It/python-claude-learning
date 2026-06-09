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

## 📝 维护日志

| 日期 | 操作 | 说明 |
|------|------|------|
| 2026-06-03 | 创建 | 提取 Knowledge_base 32篇~140考点 + share_know 6篇18考点 |
| — | 待办 | 提取 Knowledge_base 3个PDF（需PDF工具） |
