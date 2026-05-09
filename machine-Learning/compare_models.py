# 对比逻辑回归 vs 决策树（乳腺癌数据集，更难）
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. 加载数据（569条，30个特征，比鸢尾花难）
X, y = load_breast_cancer(return_X_y=True)
print("X shape:", X.shape, "| 样本数:", X.shape[0], "| 特征数:", X.shape[1])

# 2. 划分
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. 逻辑回归
lr = LogisticRegression(max_iter=5000)
lr.fit(X_train, y_train)
acc_lr = accuracy_score(y_test, lr.predict(X_test))
print(f"逻辑回归 Accuracy: {acc_lr:.4f}")

# 4. 决策树
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train, y_train)
acc_dt = accuracy_score(y_test, dt.predict(X_test))
print(f"决策树   Accuracy: {acc_dt:.4f}")

# 5. 对比
if acc_lr > acc_dt:
    print("→ 逻辑回归更准")
elif acc_dt > acc_lr:
    print("→ 决策树更准")
else:
    print("→ 平手")
