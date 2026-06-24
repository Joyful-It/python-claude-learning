# Python 学习进度追踪表

> **最后更新日期**：2026-06-23

---

## 快速统计

| 指标 | 数值 |
|-----|------|
| 总考点数 | 52 (+3 前端) |
| 已掌握考点（≥80%） | 8 |
| 学习中考点（1%-79%） | 18 |
| 未开始考点（0%） | 19 |
| **整体进度** | **38%** |
| **学习天数** | **45天** |
| **里程碑** | **知识树+30天计划+模块一23题入库** |

---

## 当前作业

| 作业 | 分值 | 截止日期 | 状态 |
|-----|-----|---------|-----|
| Deep Learning Assignment | 100% | 已完成 | ✅ |
| 作业选择：BERT + BiLSTM 对比 | - | - | 已完成 |

---

## 掌握程度说明

| 百分比 | 等级 | 说明 |
|-------|------|------|
| 100% | ✅ 完全掌握 | 能独立完成相关练习，无需提示 |
| 80-99% | ✅ 基本掌握 | 能完成大部分练习，偶尔需要提示 |
| 60-79% | 🔶 初步掌握 | 理解概念，但实操需要引导 |
| 40-59% | ⚠️ 有所了解 | 知道是什么，但不熟练 |
| 1-39% | 📖 刚接触 | 刚开始学习，需要大量讲解 |
| 0% | ⬜ 未开始 | 尚未学习 |

---

---
 
 ## 学员愿望清单（2026-05-22 整理）

### 🔥 代码实操
| # | 任务 | 状态 |
|---|------|------|
| 1 | **独立重现泰坦尼克号 PyTorch**（`11traintest.py`）| ⬜ |
| 2 | 餐厅项目 `database.py`（SQLAlchemy）| ⬜ |
| 3 | PyTorch 手写 MNIST CNN | ⬜ |
| 4 | Seq2Seq + Attention 代码实操 | ⬜ |
| 5 | `5_12.py`：class_weight + GridSearchCV 提升 recall | ⬜ |
| 6 | Matplotlib / Seaborn 系统学 | ⬜ |

### 📖 论文阅读
| # | 论文 | 状态 |
|---|------|------|
| 7 | 精读 DeepSeek 论文 | ⬜ |
| 8 | Attention Is All You Need | ⬜ |
| 9 | CLIP 原论文 | ⬜ |
| 10 | 另 7 篇待定 | ⬜ |

### 🧠 理论深入
| # | 任务 | 状态 |
|---|------|------|
| 11 | 手推深度学习核心公式（反向传播/BPTT）| ⬜ |
| 12 | 系统复习前面所有知识 | ⬜ |
| 13 | CNN 深入（池化/步长/padding/感受野）| ⬜ |
| 14 | 函数四种参数形式复习 | ✅ |
| 15 | 循环结构深入（while/for）| ✅ |

---
 
## 模块进度总表

| 模块 | 权重 | 考点数 | 已掌握 | 学习中 | 未开始 | 进度 |
|------|------|-------|-------|-------|-------|------|
| A. Python 工程化基础 | 20% | 9 | 0 | 5 | 4 | 38% |
| B. 大模型推理工程与RAG开发 | 18% | 6 | 0 | 3 | 3 | 32% |
| C. Agent智能体开发 | 16% | 5 | 0 | 4 | 1 | 52% |
| D. 大模型微调实战 | 15% | 5 | 0 | 3 | 2 | 28% |
| E. 高性能推理部署与LLMOps | 14% | 5 | 0 | 3 | 2 | 30% |
| F. 机器学习/深度学习基础 | 10% | 22 | 0 | 5 | 17 | 52% |
| G. 工具链与辅助开发 | 7% | 3 | 0 | 1 | 2 | 25% |
| H. 编程规范与工程实践 | 0% | 2 | 0 | 1 | 1 | 50% |
| I. 前端开发基础 | 0% | 3 | 0 | 2 | 1 | 30% |

---

## 已掌握考点（≥80%）

> 暂无已掌握考点

---

## 学习中考点（1%-79%）

### A.1 Python 基础语法（变量/数据类型/分支循环/函数/面向对象）
| 子考点 | 掌握度 | 更新日期 | 备注 |
|-------|-------|---------|------|
| 变量与数据类型 | 30% | 2026-03-30 | 有其他语言基础，待验证 |
| 分支结构（if/elif/else） | 25% | 2026-03-30 | 已学，待验证 |
| 逻辑运算符（and/or/not） | 60% | 2026-03-30 | 知道与C语言的差异 |
| 循环结构（while/for） | 50% | 2026-06-01 | for/while基础掌握，独立完成三道练习，Python for≠C for三段式 |
| 函数定义与调用 | 25% | 2026-03-30 | 有初步认知 |
| 函数参数（四种形式） | 70% | 2026-06-01 | 四种名称+顺序+独立写出，*args后变keyword-only理解 |
| 类与对象概念 | 60% | 2026-03-31 | 理解类=模板，对象=实例，内存中独立存储 |
| __init__ 初始化方法 | 55% | 2026-03-31 | 理解初始化，创建对象时自动执行 |
| self 的含义 | 50% | 2026-03-31 | 理解是形参+指针，指向当前对象 |
| 属性与方法 | 55% | 2026-03-31 | 能区分并正确定义 |
| 方法定义和调用 | 50% | 2026-03-31 | 理解方法调用，Python自动传self |
| 继承 | 55% | 2026-03-31 | 理解子类继承父类属性和方法 |
| 重写（Override） | 45% | 2026-03-31 | 子类可覆盖父类方法 |
| super() | 50% | 2026-03-31 | 调用父类方法 |
| 封装（私有属性） | 50% | 2026-03-31 | 理解__xxx私有属性，改名机制 |
| 字符串处理 strip/split/join | 80% | 2026-06-10 | 学员独立拆解"三strip流水线"（整体→拆分→过滤→清理），split/join互为反操作 |
| Python 三种括号体系 | 75% | 2026-06-10 | 学员自制速查表：()=执行/[]=容器/{}=映射，外圆内方口诀 |
| get/set 方法 | 55% | 2026-03-31 | 能独立写get_age/set_age |
| 多态 | 40% | 2026-03-31 | 有点模糊，需巩固 |
| __str__ 方法 | 60% | 2026-05-12 | 复习后完全理解：print 时自动触发，自定义输出 |
| 函数返回值（return） | 50% | 2026-06-01 | print(显示) vs return(交付)区分清楚，默认返回None，return是函数终止点 |
| 变量作用域 | 45% | 2026-06-01 | 局部变量隔离理解，global打破隔离，global一般不推荐用 |

**A.1 综合掌握度：52%**（06-15 重算：函数参数/面向对象/字符串处理已稳固，class_weight巩固）

---

### C.16 Function Calling / Agent 开发（LangChain）
| 子考点 | 掌握度 | 更新日期 | 备注 |
|-------|-------|---------|------|
| LangChain 三大核心模块 | 75% | 2026-06-03 | Model(invoke/stream/batch)+Tools(@tool)+Agent(create_agent)，经消息流复习后加深 |
| ReAct 循环机制 | 70% | 2026-06-03 | 消息流四步=ReAct底层实现，T→A→O→T = ①HumanMsg→②AIMsg.tool_calls→③ToolMsg→④AIMsg |
| @tool 装饰器 | 65% | 2026-06-02 | 文档注释给模型看，#注释模型读不到 |
| Agent vs 直接调 API | 60% | 2026-06-03 | Agent=自主决策调工具(Middleware不可见)，API=只生成文本 |
| Middleware 中间件 | 70% | 2026-06-04 | 洋葱模型+6钩子+10内置，实战踩坑6个全修复（参数依赖/过滤/thread_id） |
| Agent 完整搭建 | 65% | 2026-06-04 | 独立完成差旅Agent（2tool+3middleware+memory+流式交互），导入→工具→模型→中间件→记忆→Agent→交互 |
| 消息流转 | 75% | 2026-06-04 | content=""=操作工具不说话，四步口诀"问→空壳调→工具返→最终答" |
| Supervisor 多Agent | 50% | 2026-06-03 | 本质=拆开注意力不分散，Supervisor只分派不干活，可嵌套 |
| LangGraph StateGraph | 70% | 2026-06-08 | State(数据说明书)/Node(干活)/Edge(流程)三要素，compile→invoke |
| LangGraph ToolNode | 75% | 2026-06-08 | Tool=普通函数不知State，ToolNode=帮Agent执行工具，手动llm.invoke不需ToolNode |
| LLM vs Tool 区分 | 80% | 2026-06-08 | LLM=大脑(思考生成)，Tool=手脚(执行动作)，金句自创 |
| Human-in-the-Loop (HITL) | 85% | 2026-06-09 | interrupt(暂停抛数据)+MemorySaver(记忆保存)+Command(resume)(送回继续)，七步全流程自拆解 |
| MemorySaver 与 thread_id | 80% | 2026-06-09 | MemorySaver=多槽位记忆库，thread_id=任务编号，保证暂停后找回状态 |
| 条件边 (Conditional Edge) | 75% | 2026-06-09 | route 返回 str 决定下一站，add_conditional_edges(source, route, path_map) |
| AutoGPT Think-Act 循环 | 75% | 2026-06-10 | Think(LLM拆解)→Act(执行首条)→Route(判断)→循环/结束，8bug全修通 |
| Python import 路径机制 | 70% | 2026-06-10 | sys.path + __file__绝对路径 vs '..'相对工作目录 |
| Node/Route 返回规则 | 85% | 2026-06-10 | Node→dict(更新State)，Route→str(下一站节点名)，手误3次后刻在手上 |
| AutoGPT vs BabyAGI | 75% | 2026-06-11 | AutoGPT每次重新生成任务列表，BabyAGI只重排优先级(reprioritize) |
| MCP 协议三种传输模式 | 65% | 2026-06-11 | stdio/SSE/Streamable HTTP；传输与协议分离；FastMCP高阶封装 |
| 多Agent三种模式 | 60% | 2026-06-11 | Sequential(流水线)/Hierarchical(主管)/Collaborative(辩论)，区别+适用场景 |
| Fan-out / Fan-in | 65% | 2026-06-12 | Fan-out=一个节点指向多个(并行分发)；Fan-in=多个汇聚等待全部完成 |
| Tool vs Agent 核心区分 | 80% | 2026-06-12 | Tool=菜刀(可调模型但不决策)，Agent=厨师(有决策权)，多Agent=分部门 |
| 多Agent vs 单Agent+多工具 | 70% | 2026-06-12 | 选择空间缩小(大海捞针→两次小范围筛选)、Prompt精简、上层兜底纠错 |

**C.16 综合掌握度：70%**（06-15 重算：HITL/MemorySaver/NodeRoute已≥80%，AutoGPT/MCP/多Agent/Fan-out概念均已覆盖）

---

### B.14 RAG 概念（检索增强生成）
| 子考点 | 掌握度 | 更新日期 | 备注 |
|-------|-------|---------|------|
| RAG 核心概念 | 80% | 2026-06-05 | R=检索/A=增强/G=生成，六站管道完整理解 |
| RAG vs 微调 | 65% | 2026-06-14 | RAG翻书(外挂秒级更新)、微调背书(训练权重)，区别清晰 |
| RAG 完整流程 | 80% | 2026-06-14 | PDF→加载→切块→向量化→存库；提问→问题向量化→检索→拼Prompt→LLM生成 |
| Harness vs RAG | 25% | 2026-06-02 | RAG ⊂ Harness，Harness 是全链路工程体系 |
| Document 对象 | 80% | 2026-06-05 | page_content(内容)+metadata(身份证) 双件套 |
| 文本分块 RecursiveCharSplit | 75% | 2026-06-05 | 递归分隔符层级(段落→行→句→词→字符)，chunk_size+chunk_overlap |
| Embedding 三路线 | 65% | 2026-06-05 | ①云端API(智谱) ②Ollama本地(bge-m3) ③HF直载(bge-small)；Chroma≠Embedding |
| 向量库 Chroma | 60% | 2026-06-05 | 轻量级本地向量库，cos相似度检索，和Transformer自注意力同原理 |
| 基础 RAG 检索链 | 70% | 2026-06-05 | retrieve→拼Prompt→LLM生成 三步，防幻觉关键在Prompt |
| Agentic RAG | 60% | 2026-06-05 | Agent自主判断查不查，retriever包装为@tool |
| 混合检索/重排序 | 30% | 2026-06-05 | 向量+BM25混合，Cross-Encoder精排，概念速览未实操 |

**B.14 综合掌握度：42%**（RAG流程已稳固，vs微调区分清晰）

---

### A.6 数据处理（NumPy/Pandas/数据清洗与可视化）
| 子考点 | 掌握度 | 更新日期 | 备注 |
|-------|-------|---------|------|
| NumPy 创建数组 | 55% | 2026-04-01 | 已学 |
| NumPy 数组运算 | 55% | 2026-04-01 | 向量化运算 |
| NumPy reshape | 50% | 2026-04-01 | 已学 |
| NumPy flatten | 50% | 2026-04-02 | 新增：拍扁成一维 |
| NumPy 转置 .T | 50% | 2026-04-02 | 新增 |
| NumPy 数组属性 | 45% | 2026-04-01 | shape/ndim/size/dtype |
| NumPy 切片 | 50% | 2026-04-01 | 二维切片 |
| NumPy 排序 | 45% | 2026-04-01 | np.sort vs arr.sort |
| NumPy 搜索 | 20% | 2026-04-01 | 待巩固 |
| NumPy 矩阵运算 | 45% | 2026-04-02 | 逆矩阵、点积 |
| NumPy 统计函数 | 45% | 2026-04-02 | max/min/mean/std/median |
| NumPy 广播机制 | 55% | 2026-04-03 | 从右对齐，不够补1，深入理解一维vs二维 |
| Pandas 创建DataFrame | 80% | 2026-04-13 | 已学：pd.DataFrame({}) |
| Pandas 查看数据 | 85% | 2026-04-13 | info/describe/head |
| Pandas 缺失值处理 | 80% | 2026-05-23 | fillna/dropna/isnull + 数值填中位数/分类填众数/分组填充 |
| 数据清理标准流程 | 50% | 2026-05-23 | 四步：分家→扔掉→补缺→转数字 + 标准化必须切分后fit |
| Pandas 重复值处理 | 75% | 2026-04-13 | duplicated/drop_duplicates |
| Pandas 排序 | 75% | 2026-04-13 | sort_values/sort_index/rank |
| Pandas 类型转换 | 70% | 2026-04-13 | astype (需先fillna) |
| Pandas 批量处理 | 65% | 2026-04-13 | apply(lambda x: ...) |
| Pandas 字符串处理 | 70% | 2026-04-13 | str.replace() |
| Matplotlib | 0% | - | 明日学习 |
| Seaborn | 0% | - | 明日学习 |

**A.6 综合掌握度：35%**（Pandas大幅提升）

---

### B.1 大模型基础认知（新增）
| 子考点 | 掌握度 | 更新日期 | 备注 |
|-------|-------|---------|------|
| 梯度下降原理 | 55% | 2026-04-03 | 下降的是损失值（错误程度） |
| GPU vs CPU | 50% | 2026-04-02 | GPU核心多，适合矩阵乘法 |
| H100/A100/H800/A800 | 50% | 2026-04-03 | 封禁原因、区别 |
| RTX系列显卡 | 45% | 2026-04-03 | 性价比排序 |
| 神经网络层概念 | 50% | 2026-04-02 | 输入→矩阵乘法→输出 |
| 本地vs云端vs算力 | 55% | 2026-04-03 | 云服务器vs算力服务器 |
| PyTorch CPU模式 | 40% | 2026-04-03 | 学语法够用，Intel Arc不推荐 |
| 归一化 Normalization | 60% | 2026-04-27 | 均值≈0、方差≈1，让训练更稳定 |
| Layer Norm | 55% | 2026-04-27 | 单个词自己的512维向量归一化，Transformer专用 |
| Batch Norm | 50% | 2026-04-27 | 对整个批次同一维度归一化，不适合NLP |

**B.1 综合掌握度：35%**（新增归一化、Layer Norm/Batch Norm、DeepSeek API）

---

### B.10 大模型API调用（DeepSeek/OpenAI）
| 子考点 | 掌握度 | 更新日期 | 备注 |
|-------|-------|---------|------|
| OpenAI 库调用 DeepSeek | 65% | 2026-04-27 | openai库 + base_url |
| API Key 配置 | 60% | 2026-04-27 | 已成功调用 |
| temperature 参数 | 65% | 2026-04-27 | 控制随机程度 0-1 |
| max_tokens 参数 | 60% | 2026-04-27 | 控制回答字数 |
| 流式输出 stream | 55% | 2026-04-27 | 边回答边显示 |

**B.10 综合掌握度：65%**

---

### 用户电脑配置
| 硬件 | 型号 | 评价 |
|-----|------|------|
| CPU | Intel Ultra 5 125H（12核） | 不错 |
| 内存 | 32GB | 够用 |
| 显卡 | Intel Arc 集成核显 | 弱，不适合本地跑大模型 |
| 存储 | 1TB SSD | 够用 |

---

### A.8 后端开发（FastAPI深度使用/接口设计）
| 子考点 | 掌握度 | 更新日期 | 备注 |
|-------|-------|---------|------|
| requests.get | 50% | 2026-04-01 | 已学 |
| requests.post | 35% | 2026-04-01 | 已学 |
| status_code 状态码 | 45% | 2026-04-01 | 已学 |
| API 调用流程 | 30% | 2026-04-01 | 大模型API调用尝试，路径待确认 |
| response.json() | 50% | 2026-04-01 | 已学 |
| FastAPI 基础 | 65% | 2026-04-16 | @app.get/post、装饰器、三种参数 |
| Pydantic BaseModel | 60% | 2026-04-16 | 数据验证 vs 普通类 |
| 前后端分离架构 | 75% | 2026-04-16 | 完全理解 |
| Path/Query/Body参数 | 65% | 2026-04-16 | 已实操练习 |

**A.8 综合掌握度：20%**

---

### G.35 开发工具（dotenv/logging/配置文件管理）
| 子考点 | 掌握度 | 更新日期 | 备注 |
|-------|-------|---------|------|
| JSON 基础操作 | 55% | 2026-04-01 | dumps/loads |
| JSON 嵌套提取 | 55% | 2026-04-02 | 字典+列表逐层访问 |
| JSON 美化输出 | 45% | 2026-04-01 | indent/ensure_ascii |
| JSON 文件操作 | 30% | 2026-04-01 | dump/load（待巩固） |
| time 模块 | 40% | 2026-04-01 | sleep/time/strftime |
| random 模块 | 35% | 2026-04-01 | 已学 |
| Pydantic 基础 | 20% | 2026-04-01 | 了解概念 |
| import 导入模块 | 40% | 2026-04-01 | import/from...import |

**G.35 综合掌握度：25%**

---

### I. 前端开发基础（HTML/CSS/JavaScript）
| 子考点 | 掌握度 | 更新日期 | 备注 |
|-------|-------|---------|------|
| HTML 基础标签 | 60% | 2026-04-21 | h/div/a/img/table/form/input/select/button |
| HTML 表格结构 | 55% | 2026-04-21 | thead/tbody/tr/th/td |
| HTML 表单标签 | 60% | 2026-04-21 | text/password/radio/checkbox/file/textarea |
| CSS 选择器 | 50% | 2026-04-21 | 标签/id/class选择器 |
| CSS 常用属性 | 45% | 2026-04-21 | margin/padding/width/height/color |
| CSS 三种使用方式 | 50% | 2026-04-21 | style标签/style属性/link导入 |
| JavaScript 变量/常量 | 55% | 2026-04-21 | let/const/数据类型 |
| JavaScript 运算符 | 50% | 2026-04-21 | 算术/赋值/比较/逻辑 |
| JavaScript 分支循环 | 50% | 2026-04-21 | if/for |
| JavaScript 函数 | 45% | 2026-04-21 | function/return |

**I 综合掌握度：30%**

---

### H.39 Git 版本控制（已学习）
| 子考点 | 掌握度 | 更新日期 | 备注 |
|-------|-------|---------|------|
| Git 基础操作 | 60% | 2026-04-25 | clone/add/commit/push/pull |
| Git 分支操作 | 55% | 2026-04-25 | branch/switch/merge |
| Git 远程仓库 | 50% | 2026-04-25 | remote set-url/add |
| Git 状态查看 | 60% | 2026-04-25 | status/diff/log |

**H.39 综合掌握度：60%**

---

### F. 机器学习/深度学习基础（新增）
| 子考点 | 掌握度 | 更新日期 | 备注 |
|-------|-------|---------|------|
| 神经网络识别原理 | 55% | 2026-05-18 | 隐藏层层级抽象(边→部件→完整)，自然涌现非预设 |
| 神经元计算 (z=wx+b, a=σ(z)) | 50% | 2026-05-18 | 区分z(线性结果)和a(激活后)，反向链穿过5步 |
| Sigmoid 激活函数 | 40% | 2026-05-18 | 压缩0-1，σ'(z)在反向时压梯度 |
| 偏置 b 的作用 | 25% | 2026-04-28 | 调整激活门槛 |
| 权重初始化 | 20% | 2026-04-28 | 随机初始化，不能全为0 |
| 反向传播 | 60% | 2026-05-18 | 链式法则手工计算 ∂L/∂w₁=28×4×2=224，穿过w₂ |
| 训练循环五步 | 75% | 2026-06-01 | 口诀"前损后步清"稳定，今日热身一遍过 |
| DL属wx+b派 | 70% | 2026-05-18 | X@W+b堆叠+梯度下降更新 |
| CNN 卷积核机制 | 55% | 2026-05-19 | in/out channels、参数计算(3×3×1+1)×16=160、并行滑动、分工涌现 |
| PyTorch 五块模板 | 50% | 2026-05-19 | 数据→DataLoader→模型→配置→训练循环，哪些变哪些不变 |
| 泰坦尼克号完整流程 | 60% | 2026-05-24 | 十步清单可背出，进阶版(分组填Age/Has_Cabin/衍生特征/正确标准化顺序)，逐行注释版 |
| PyTorch import 规范 | 45% | 2026-05-24 | 三件套必写(torch/nn/Dataset+DataLoader)，sklearn可手写替代 |
| torch.nn 边界 | 40% | 2026-05-24 | nn只有基础积木(Linear/Conv/LSTM)，完整模型在外部库(torchvision/transformers/ultralytics) |
| Transformer 自注意力 | 70% | 2026-06-09 | QKV三投影手写实现 (4,512)→(4,64)，形状变换卡已通，下一步attn_scores=Q@K^T/√dk |
| softmax 三步骤 + √dₖ | 85% | 2026-06-12 | 手算全链打通：eˣ→求和→÷，dₖ大→点积飙升→softmax变独热→梯度消失，除√dₖ拉回 |
| Transformer Attention 六步 | 75% | 2026-06-12 | QKV投影→Q@Kᵀ→÷√dₖ→softmax→×V→输出，Q@Kᵀ矩阵含义已通 |
| Tensor ↔ NumPy 共享内存 | 55% | 2026-06-12 | torch.from_numpy()默认共享，改一个变两个，.clone()分家 |
| KV Cache | 40% | 2026-06-12 | 自回归时不重算历史K/V，O(n²)→O(n)；Pre-LN vs Post-LN顺序 |
| Transformer 架构组件 | 50% | 2026-06-09 | 手搓启动——编码/解码掩码、位置编码、FFN(先升后降)、残差+LN、Pre-LN vs Post-LN，QKV命名纠正(W_K/W_V) |
| Transformer vs RNN | 50% | 2026-05-25 | 并行/长程直连/扩展快 三优势，RNN流式/线性 互补 |
| 梯度概念全家桶 | 55% | 2026-05-25 | 梯度定义/正负/消失(连乘→0)/爆炸(连乘→∞)/累积(loss/acc) |
| GPU与大模型 | 40% | 2026-05-25 | 显存/算力/带宽，训练=推理×4，量化/梯度累积/模型并行 |
| ML→DL数学链 | 50% | 2026-05-25 | 线性→逻辑→多层→CNN→RNN→Transformer，全是wx+b变体 |
| HuggingFace Tokenizer | 45% | 2026-05-26 | 四步流程(标准化→预分词→模型分词→后处理)，三参数三输出字段 |
| HuggingFace Pipeline | 40% | 2026-05-26 | 三阶段(Tokenizer→Model→Postprocess)，4个标准任务名 |
| HuggingFace 五大组件 | 40% | 2026-05-26 | Transformers/Datasets/Evaluate/Accelerate/Hub |
| 词嵌入演进 | 45% | 2026-05-26 | 静态(Word2Vec)→动态(BERT)，一词多义靠上下文 |
| 注意力本质 | 50% | 2026-05-26 | Q查K取V，动态信息筛选，解决长程遗忘+信息瓶颈 |
| 知识蒸馏 | 40% | 2026-05-26 | 老师-学生框架、软标签vs硬标签、温度T、双损失(KL+CE) |
| Scaling Law 与涌现 | 60% | 2026-06-10 | 涌现派(Google2022阈值跳升)vs质疑派(评测方式造成假象)；GPT-2→3→4三代跃迁；Scale=必要非充分 |
| GELU vs ReLU | 45% | 2026-05-26 | ReLU一刀切负数全杀，GELU平滑概率留余地，原论文ReLU但BERT后改GELU |
| 学习率预热 Warmup | 45% | 2026-05-26 | lr本质=步伐，预热=开局低速爬坡防崩，lr过大≠梯度爆炸 |
| IMDB 情感分析项目 | 70% | 2026-06-01 | 骨架六步完成+三处改进(fp16/F1指标/tokenizer保存)+compute_metrics结构理解+注释版完整 |
| HuggingFace Trainer API | 55% | 2026-06-02 | processing_class(新版)替代tokenizer(已弃用)，查GitHub #37734确认，多模态演进所致 |
| 大模型显存评估 | 55% | 2026-06-01 | 推理公式(B×字节×1.2)、FP16/INT8/INT4精度对比口诀、训练≈推理×4、LoRA/QLoRA显存对比、fp16=训练提速/INT8=推理瘦身不能混用 |
| LoRA 低秩微调 | 65% | 2026-05-27 | ΔW=B×A、省256倍、乘≠训(前向读/反向不改)、A/B初始化(A随机B零)、矩阵维度由输入列决定 |
| C盘清理+环境管理 | 70% | 2026-05-30 | conda/pip/venv区分、软链接mklink、多环境隔离、Python313统一到Conda D盘 |
| GRPO/DeepSeek R1 | 50% | 2026-05-27 | PPO省Critic+人工标注，16条同模型回答，规则奖励+组平均=基线，Advantage=自己-平均 |
| 残差连接 | 60% | 2026-05-28 | y=F(x)+x，+1保底梯度不消失，正向无损传输，Transformer堆深全靠它 |
| LayerNorm | 60% | 2026-05-28 | 拉回均值0方差1防数值失控，先残差再加Norm（保证残差加的是原样信息） |
| Transformer 全流程 | 55% | 2026-05-28 | Embedding→位置编码→Encoder(自注意力+残差+Norm+FFN)×N→Decoder(掩码自注意力+交叉注意力+FFN)×N→预测 |
| 自注意力 vs 交叉注意力 | 55% | 2026-05-28 | 自注意力QKV全来自同一层，交叉注意力Q来自Decoder/KV来自Encoder |
| YOLO 实时检测 | 50% | 2026-05-19 | 5步骨架：加载模型→开摄像头→循环读帧→检测→显示 |
| OpenCV 基础 | 45% | 2026-05-19 | 读图/显示/人脸检测/裁剪/画框/写字/截图/摄像头 |
| 试卷知识点 | 60% | 2026-05-19 | 10选择+4简答 全部理解 |
| RNN 循环神经网络 | 55% | 2026-05-19 | h_t=tanh(x@W_x+h@W_h+b)，比全连接多一项，参数跨时刻共享 |
| LSTM 三门机制 | 50% | 2026-05-19 | 遗忘/输入/输出门公式+分工，C_t长期vs h_t短期，sigmoid门vs tanh候选 |
| GRU | 30% | 2026-05-19 | 2门(重置+更新)+1状态，LSTM简化版 |
| 双向RNN (BiRNN) | 40% | 2026-05-22 | 正反向拼接，FC输入维度×2，NER/情感分析/翻译标配 |
| RNN vs Transformer对比 | 35% | 2026-05-22 | 非替代是互补(O(n) vs O(n²)，流式 vs 并行，常混合使用) |
| RNN/LSTM工程实践 | 30% | 2026-05-22 | 6条：词表填充、Embedding→RNN→Dropout→FC、梯度裁剪、Adam、内存三招 |
| CLIP 多模态模型 | 40% | 2026-05-22 | 双塔架构(图像+文本编码器)、对比学习(InfoNCE)、零样本推理、乐高式语义组合 |
| θ=w 统一理解 | 75% | 2026-05-17 | θ就是权重w——贝叶斯算的、梯度找的、正则约束的，同一个东西 |
| 贝叶斯→正则化推导链 | 65% | 2026-05-17 | -log p(X\|w)=MSE, -log p(w)=L2/L1, MAP=Ridge |
| ML模型五派分类 | 70% | 2026-05-17 | wx+b派/树派/距离派/概率派/边界派，按计算方式分类 |
| Ridge vs BayesianRidge | 65% | 2026-05-17 | 点估计vs分布+置信度，工业用前者（快），医疗/金融用后者 |
| 梯度下降学习率作用 | 65% | 2026-05-17 | 梯度=方向，lr=步长，最好w一步步走，不是求导直接得到 |
| 决策树切分原理 | 50% | 2026-05-17 | 贪心搜索所有切分点，不求导，用Gini/MSE量纯度 |
| ML标准五步框架 | 70% | 2026-05-17 | 选模型→损失→正则化→优化→评估，能独立写代码 |
| sklearn ML流程 | 65% | 2026-05-17 | 五步模板独立写出并跑通（Ridge+LogisticRegression双示例） |
| 机器学习 vs 深度学习 | 30% | 2026-04-28 | 机器学习人工设计特征，深度学习自动学 |
| 卷积原理 | 25% | 2026-04-28 | 小窗口滑动检测局部特征 |
| CNN 卷积神经网络 | 25% | 2026-04-28 | 卷积层+激活+池化+全连接 |
| sklearn ML流程 | 60% | 2026-05-10 | 能裸写骨架，导入/fit参数偶尔出错 |
| 逻辑回归（sklearn） | 65% | 2026-05-10 | 红酒数据集独立跑通，准确率 1.0 |
| sklearn 子模块导入 | 50% | 2026-05-10 | 掌握命名规律（线/树/邻/贝/SVM=基础五件套） |
| 决策树（sklearn） | 40% | 2026-05-09 | DecisionTreeClassifier 已跑通 |
| 朴素贝叶斯 | 40% | 2026-05-09 | GaussianNB/Bernoulli/Multinomial/Complement 了解区别 |
| KNN | 45% | 2026-05-09 | KNeighborsClassifier + 手动调参 + 画曲线 |
| random_state | 50% | 2026-05-09 | 固定随机种子，可复现 |
| StandardScaler | 55% | 2026-05-10 | fit_transform vs transform，知道哪些模型需要标准化 |
| 手动调参（for循环） | 40% | 2026-05-09 | 遍历K值找最优 |
| matplotlib 画图 | 25% | 2026-05-09 | plot/xlabel/ylabel/title/show，中文乱码需SimHei |
| make_classification | 30% | 2026-05-09 | 造分类数据做实验 |
| 集成学习（Bagging/Boosting/Stacking） | 50% | 2026-05-12 | 概念三招已通，StackingClassifier 代码已写 |
| PCA 降维 | 50% | 2026-05-11 | 原理推导已理解，代码已看 |
| t-SNE 降维 | 45% | 2026-05-11 | 原理推导已理解，与 PCA 区别清楚 |
| 分类指标（Accuracy/Recall/Precision/F1） | 60% | 2026-05-12 | 能用自己的话解释四指标，知道 Recall 和 Precision 不能同时高 |
| class_weight 不平衡处理 | 50% | 2026-05-12 | 理解原理（少数类权重更高），试了 balanced |

**F 模块综合掌握度：45%**（新增 MLM/CLM/Decoder-only/GDN/MoE/BBPE/GLM架构等概念）

---

## 知识漏洞追踪（需针对性复习）

| 考点编号 | 漏洞描述 | 严重程度 | 发现日期 | 状态 |
|---------|---------|---------|---------|------|
| A.1 | 循环结构未深入讲解 | 中 | 2026-03-30 | 待解决 |
| A.1 | 多态概念有点模糊 | 低 | 2026-03-31 | 跟进中 |
| A.1 | 方法调用时有点慌 | 低 | 2026-03-31 | 需多练习 |
| G.35 | json.dump/load 文件操作未深入 | 低 | 2026-04-01 | 待补充 |
| A.6 | drop_duplicates/dropna 区分不清 | 低 | 2026-04-19 | ✅ 已复习 |
| A.6 | json.dumps/loads 区分不清 | 低 | 2026-04-19 | ✅ 已复习 |
| A.8 | 大模型API调用路径未确认 | 低 | 2026-04-01 | 待确认 |
| **缺失** | Matplotlib/Seaborn 还没学 | 中 | 2026-04-19 | matplotlib基本画图已会 |
| **缺失** | SQLAlchemy 还没学 | 高 | 2026-04-19 | 待补充 |
| **缺失** | SVM 概念已懂，但未亲手写代码 | 中 | 2026-05-09 | 待实操 |
| **缺失** | sklearn代码独立默写不熟练 | 高 | 2026-05-09 | 需多套模板练习 |
| **缺失** | 文本情感分析完全不会 | 低 | 2026-05-09 | 待学 |
| **缺失** | `fit(X_train, y_train)` 参数易写错（写成 X_test） | 中 | 2026-05-10 | 需反复练习 |
| **缺失** | sklearn 导入路径需查表，不能独立写出 | 中 | 2026-05-10 | 已掌握命名规律，需巩固 |
| **缺失** | GridSearchCV 自动调参还没学 | 中 | 2026-05-09 | 待补充 |
| **缺失** | matplotlib 语法不熟 | 低 | 2026-05-09 | 待练习 |
| **缺失** | Recall/Precision 分母混淆（TP/TN vs TP/FN）| 高 | 2026-06-04 | 🔴 第二次暴露 |
| **缺失** | fit_transform vs transform 数据泄露 | 高 | 2026-06-06 | 🆕 首次暴露 |
| **缺失** | Chroma ≠ Embedding 混淆 | 中 | 2026-06-05 | 🔴 持续第二天 |
| **缺失** | Python 三种访问级别 | 低 | 2026-06-06 | 🆕 首次暴露 |
| **缺失** | 广播 vs 向量化 | 低 | 2026-06-06 | 🆕 首次暴露 |
| **缺失** | Agent 死循环机制 + ModelCallLimit | 低 | 2026-06-06 | 🆕 首次暴露 |
| **缺失** | Gini vs Entropy 区别 | 低 | 2026-06-06 | 🆕 首次暴露 |
| **缺失** | Command(resume) vs 直接更新 State 的区分 | 低 | 2026-06-09 | 🆕 关键——resume是送回interrupt暂停点而非直接改state |
| **缺失** | 多内容审批（interrupt 带复杂数据结构）| 低 | 2026-06-09 | 🆕 概念已通但未实操 |
| **缺失** | class_weight='balanced' 全忘 | 中 | 2026-06-12 | ✅ 06-14 晚间巩固已纠正 |
| **缺失** | OOP 三大特性（封装/继承/多态）全忘 | 中 | 2026-06-12 | ✅ 06-14 晚间巩固已纠正 |
| **缺失** | 训练循环五步缺loss步+顺序偏差 | 高 | 2026-06-12 | 🔴 口诀"前损后步清"记不牢 |
| **缺失** | HF 五大组件只记2个 | 中 | 2026-06-12 | 🆕 缺Evaluate/Accelerate/Hub |
| **缺失** | 多态两种形式（重写+向上转型） | 低 | 2026-06-12 | 🆕 只记得方法重写 |
| **缺失** | Tensor ↔ NumPy 共享内存不知道 | 中 | 2026-06-12 | 🆕 首次接触，torch.from_numpy()无复制 |
| **缺失** | KV Cache 概念遗忘 | 低 | 2026-06-12 | 🆕 生成优化核心技术 |
| **缺失** | CrossEntropyLoss 内置三件套细节 | 中 | 2026-06-14 | 🔴 知道不加激活但说不出内部softmax+log+NLLLoss |
| **缺失** | Matplotlib 四种基本图 | 低 | 2026-06-14 | 🆕 课件15未学 |
| **缺失** | 自定义网络 __init__+forward | 中 | 2026-06-14 | 🆕 PyTorch基础知识未覆盖 |

**已解决的漏洞：**
- ~~self 概念理解不够牢固~~ → ✅ 已改善（60%）
- ~~drop_duplicates/dropna 区分不清~~ → ✅ 已复习
- ~~json.dumps/loads 区分不清~~ → ✅ 已复习
- ~~State/TypedDict/类型注解混淆~~ → ✅ 贯通（85%，学员独立拆解「数据格式说明书」类比）
- ~~state变量 vs State类型 区分~~ → ✅ 贯通（name:str 类比）
- ~~Tool vs ToolNode vs Node 混淆~~ → ✅ 贯通（学员画出完整链路图）
- ~~LangGraph 条件边~~ → ✅ 贯通（75%，route返回str+add_conditional_edges三参数）
- ~~ToolNode 与手动 llm.invoke 的选择~~ → ✅ 概念已通（ToolNode=自动，手动=灵活）

---

## 常犯错误模式

| 编号 | 错误模式 | 正确写法 | 严重程度 | 最早发现 |
|------|---------|---------|---------|---------|
| 🔴 E1 | `fit(X_train, X_test)` | `fit(X_train, y_train)` | 高 | 2026-05-09 |
| 🔴 E2 | `predict()` 忘写参数 | `predict(X_test)` | 中 | 2026-05-09 |
| E3 | `final_estimator=LogisticRegression` 少括号 | `LogisticRegression()` | 中 | 2026-05-12 |
| E4 | 相对路径找不到文件 | 用绝对路径或确认执行目录 | 中 | 2026-05-12 |
| E5 | `pd.to_numeric()` 对整表用 | 只对单列（Series）用 | 低 | 2026-05-12 |

---

## 机器学习速查框架（2026-05-10 总结）

### 选模型三步决策

```
1. 分类还是回归？
   分类（判断类别）→ 逻辑回归/决策树/随机森林/KNN/贝叶斯/SVM
   回归（预测数字）→ 线性回归/决策树回归/随机森林回归/KNN回归

2. 数据多大了？
   样本<1000, 特征<20 → 传统ML
   样本>1000, 特征很多 → 深度学习

3. 数据长什么样？
   线性关系明显 → 逻辑回归/线性回归（快，可解释）
   不确定什么关系 → 决策树/随机森林（万能基线）
   文本数据 → 朴素贝叶斯
   小样本+特征干净 → KNN 或 SVM
   要最高精度 → XGBoost/LightGBM
```

### 模型家族速查

| 家族 | 子模块 | 分类模型 | 回归模型 | 适用场景 |
|------|--------|---------|---------|---------|
| 线性 | `linear_model` | LogisticRegression | LinearRegression, Ridge, Lasso, ElasticNet | 线性关系、需解释 |
| 树 | `tree` | DecisionTreeClassifier | DecisionTreeRegressor | 非线性、表格数据 |
| 集成 | `ensemble` | RandomForestClassifier | RandomForestRegressor | 万能基线 |
| 距离 | `neighbors` | KNeighborsClassifier | KNeighborsRegressor | 小样本、需标准化 |
| 概率 | `naive_bayes` | GaussianNB, MultinomialNB | — | 文本分类 |
| 边界 | `svm` | SVC | SVR | 高维、非线性、小样本 |

### 一句口诀
> 拿数据先试树，要解释用线回，做文本上贝叶斯，追精度上 XGBoost。

### 分类四指标速查

| 指标 | 含义 | 公式 | 业务问题 | 你的模型 |
|------|------|------|---------|---------|
| Accuracy | 判断对了多少（笼统） | (TP+TN) / 总数 | "看病有没有用" | 79% |
| Recall | 真要走的，抓多少 | TP / (TP+FN) | "漏了多少"→越低漏越多 | 53% ⚠️ |
| Precision | 喊走的，几个真走 | TP / (TP+FP) | "虚惊多少"→误报 | 64% |
| F1 | Recall 和 Precision 调和平均 | 2RP/(R+P) | "两个一起看" | 58% |

**四种结果：**
```
预测不走 + 真实不走 = TN（正常）
预测会走 + 真实会走 = TP（抓到了）
预测会走 + 真实不走 = FP（虚惊）
预测不走 + 真实会走 = FN（漏了！）
```

| 场景 | 优先指标 | 原因 |
|------|---------|------|
| 挽留用户（流失预测） | Recall | 漏一个丢几百块 |
| 垃圾邮件 | Precision | 误删一封重要邮件比漏一封垃圾严重 |
| 疾病筛查 | Recall | 漏诊命没了 |
| 精准广告 | Precision | 乱推广告只烦人，不推也行 |

---

---

## 课件进度

| 课件 | 内容 | 状态 |
|-----|------|------|
| 01-14 | Python基础/Numpy/Pandas | ✅ 已学 |
| 15 | Matplotlib/Seaborn | ❌ 未学 |
| 16 | Git/MySQL | ✅ 已学 |
| 17 | SQLAlchemy | ❌ 未学 |
| 18 | FastAPI | ✅ 已学 |

---

## 学习计划

### 当前阶段
- **重点模块**：A. Python 工程化基础（权重最高 20%）
- **当前考点**：A.1 Python 基础语法 - 面向对象
- **综合掌握度**：42%

### 今日完成 ✅

**2026-03-31（面向对象）：**
- [x] 预习作业：写"狗"类
- [x] 深入理解 self 的作用
- [x] 学习方法的定义和调用
- [x] 学习继承
- [x] 学习重写（Override）
- [x] 学习 super()
- [x] 学习封装（私有属性）
- [x] 学习 get/set 方法
- [x] 学习多态（初步）
- [x] 学习 __str__ 方法
- [x] 理解内存中对象的存储

**2026-04-01（数据分析 + API）：**
- [x] NumPy 创建数组、运算、reshape
- [x] NumPy 数组属性、切片
- [x] NumPy 排序（np.sort vs arr.sort）
- [x] JSON 基础操作（dumps/loads）
- [x] requests.get 获取数据
- [x] requests.post 发送数据
- [x] 嵌套 JSON 数据提取
- [x] 尝试调用大模型 API

**2026-04-02（NumPy 深入 + 大模型概念）：**
- [x] NumPy flatten 拍扁数组
- [x] NumPy 转置 .T
- [x] NumPy 逆矩阵 linalg.inv
- [x] NumPy 统计函数（max/min/mean/std/median）
- [x] NumPy 广播机制原理
- [x] 大模型基础：梯度下降原理
- [x] 大模型基础：GPU vs CPU
- [x] 大模型基础：H100/A100/H800/A800 区别
- [x] 大模型基础：神经网络层概念
- [x] 大模型基础：本地 vs 云端运行

**2026-04-03（广播机制深入 + 大模型完整认知）：**
- [x] 广播机制深入：从右对齐，不够补1
- [x] 一维 vs 二维的本质区别（形状不同）
- [x] 一维转置不变，二维转置行列互换
- [x] 梯度下降复习：下降的是损失值
- [x] RTX系列显卡性价比排序
- [x] PyTorch能否在Intel Arc上运行
- [x] 云服务器 vs 算力服务器区别
- [x] 分析用户电脑配置（Intel Ultra 5 125H + Arc核显）

### 今日完成 ✅

**2026-05-10（ML 模板复习 + 科学复习法）：**
- [x] 裸写 ML 7 步模板（红酒数据集）
- [x] 掌握 sklearn 子模块命名规律（基础五件套 + 辅助三兄弟）
- [x] 理解标准化适用场景（哪些模型需要/不需要）
- [x] 独立跑通 `5_9task.py`（红酒分类，准确率 1.0）
- [x] 理清知识管理策略（tracker 是唯一笔记，对话产出最有价值）

**2026-05-11（集成学习入门 + 无监督学习 + 数学基础）：**
- [x] 集成学习三招入门（Bagging/Boosting/Stacking）
- [x] 无监督学习概览（K-Means/DBSCAN/层次聚类/PCA/t-SNE）
- [x] 手推机器学习第一章整理（频率派vs贝叶斯派 + 高斯分布）
- [x] ML 速查框架沉淀到 tracker
- [x] CLAUDE.md 新增"所有总结必须保存"规则

### 近期目标（按优先级）
1. [x] ✅ Git 基础操作 → 已学习（2026-04-25）
2. [ ] 循环结构（while/for）→ 目标 60%
3. [ ] 多态巩固练习
4. [ ] 函数参数四种形式 → 目标 60%
5. [ ] SQLAlchemy 深入学习
6. [ ] Matplotlib/Seaborn 可视化

**2026-05-12（Stacking 实战 + 分类指标 + OOP 复习）：**
- [x] 贝叶斯 MAP 公式深度学习（argmax/log/先验→正则化）
- [x] 电信用户流失预测项目（StackingClassifier，accuracy 0.79）
- [x] 分类指标深入理解（Accuracy/Recall/Precision/F1）
- [x] class_weight='balanced' 原理与实操
- [x] OOP 快速复习（__init__/__str__/self/继承）
- [x] Session notes 记录标准改革（CLAUDE.md 更新）

**2026-05-13（深度学习入门 + 系统复习 + 记忆固化）：**
- [x] PyTorch 入门（训练循环 vs sklearn fit 对比）
- [x] 神经网络基础复习（有监督学习、需要标准化）
- [x] SVM 系统复习（软硬间隔、核函数、支撑向量、适用/不适用场景）
- [x] 标准化原理深度学习（哪些模型需要 + 数学原因）
- [x] 朴素贝叶斯四种复习（Gaussian/Multinomial/Bernoulli/Complement）
- [x] CLAUDE.md 新增「间隔复习提问」规则
- [x] 分类指标 + OOP + 正则化 间隔复习提问
- [x] Session notes 写成"背诵清单"格式

**2026-05-14（系统串联复习 + 知识网络固化）：**
- [x] 训练循环六步完整推导（MSE→梯度→更新 w）
- [x] 损失函数三人对比（MSE vs 交叉熵 vs MAE）
- [x] 正则化串联（MSE/L2 → Ridge → 高斯先验）
- [x] 贝叶斯线完全推导（p(θ)→先验三分布→三正则）
- [x] 梯度下降精讲（梯度=0 含义）
- [x] 标准化决策树（谁需要+数学原因）
- [x] 模型全家福速查表（六家族+特殊需求）
- [x] 深度学习入门（隐藏层逐层抽象+激活函数折弯）
- [x] SVM 四核函数 vs 朴素贝叶斯四种（防串助记）
- [x] 分类四指标公式默写纠正（Recall 分母 TP+FN）
- [x] Session notes 写成「11 节串联背诵链」

**2026-05-17（ML底层五大追问 + 五步代码 + 思维导图完整版）：**
- [x] θ=w 统一理解（贝叶斯θ→ML权重w，全链打通）
- [x] 贝叶斯→正则化完整推导链（-log p(X|w)=MSE, -log p(w)=L2/L1, MAP=Ridge）
- [x] 频率vs贝叶斯：是统计学哲学，不是ML算法分类方式
- [x] ML模型五派分类体系（wx+b派/树派/距离派/概率派/边界派）
- [x] Ridge vs BayesianRidge 核心区别（点估计vs分布，工业vs医疗）
- [x] 梯度下降学习率本质（梯度=方向，lr=步长，最好w一步一步走）
- [x] 决策树切分原理（贪心搜索不求导）+ 三算法演进(ID3→C4.5→CART)
- [x] 决策树 vs 逻辑回归全面对比表
- [x] wx+b标量→矩阵推导（X@w+b, X.T@(ŷ-y)）
- [x] sklearn 内置数据集速查（load_/fetch_/make_ 三类）
- [x] ML五步标准模板代码（ml_standard_template.py, Ridge+LogisticRegression双示例）
- [x] 机器学习思维导图完整版：融合对话+Knowledge Base+PDF+左右布局
- [x] F模块：新增8子考点，综合30%→35%

**2026-05-18（深度学习入门——反向传播+TODO训练循环）：**
- [x] 隐藏层层级抽象（边→部件→完整概念，自然涌现非预设）
- [x] 多模态本质（图像/语音/文本→都是张量，X@W+b）
- [x] 前向→反向→更新 完整流程（每层都在更新 w,b）
- [x] 反向传播链式法则手动计算（x=2,w₁=3,w₂=4,y=10）
- [x] 导数=方向：正数→w变小，负数→w变大
- [x] z(线性) vs a(激活后) 符号区分
- [x] PyTorch 训练循环五步（forward→loss→backward→step→zero_grad）
- [x] DL 属于 wx+b 派（五派分类确认）
- [x] 间隔复习：标准化（逻辑回归需要vs决策树不需要）

**2026-05-19（泰坦尼克号实操+CNN卷积基础+每日问答）：**
- [x] 泰坦尼克号完整代码逐行精讲（fillna/One-Hot/stratify/fit_transform/Dataset/DataLoader/.view）
- [x] 数据泄露原理（fit_transform 只在训练集，验证集只 transform）
- [x] pandas→PyTorch 两大数据类型 Bug 修复（copy + astype）
- [x] CNN 卷积核底层机制（in/out_channels、参数计算、并行滑动、分工涌现）
- [x] PyTorch 五块模板体系（数据→DataLoader→模型→配置→训练循环）
- [x] Python 五种基本数据类型复习（列表/元组/集合/字典/字符串）
- [x] 每日问答 5 题（动态计算图/训练四步/NaN排查/梯度累积）

### 明日计划
- [ ] **独立重现 10taitan.py**（不查资料，从五块骨架开始裸写）
- [ ] CNN 继续深入（池化层 Pooling、步长 stride、padding、感受野）
- [ ] PyTorch 手写 MNIST CNN（实用卷积代码）
- [ ] 函数四种参数形式快速复习（当前 25%）
- [ ] Seq2Seq + Attention 代码实操

**2026-05-22（RNN/LSTM 五道题复盘 + 课件对照 + 补漏）：**
- [x] LSTM 权重共享澄清：跨时刻共享 vs 跨门独立（两个维度）
- [x] 五道题完整回答：RNN tanh、BPTT 消失/爆炸、LSTM C_t 加法、GRU 简化、注意力三步
- [x] 课件对照：发现漏掉 BiRNN、RNN vs Transformer、工程 6 条
- [x] 双向 RNN 原理（正反拼接 + hidden×2）
- [x] RNN vs Transformer 互补关系
- [x] 工程实践 6 条（词表填充→Embedding→RNN→Dropout→FC、梯度裁剪、内存三招）

---

## 会话历史索引

| 日期 | 会话记录 | 核心主题 | 重点收获 |
|------|---------|---------|---------|
| 2026-03-30 | [session-notes](../sessions/2026-03-30/session-notes.md) | 函数参数 + 面向对象预习 | 逻辑运算符60%，面向对象初步接触 |
| 2026-03-31 | [session-notes](../sessions/2026-03-31/session-notes.md) | 面向对象深入学习 | 继承、重写、封装、多态、__str__，A.1提升到42% |
| 2026-04-01 | [session-notes](../sessions/2026-04-01/session-notes.md) | NumPy + JSON + requests | 数据分析预习，API调用入门 |
| 2026-04-02 | [session-notes](../sessions/2026-04-02/session-notes.md) | NumPy深入 + 大模型概念 | 广播机制、矩阵运算、梯度下降、GPU、大模型基础 |
| 2026-04-03 | [session-notes](../sessions/2026-04-03/session-notes.md) | 广播深入 + 完整认知 | 一维vs二维区别、云算力、学习路线、用户配置分析 |
| 2026-04-11 | [session-notes](../sessions/2026-04-11/session-notes.md) | BERT深入学习 | Encoder/Decoder、MLM/NSP、Multi-Head Attention |
| 2026-04-13 | [session-notes](../sessions/2026-04-13/session-notes.md) | Pandas数据处理 + 作业规划 | fillna/dropna/rank/astype/apply/str + 作业确认为BERT+BiLSTM |
| 2026-04-16 | [session-notes](../sessions/2026-04-16/session-notes.md) | FastAPI基础 + 前后端架构 | @装饰器、Path/Query/Body参数、Pydantic模型、前后端分离 |
| 2026-04-19 | [session-notes](../sessions/2026-04-19/session-notes.md) | 复习+查漏补缺 | 面向对象练习、命名规范、知识漏洞发现 |
| 2026-04-21 | [session-notes](../sessions/2026-04-21/session-notes.md) | 前端三件套+FastAPI项目 | HTML/CSS/JS基础、SQLAlchemy初步、依赖注入 |
| 2026-04-25 | [session-notes](../sessions/2026-04-25/session-notes.md) | Git复习+推送练习 | clone/add/commit/push、远程仓库、GitHub推送 |
| 2026-04-27 | [session-notes](../sessions/2026-04-27/session-notes.md) | Attention论文+DeepSeek API | 归一化、Layer Norm、DeepSeek调用 |
| 2026-04-28 | [session-notes](../sessions/2026-04-28/session-notes.md) | 神经网络+深度学习理论 | 神经元计算、反向传播、卷积/CNN（刚记录待深入） |
| 2026-05-09 | [session-notes](../sessions/2026-05-09/session-notes.md) | sklearn实操（贝叶斯/KNN/调参） | ML模板、4种贝叶斯、KNN调参画图、模型对比 |
| 2026-05-10 | [session-notes](../sessions/2026-05-10/session-notes.md) | ML模板复习+科学复习法 | 裸写7步模板、sklearn导入规律、标准化适用场景、42梗 |
| 2026-05-11 | [session-notes](../sessions/2026-05-11/session-notes.md) | 集成学习+无监督学习+数学基础 | 三招(Bagging/Boosting/Stacking)、PCA/t-SNE推导、聚类、频率派vs贝叶斯派 |
| 2026-05-12 | [session-notes](../sessions/2026-05-12/session-notes.md) | 贝叶斯深度学习+Stacking实战+分类指标+OOP复习 | MAP公式推导、StackingClassifier、accuracy/recall/precision/F1、__str__复习 |
| 2026-05-13 | [session-notes](../sessions/2026-05-13/session-notes.md) | 深度学习入门+SVM复习+标准化原理+间隔复习 | PyTorch骨架、标准化谁需要/谁不需要、SVM软硬间隔核函数、贝叶斯4种、知识点背诵清单 |
| 2026-05-14 | [session-notes](../sessions/2026-05-14/session-notes.md) | 系统串联复习（训练循环→损失→正则→贝叶斯→模型全家福→深度学习） | 11节背诵链：MSE/交叉熵/MAE、L1/L2→Ridge/Lasso、三先验→三正则、梯度下降六步、模型选型表 |
| 2026-05-17 | [session-notes](../sessions/2026-05-17/session-notes.md) | ML底层五大追问（θ意义/损失角色/频率vs贝叶斯/正则化目的/学习率）+五步代码 | θ=w全链、贝叶斯→正则推导、五派分类、Ridge/BayesianRidge对比、梯度vs学习率、五步标准模板 |
| 2026-05-18 | [session-notes](../sessions/2026-05-18/session-notes.md) | 深度学习入门——反向传播链式法则手动计算+训练循环五步 | 隐藏层层级抽象、前向→反向→更新全流程、偏导数手动计算(28×4×2=224)、导数=指南针正负号、DL=wx+b派 |
| 2026-05-19 | [session-notes](../sessions/2026-05-19/session-notes.md) | 泰坦尼克号实操+CNN卷积基础+PyTorch五块模板 | 数据全流程(缺失值→One-Hot→标准化→DataLoader)、卷积核机制(160参数并行分工)、pandas bug修复、每日问答5题 |
| 2026-05-21 | [session-notes](../sessions/2026-05-21/session-notes.md) | RNN+LSTM+GRU 三门机制深度学习 | RNN比全连接多h@W_h、LSTM三门(遗忘/输入/输出)+C长期h短期、GRU简化版、sigmoid门vs tanh候选 |
| 2026-05-22 | [session-notes](../sessions/2026-05-22/session-notes.md) | RNN/LSTM 五道题复盘 + 课件对照补漏 | 权重共享两维度、BiRNN、RNN vs Transformer互补、工程实践6条、CLIP双塔多模态 |
| 2026-05-23 | [session-notes](../sessions/2026-05-23/session-notes.md) | 泰坦尼克号数据清理流程 + 两种方案对比 | 四步决策链、基础vs进阶方案、标准化顺序（先切后fit）、特征衍生 |
| 2026-05-24 | [session-notes](../sessions/2026-05-24/session-notes.md) | import 三分类 + torch.nn 边界 + Titanic 十步清单 | 不变核心vs可变外圈、nn只有积木模型在外部库、逐行注释版代码 |
| 2026-05-25 | [session-notes](../sessions/2026-05-25/session-notes.md) | Transformer 七问 + 梯度全家桶 + GPU + ML→DL链 | 自注意力五步、多头、掩码、位置编码、FFN、残差+Pre-LN、梯度消失/爆炸/累积 |
| 2026-05-26 | [session-notes](../sessions/2026-05-26/session-notes.md) | HF晨考 + 知识蒸馏 + DL全链复习 + IMDB项目拆解 | HF七问、蒸馏(软标签/温度T/双损失)、DL全景(张量→Transformer)、IMDB情感分析10步 |
| 2026-05-27 | [session-notes](../sessions/2026-05-27/session-notes.md) | 大模型显存评估 + LoRA 低秩微调 + GRPO | 推理公式/量化精度、ΔW=B×A、256倍参数压缩、PPOvsGRPO、规则奖励+组平均基线 |
| 2026-05-28 | [session-notes](../sessions/2026-05-28/session-notes.md) | 残差连接 + LayerNorm + Transformer 全流程 | +1保底梯度不消失、先残差后Norm、Encoder-Decoder全景、自注意力vs交叉注意力 |
| 2026-05-30 | [session-notes](../sessions/2026-05-30/session-notes.md) | C盘清理 + 环境整治 + IMDB骨架六步实操 | 软链接搬家释放23G、Conda统一环境、IMDB六步独立写出+每步理解 |
| 2026-06-01 | [session-notes](../sessions/2026-06-01/session-notes.md) | IMDB项目收尾——代码改进+精度概念深挖 | fp16/INT8精度对比、tokenizer配套保存原理、compute_metrics结构、训练五步口诀"前损后步清" |
| 2026-06-03 | [session-notes](../sessions/2026-06-03/session-notes.md) | nn.Linear微认知穿透 + LangChain进阶（中间件/消息流转/Supervisor）+ 题库系统搭建 | nn.Linear行列方向85%、Middleware 60%、消息流70%、Supervisor 50%、Agent 10%→18% |
| 2026-06-04 | [session-notes](../sessions/2026-06-04/session-notes.md) | 智能差旅Agent实战 + 晨间9题 + 薄弱点速固 | Middleware 60%→70%、Agent搭建40%→65%、PIIMiddleware 5种类型、stream过滤、thread_id |
| 2026-06-05 | [session-notes](../sessions/2026-06-05/session-notes.md) | RAG完整教程(59页1-8章精讲+9-12速览) + 晨间9题 | RAG六站管道70%、Document80%、分块75%、Embedding三路线65%、Agentic RAG60%、B模块5%→35% |
| 2026-06-06 | [session-notes](../sessions/2026-06-06/session-notes.md) | 题库架构v2.0（双层晨考20题）+ ChatPDF项目启动 + 晨考错题沉淀 | 题库架构80%、enumerate85%、BPTT梯度消失75%、Gini60%、注入10题首发 |
| 2026-06-08 | [session-notes](../sessions/2026-06-08/session-notes.md) | LangGraph核心概念拆解（State/Node/Tool/ToolNode/LLM）+ 三个demo实战调试 | State/TypedDict 85%、Node本质80%、Tool vs ToolNode 75%、LLM vs Tool 80%、六概念独立拆解 |
| 2026-06-09 | [session-notes](../sessions/2026-06-09/session-notes.md) | Human-in-the-Loop 全流程拆解（interrupt/Command/MemorySaver）+ demo3_2_hum_loop 调试 | HITL 85%、MemorySaver/thread_id 80%、条件边 75%、学员独立输出七步面试级总结 |
| 2026-06-10 | [session-notes](../sessions/2026-06-10/session-notes.md) | AutoGPT Think-Act 循环从零调试（8bug全修：import路径/括号/State类型/return规则/path_map）| 条件边 80%、AutoGPT循环 75%、Node/Route规则 85%、import 70% |
| 2026-06-11 | [session-notes](../sessions/2026-06-11/session-notes.md) | 题库轻量索引建设 + AutoGPT/BabyAGI测验14题 + 模块三HTML提取16题入库 | C模块30→60题，四文件分工系统，晨考上下文省88% |
| 2026-06-12 | [session-notes](../sessions/2026-06-12/session-notes.md) | softmax手算全链 + Transformer公式六步 + Tool/Agent/多Agent辨析 + 晨考19题 | softmax 85%、Attention六步75%、Agent决策权区分80%、晨考47%暴露OOP/训练循环遗忘 |
| 2026-06-14 | [session-notes](../sessions/2026-06-14/session-notes.md) | 06-11回顾 + 晚间5题巩固 + 晨考二轮18题（72%） | 间隔复习验证有效(47%→72%)、HF五组件/训练循环/OOP全焊住、面试注入100% |
| 2026-06-23 | [session-notes](../sessions/2026-06-23/session-notes.md) | 课件模块一二提取23题入库 + Day1训练(1.1~1.3) + 学员推导XLNet/KV Cache | 注入池A 186题、D28%/E30%整体38%、1.2 C层项目映射完成、BERT/GPT/XLNet三架构贯通 |

