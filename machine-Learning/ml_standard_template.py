"""
ML 标准五步模板
目标：让模型在没见过的数据上准确预测（泛化）
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, accuracy_score, classification_report

# ============================================================
# 第一步：选择模型结构
# ============================================================
# 看数据长什么样 → 选模型
#   线性关系 → 线性回归 / 逻辑回归          (wx+b)
#   非线性   → 决策树 / 随机森林 / 神经网络  (树切分 / 激活折弯)
#   分类问题 → 逻辑回归 / 树 / KNN / SVM

# ============================================================
# 第二步：定义损失函数（衡量预测和真实差多少）
# ============================================================
# 回归：MSE = (1/n) × Σ(ŷ - y)²    平方罚大错
#       MAE = (1/n) × Σ|ŷ - y|     绝对值，不理离群点
# 分类：交叉熵 = -[y×log(ŷ) + (1-y)×log(1-ŷ)]  罚方向对不对

# ============================================================
# 第三步：加约束（正则化 → 防过拟合）
# ============================================================
# 频率派做法：损失里直接加惩罚项
#   Ridge = MSE + α × Σw²      （L2：w 趋近 0）
#   Lasso = MSE + α × Σ|w|     （L1：不重要 w 直接变 0）
# 贝叶斯派做法：给 w 加先验分布 → 数学上等价于上面
#   Gaussian先验 → L2 / Ridge
#   Laplace先验  → L1 / Lasso

# ============================================================
# 第四步：优化 → 找到最好的 w
# ============================================================
# 有解析解：线性回归直接公式算（最小二乘法）
# 没解析解：梯度下降一步步走
#   w_new = w_old - lr × 梯度        lr=学习率，控制步长
#   sklearn 里 fit() 帮你全干了

# ============================================================
# 第五步：评估 → 在没见过的数据上测泛化能力
# ============================================================
# 回归看：MSE / MAE / R²
# 分类看：Accuracy / Recall / Precision / F1


# ============================================================
# 完整实操：用 Ridge 回归预测房价（回归问题）
# ============================================================
print("=" * 50)
print("示例：回归任务（Ridge）")
print("=" * 50)

# 造数据：房价 ≈ 面积×3 + 房间数×10 + 噪音
np.random.seed(42)
n = 200
area = np.random.uniform(30, 200, n)          # 面积 30-200 平米
rooms = np.random.randint(1, 6, n)             # 房间 1-5 个
noise = np.random.normal(0, 15, n)             # 随机噪音
price = area * 3.0 + rooms * 10.0 + noise + 50  # 真实公式（模型不知道）

X = pd.DataFrame({'area': area, 'rooms': rooms})
y = price

# 切数据：训练集（学）+ 测试集（验）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---- 第一步：选模型 ---- #
# 数据是线性的（面积/房间 → 房价），用线性回归/Ridge
model = Ridge(alpha=1.0)  # alpha=λ，L2 正则化强度

# ---- 第四步：fit() 里内置了损失(MSE+L2)+梯度下降，一步到位 ---- #
model.fit(X_train, y_train)

# 看看学到了什么
print(f"真实公式: price = 50 + 3.0×area + 10.0×rooms")
print(f"模型学到的: w_area={model.coef_[0]:.2f}, w_rooms={model.coef_[1]:.2f}, b={model.intercept_:.2f}")

# ---- 第五步：评估 ---- #
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"测试集 MSE: {mse:.2f}")


# ============================================================
# 再一个：用逻辑回归做分类（加 L2 正则化）
# ============================================================
print("\n" + "=" * 50)
print("示例：分类任务（逻辑回归 + L2）")
print("=" * 50)

# 造数据：根据两门分数判断是否录取
np.random.seed(42)
n = 300
score1 = np.random.normal(70, 15, n)
score2 = np.random.normal(65, 12, n)
# 总分 > 140 的大概率录取，加噪音
admit = ((score1 * 0.5 + score2 * 0.5 + np.random.normal(0, 8, n)) > 70).astype(int)

X_clf = pd.DataFrame({'score1': score1, 'score2': score2})
y_clf = admit

Xc_train, Xc_test, yc_train, yc_test = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42)

# ---- 第一步：分类问题 → 逻辑回归 ---- #
# ---- 第三步：C=1.0 就是加 L2（越大正则化越弱） ---- #
model_clf = LogisticRegression(C=1.0, max_iter=1000)  # C 是 λ 的倒数
model_clf.fit(Xc_train, yc_train)

# ---- 第五步 ---- #
yc_pred = model_clf.predict(Xc_test)
print(f"准确率 Accuracy: {accuracy_score(yc_test, yc_pred):.2f}")
print(f"\n详细报告:\n{classification_report(yc_test, yc_pred, target_names=['不录取', '录取'])}")
