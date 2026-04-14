# 学习会话记录 - 2026-04-13

## 会话概览
- 日期：2026-04-13
- 形式：一对一教学
- 核心主题：Pandas数据处理 + 作业规划

## 学员提出的问题/需求
1. 不确定作业要求是1个模型还是2个模型对比
2. 想学Pandas数据处理
3. 计划：BERT + BiLSTM 对比做情感分析

## 讲解的概念与教学过程

### 1. 作业要求澄清
学员误以为BERT/Transformer/Embedding是同一个东西，实际上：
- Embedding = 词向量（把词变成数字）
- Transformer = 神经网络架构
- BERT = 用Transformer的Encoder做出来的模型

**结论**：Assignment 2 需要实现至少1个模型，为了高分建议做BERT vs BiLSTM对比

### 2. Pandas数据处理学习（基于demo3代码）

#### 已掌握的知识点：
| 知识点 | 命令 | 状态 |
|-------|------|------|
| 创建DataFrame | pd.DataFrame({'列名': [值]}) | ✅ |
| 查看概况 | info() / describe() / head() | ✅ |
| 处理缺失值 | fillna() / dropna() | ✅ |
| 处理重复值 | drop_duplicates() | ✅ |
| 定位数据 | loc[条件, 列名] | ✅ |

#### 新学的知识点：
| 知识点 | 命令 | 示例 |
|-------|------|------|
| 排序 | sort_values() / sort_index() | df.sort_values('col') |
| 排名 | rank() | df['col'].rank(method='min') |
| 最大最小 | nlargest() / nsmallest() | df.nlargest(2, 'col') |
| 检查缺失 | isnull() / isna() | df.isnull().sum() |
| 类型转换 | astype() | df['col'].astype(int) |
| 批量处理 | apply(lambda) | df['col'].apply(lambda x: ...) |
| 字符串处理 | str.replace() | df['col'].str.replace('a', 'b') |

### 3. 遇到的错误
- `df[条件]['列'] = 值` 警告：用 loc 更安全
- `astype(int)` 失败：NaN不能转int，需先 fillna()

## 学员问题记录
- loc[行条件, 列名] 第二个age是什么意思？（回答：定位到哪一列）
- rank() 并列平均的意义？（回答：用于精确统计分析）
- 大括号{} vs 中括号[] 创建DataFrame的区别？（回答：{}有列名，[]无列名）

## 识别的知识漏洞
- rank() 的 method='average' 实际应用场景较少
- 字符串列 vs 普通 replace() 的区别

## 完成的练习
1. 运行 info() / describe() / head()
2. fillna() 填充缺失值
3. drop_duplicates() 按列去重
4. loc[] 定位并修改异常值
5. astype() 类型转换
6. apply(lambda) 批量处理
7. str.replace() 字符串替换

## 明天学习计划
1. Matplotlib（折线图、柱状图、饼图、散点图）
2. Seaborn（7种图表）
3. Pandas补充：fillna、duplicated、drop_duplicates、astype、apply、str.replace

## 作业规划
- 选定模型：BERT + BiLSTM 对比
- 剩余时间：约5天
- 下一步：开始写BERT情感分析代码

## 学习效果评估
- Pandas数据处理能力：明显提升
- 对作业要求的理解：已澄清
- 学员状态：积极学习
