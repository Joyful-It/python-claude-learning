# 学习会话记录 - 2026-05-09

## 会话概览
- 日期：2026-05-09
- 形式：一对一教学
- 核心主题：sklearn机器学习实操（贝叶斯/KNN/模型对比/调参/可视化）

## 学员提出的问题/需求
1. 总结上次（2026-04-28）以来的神经网络/深度学习知识点
2. 学习千峰课件三个PDF（机器学习一、二、三）
3. 理解"搞透"代码的四关标准
4. 理解 random_state、test_size 含义
5. 学习朴素贝叶斯4种类型
6. 学习 KNN + 调参 + 画准确率曲线
7. 对代码感到生疏，询问学习方法

## 讲解的概念与教学过程

### 1. sklearn 机器学习流程（万能模板）
```
1. 加载数据    → load_xxx() 或 make_classification()
2. 划分        → train_test_split(X, y, test_size=0.2)
3. 标准化(可选) → StandardScaler → fit_transform / transform
4. 建模型      → XxxModel()
5. 训练        → model.fit(X_train, y_train)
6. 预测        → model.predict(X_test)
7. 评估        → accuracy_score(y_test, y_pred)
```

### 2. 搞透四关
```
第一关：能解释每行代码在干什么
第二关：能改参数，知道后果
第三关：能换数据集，独立跑通
第四关：能对比不同模型，说出谁好谁坏
```

### 3. random_state 理解
- 固定随机抽签顺序，让每次运行结果可复现
- 数字本身无意义（42、0、123都一样）

### 4. test_size 理解
- 0.2 = 20%测试集，0.5 = 50%测试集

### 5. train_test_split 返回顺序
- 固定顺序：X_train, X_test, y_train, y_test
- 学员曾写错顺序导致报错

### 6. 模型对比（逻辑回归 vs 决策树）
- 鸢尾花太简单，两者都1.0（分不出高下）
- 乳腺癌数据集更难，逻辑回归略高

### 7. 朴素贝叶斯 4 种类型
| 类型 | 适用数据 | 鸢尾花效果 |
|------|---------|-----------|
| GaussianNB | 连续值 | 1.0 ✅ |
| BernoulliNB | 0/1值 | 0.25 ❌ |
| MultinomialNB | 计数 | 0.95 ⚠️ |
| ComplementNB | 不平衡计数 | 0.65 ❌ |

### 8. KNN（K近邻）
- 核心：找最近的K个邻居，看它们大多数是什么
- metric='euclidean'（直线距离）
- 还有 manhattan、cosine

### 9. 手动调参 vs 自动调参
- 手动：for循环试不同K值
- 自动：GridSearchCV（待学）

### 10. matplotlib 画图
- plt.plot(x, y, marker='o')
- plt.xlabel/ylabel/title
- plt.show()
- 中文乱码：plt.rcParams['font.sans-serif'] = ['SimHei']

## 完成的练习
1. ✅ 鸢尾花 + 逻辑回归 + 决策树对比
2. ✅ 乳腺癌 + 逻辑回归 vs 决策树
3. ✅ 朴素贝叶斯4种对比（NB1.py）
4. ✅ KNN + 手动调参 + 准确率曲线图（KNN_demo1.py）

## 识别的知识漏洞
- 代码不够熟练，依赖参考（主要问题）
- matplotlib 语法不熟
- SVM 还没学
- 验证集概念不熟（只知训练集/测试集）
- make_classification 参数不熟
- 文本情感分析完全不会

## 学习方法讨论
- 建议采用"模板学习法"：死记8步流程，具体模型名/参数随时查
- 通过换数据集、换模型反复套模板来熟练
- AI时代不背语法，记流程和思路

## 待做练习题
1. ✅ KNN画准确率曲线（已做）
2. ❌ SVM不同核函数对比
3. ❌ 朴素贝叶斯文本情感分析

## 学习效果评估
- sklearn ML流程：已理解，手写还不熟练
- KNN调参：已理解原理
- 朴素贝叶斯：知道4种类型区别
- 整体状态：套模板能力提升，需更多独立练习

---

## 下次继续
```
继续学习，请读取：
1. progress/python-tracker.md
2. sessions/2026-05-09/session-notes.md

上次学完发现：
- 模板已基本掌握，需独立默写练习
- SVM还没学
- 文本情感分析还没碰
```
