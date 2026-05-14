# 学习会话记录 - 2026-05-12

## 今日理解跃迁

> 从"__str__ 是什么鬼完全没印象" → "就是给 print 自定义输出，Python 自动调的。跟 __init__ 一样是自动触发机制"

## 会话概览
- 日期：2026-05-12
- 核心主题：贝叶斯深度学习 + Stacking 实战 + 分类指标 + OOP 复习

---

## 学员提出的问题（原文）

1. "卡尔曼滤波是将上一刻的后验，变成这一刻的先验，带入到贝叶斯概率公式，用到高斯线性回归模型，对吗"
2. "独立同分布抽出来，这句话代表什么意思"
3. "为什么物理数学到最底层就会分为两类"
4. "贝叶斯派的观点这个公式怎么来的"
5. "argmax 再详细一点"
6. "为什么加 log，为什么加个 log p(θ) 就是惩罚项"
7. "stacking 后面是 classifier 或者 regression，有区别吗，预测不是应该回归吗"
8. "class_weight='balanced'，这个作用详细解释一下"
9. "可以详细给我讲解一下这些指标吗（分类指标），我还是很懵"
10. "就是这个 str 我对这个完全没用印象，不知道如何用"

---

## 核心问答记录

### 1. 卡尔曼滤波 vs 贝叶斯

> **学员说：** "卡尔曼滤波是将上一刻的后验，变成这一刻的先验，带入到贝叶斯概率公式"
> **答：** 完全正确。卡尔曼滤波 = 贝叶斯推断的递归版本。每步都是先验 × 似然 → 后验，后验滚到下一步当先验。必须用高斯线性模型是因为只有高斯×线性变换还是高斯，整个递归才能用解析公式。

### 2. iid 独立同分布

> **问：** 独立同分布什么意思？
> **答：** 独立 = 一个样本不影响另一个（才能拆成连乘）；同分布 = 所有样本来自同一个分布同一个 θ。MLE 公式里 `p(X|θ) = ∏ p(x_i|θ)` 能成立，前提就是 iid。

### 3. 为什么加 log？（两个原因）

**原因一：连乘变连加，求导好算。** N 个概率连乘求导痛苦，取 log 后加法每项独立。
**原因二：防止下溢。** 0.1^1000 ≈ 10^(-1000)，计算机当 0。取 log 后 1000 个负数相加完全在范围内。
**log 是单调递增的，最大值位置不变。**

### 4. 为什么 log p(θ) 是"惩罚项"？（学员质疑了"惩罚"这个叫法）

**优化视角（工程师）：** log p(θ) 很负时总分被拉低，优化器避开不合理区域 → "惩罚"
**贝叶斯视角（学员自己的理解）：** "不该说是惩罚项，而是贝叶斯的根本——就是我心里有这个想法，我想让数据往我想法靠近一点"

**学员原话：**
> "log p(θ) 不该说是惩罚项，而是贝叶斯的根本——就是我心里有这个想法，我想让数据往我想法靠近一点。贝叶斯太牛逼了，我现在明白之后，感觉它真牛逼。"

### 5. 先验分布 → 正则化对应关系

| 先验分布 | log p(θ) | 转成最小化 | 正则化 |
|---------|----------|-----------|--------|
| 均匀分布（常数） | 0 | 无 | 退化成 MLE |
| 高斯 N(0,σ²) | -θ²/(2σ²) | +λθ² | L2 |
| 拉普拉斯 | -|θ| | +λ|θ| | L1 |

### 6. StackingClassifier 项目（电信用户流失预测）

**数据：** telco-churn-7k，7043 条，21 列 → get_dummies 后 45 列（drop_first 后 25 列）
**目标：** 预测 Churn（Yes/No，二分类）

**数据清洗流程：**
```python
pd.read_csv()                           # 加载
pd.to_numeric(col, errors='coerce')     # TotalCharges 空格→NaN
drop('customerID', axis=1)             # 删无关列
pd.get_dummies(X, drop_first=True)     # 文字→0/1
y.map({'Yes': 1, 'No': 0})            # 目标编码
dropna()                                # 处理 NaN
train_test_split(X, y, test_size=0.2)  # 切数据
```

**Stacking 结构：**
```python
base_model = [
    ('lr', LogisticRegression(max_iter=5000)),
    ('dt', DecisionTreeClassifier()),
    ('rf', RandomForestClassifier())
]
stacking = StackingClassifier(estimators=base_model, final_estimator=LogisticRegression())
```

**结果：** accuracy 0.79，recall(Yes) 53%

### 7. 分类指标详解（学员说"懵"）

**学员纠正了一个小错误：** Precision = TP/(TP+FP)，不是 TP/(TP+TN)

**用数据反推的实际数字：**
```
917人 ✅ 猜对（预测不走，确实没走）
199人 ✅ 抓到（预测会走，真走了）
114人 ❌ 虚惊（预测会走，结果没走）
177人 ❌ 漏了（预测不走，实际走了）

Accuracy = (917+199)/1407 = 79%
Recall(Yes) = 199/376 = 53%   ← 真要走的 376 人只抓到 199
Precision(Yes) = 199/(199+114) = 64%
```

**学员原话理解：**
> "准确率是模型预测的是否正确，召回率是目标值模型预测或者说找到多少，精确率是模型预测是的情况下真正预测对的人，f1则是调和准确率和召回，因为这两个指标很难做到同时都高。"

### 8. 模型选型决策（针对电信数据）

| 模型 | 适合不 | 原因 |
|------|--------|------|
| 逻辑回归 | ✅ | 0/1 列和数字列，线性可抓趋势 |
| 决策树 | ✅ | 天然处理 0/1 列，不用标准化 |
| 随机森林 | ✅ 最推荐 | Bagging 版决策树，表格数据主场 |
| KNN | ⚠️ | 25 维太高，0/1 列算距离无意义 |
| 朴素贝叶斯 | ❌ | 0/1 列之间不独立 |
| SVM | ⚠️ | 7000 条训练慢，杀鸡用牛刀 |

---

## OOP 快速复习（学员说"我真忘完了"）

**问题：** `__str__` 完全没印象，不知道如何用

**用旧代码讲解（practice5.py）：**

```python
class bicycle(Vehicle):
    def __str__(self):
        return f"自行车品牌是{self.brand}，材料是{self.material}"

a = bicycle("a", 12, "glass")
print(a)  # 自动调 __str__ → "自行车品牌是a，材料是glass"
```

**核心理解：**
- `__init__` = 创建对象时自动跑（`Dog("旺财")` 时触发）
- `__str__` = print(对象) 时自动跑（让你自定义输出样子）
- 不加 `__str__` → `print(对象)` 输出 `<object at 0x...>` 丑东西

**实际开发三个场景：**
1. **调试** — `print(对象)` 看到具体数据而非内存地址
2. **日志** — 崩了能读而不是 `<student at 0x...>`
3. **API 返回** — 前端调接口返回的 JSON 里对象得能读

**本质：** 不用手动 `print(obj.name, obj.age, obj.ic)`，一句 `print(obj)` 全搞定。

---

## 踩坑与纠正

| 错误 | 怎么发现的 | 正确 |
|------|-----------|------|
| `final_estimator=LogisticRegression` 少 `()` | TypeError: Cannot clone object | `final_estimator=LogisticRegression()` |
| 路径 `../telco-churn-7k/` 找不到文件 | FileNotFoundError | 数据在 `machine-Learning` 下，用绝对路径 |
| `pd.to_numeric(A)` 对整表用 | 函数只接受 Series | `A['TotalCharges']=pd.to_numeric(...)` |
| `X,y=A['Churn']` 拆不开 | 语法错 | 分两行：`y=A['Churn']` + `X=A.drop('Churn',axis=1)` |
| 数据有 NaN | LogisticRegression 报错 | `X.dropna()` 处理 |

---

## 知识漏洞

- OOP 基础忘了很多（`__init__`/`__str__`/继承语法需要复习）
- `pd.read_csv` 记不住路径规则（相对路径 vs 绝对路径、执行目录 vs 脚本目录）
- 回归模型（Ridge/Lasso）概念懂但分不清分类 vs 回归场景
- Stacking 是第一次写，`final_estimator` 语法不熟

---

## 创建的/更新的文件

| 文件 | 操作 | 内容 |
|------|------|------|
| `CLAUDE.md` | 更新 | Session notes 新标准（10 板块 + 判断标准 + Tracker/Session 分工表） |
| `sessions/2026-05-11/session-notes.md` | 更新 | 补"今日理解跃迁"、续接贝叶斯深度学习内容 |
| `restaurant_test/model.py` | 新建 | Restaurant 类（__init__ 完成，__str__ 待补） |
| `machine-Learning/5_12.py` | 新建 | 电信流失 Stacking 项目（accuracy 0.79） |

---

## 学习效果评估

- 贝叶斯理解：从"先验是惩罚"到"先验是我心里本就有的信念"，理解跃迁完成
- ML 实操：独立完成从 CSV 读取到 StackingClassifier 全流程，中途语法需提示
- 分类指标：能用自己的话解释四指标含义和场景
- OOP：快速复习后恢复记忆，`__str__` 从零到理解

---

## 下次继续

继续学习，请读取：
1. progress/python-tracker.md
2. sessions/2026-05-12/session-notes.md

今天最后在复习 OOP 基础，下次可以：
- 继续餐厅评分项目：database.py（SQLAlchemy）
- 或 5_12.py 调参提升 recall
