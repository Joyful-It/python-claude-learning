# 学习会话记录 - 2026-05-10

## 会话概览
- 日期：2026-05-10
- 形式：一对一教学
- 核心主题：ML 模板复习 + sklearn 子模块速查 + 科学复习法

## 学员提出的问题/需求
1. "怎么复习，要求科学，性价比" — 希望高效复习而非重读课件
2. "除了逻辑回归，其他机器学习模型怎么导入" — 想建立系统的导入记忆法
3. "为什么大家默认填 42" — 对 random_state=42 的梗好奇
4. "为什么要标准化，我记得线性回归好像就没用到这个" — 质疑标准化必要性
5. "我还需要总结吗，比如这个记忆口诀，我还需要再写一个笔记吗" — 询问笔记策略
6. "你更新知识的标准是什么，我觉得最重要的是我问的然后总结出来的东西" — 对知识管理的元认知

## 讲解的概念与教学过程

### 1. 科学复习法（主动提取）
- 裸写 → 对答案 → 换数据 → 学新知，四步递进
- 记忆留存率：重读 20% vs 裸写 70% vs 换数据 85%

### 2. sklearn 子模块命名规律（用户主动问）
| 家族 | 子模块 | 常用模型 |
|------|--------|---------|
| 线性模型 | `linear_model` | LogisticRegression, LinearRegression |
| 树模型 | `tree` | DecisionTreeClassifier |
| 邻居 | `neighbors` | KNeighborsClassifier |
| 贝叶斯 | `naive_bayes` | GaussianNB, BernoulliNB, MultinomialNB |
| SVM | `svm` | SVC |
| 集成 | `ensemble` | RandomForestClassifier, GradientBoostingClassifier |
| 预处理 | `preprocessing` | StandardScaler, MinMaxScaler |
| 模型选择 | `model_selection` | train_test_split, GridSearchCV |
- **记忆口诀**：基础五件套（线/树/邻/贝/SVM）+ 辅助三兄弟（预/选/管）

### 3. 标准化适用场景（用户主动质疑）
- 必须标准化：KNN、SVM（算距离）、神经网络、正则化回归
- 不需标准化：决策树、随机森林、朴素贝叶斯
- 逻辑回归：可做可不做，做了收敛更快
- **核心判断**：涉及"距离计算"或"梯度下降"就先标准化

### 4. random_state=42 由来
- 科幻小说《银河系漫游指南》梗："42 是生命、宇宙和万物的终极答案"
- 无技术原因，填任意数字效果相同

### 5. 练习：红酒分类（裸写 ML 模板）
- 用户从伪代码开始，一步步补全到可运行代码
- 最终结果：准确率 1.0（红酒数据集，逻辑回归）
- 踩坑记录：
  - `train_test_split` 返回顺序险些写错（昨天也犯过）
  - `fit(X_train, X_test)` → 应为 `fit(X_train, y_train)`
  - `predict()` 忘写参数 → 应为 `predict(X_test)`

## 完成的练习
1. ✅ 5_9task.py — 红酒分类：load_wine → split → StandardScaler → LogisticRegression → 1.0

## 识别的知识漏洞
- 导入路径需查表，不能独立写出（但对命名规律已有认知）
- `fit` 参数容易写错（训练时需要 X + y，不是 X_train + X_test）
- `RadiusNeighborsClassifier` 写错（应为 `KNeighborsClassifier`）
- 漏加 `max_iter`（虽未报警告，概念上应知道多分类需更大迭代次数）

## 知识管理元认知讨论
- 学员认为最有价值的是"主动问出来的总结"而非预设课件
- 确认：CLAUDE.md 是骨架，对话中产出的速查表/口诀/踩坑记录才是血肉
- tracker 更新标准：新学知识点 + 主动提问总结 + 暴露薄弱点

机器学习
│
├── 按任务分
│   ├── 分类（判断类别）
│   │   ├── 二分类：垃圾邮件？续费？
│   │   └── 多分类：手写数字 0-9
│   │
│   ├── 回归（预测数字）
│   │   └── 房价、温度、分数
│   │
│   ├── 聚类（无标签，自动分组）
│   │   └── 用户分群、异常检测
│   │
│   └── 降维（压缩特征，可视化）
│       └── PCA、t-SNE
│
├── 按学习方式分
│   ├── 监督学习（有标签）← 你现在学的
│   ├── 无监督学习（无标签）
│   ├── 半监督学习（少量标签）
│   └── 强化学习（奖惩机制）
│
└── 按模型家族分
    │
    ├── 🟦 线性家族（linear_model）
    │   线性回归 → 预测数字
    │   逻辑回归 → 二分类概率
    │   Ridge/Lasso/ElasticNet → 防过拟合
    │   多项式回归 → 曲线关系
    │   【适合：数据线性、需要解释】
    │
    ├── 🟩 树家族（tree + ensemble）
    │   决策树 → 分类/回归
    │   随机森林 → Bagging，稳
    │   XGBoost/LightGBM → Boosting，准（比赛首选）
    │   【适合：非线性、表格数据、不知道用啥先试它】
    │
    ├── 🟧 距离家族（neighbors）
    │   KNN 分类 → 随大流投票
    │   KNN 回归 → 随大流均值
    │   【适合：小数据、需标准化】
    │
    ├── 🟪 概率家族（naive_bayes）
    │   GaussianNB → 连续值
    │   MultinomialNB → 文本分类
    │   【适合：文本、特征独立场景】
    │
    ├── 🟥 边界家族（svm）
    │   SVC（linear/poly/rbf核）→ 找最优分界线
    │   【适合：高维、非线性、小样本】
    │
    └── 🔲 神经网络家族（neural_network）
        MLPClassifier → 多层感知机
        → 再往上：深度学习（PyTorch）→ LLM
        【适合：大数据、复杂模式】

拿到数据
    │
    ├── 预测数字？ → 回归
    │   ├── 数据呈直线 → 线性回归
    │   ├── 有弯曲 → 多项式回归
    │   ├── 特征太多可能过拟合 → Ridge/Lasso
    │   └── 万能 → 随机森林回归
    │
    ├── 判断类别？ → 分类
    │   ├── 文本数据 → MultinomialNB（先试）
    │   ├── 需要解释理由 → 逻辑回归 + 决策树
    │   ├── 不知道用啥 → 随机森林（基线）
    │   ├── 要最高精度 → XGBoost
    │   └── 小样本 + 特征干净 → KNN 或 SVM
    │
    └── 没有标签？ → 聚类
        └── KMeans（暂未学）

## 下次继续
```
继续学习，请读取：
1. progress/python-tracker.md
2. sessions/2026-05-10/session-notes.md

今天复习了 ML 模板裸写，下次可以：
- 决策树对比（5_9task.py 只写了 LR，还没加 DT）
- 课件 32（SVM 等新模型）
- 或继续换数据集练模板
```
