import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文显示
plt.rcParams['axes.unicode_minus'] = False     # 负号正常显示

# ========== 1. 造数据 ==========
# make_classification：生成分类任务的数据（n_samples条，n_features个特征，n_classes个类别）
X, y = make_classification(
    n_samples=50,     # 50 个样本
    n_features=8,     # 8 个特征
    n_classes=2,      # 2 个类别（0 和 1）
    random_state=30   # 固定随机种子，每次生成的数据一样
)

# ========== 2. 划分训练集/测试集 ==========
# 返回顺序是固定的：X训练, X测试, y训练, y测试
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,    # 20% 作为测试集
    random_state=42   # 固定划分方式
)

print("aim:", y_test)  # 真实标签（用来和预测结果对比）

# ========== 3. 标准化 ==========
# 把数据缩放到均值≈0、方差≈1，让不同特征之间可比
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)   # 训练集：计算均值和标准差 + 转换
X_test = scaler.transform(X_test)         # 测试集：只用训练集的均值/标准差来转换（不能偷看测试集）

# ========== 4. 建 KNN 模型 ==========
# KNN：找最近的 K 个邻居，它们大多数是什么，新样本就是什么
model = KNeighborsClassifier(
    n_neighbors=8,          # K=5，看最近的 5 个邻居
    metric='euclidean'      # 距离公式：直线距离
)
# metric 可选：
#   'euclidean' — 直线距离（最常用）
#   'manhattan'  — 横竖走距离（城市街区距离）
#   'cosine'     — 余弦相似度（看方向不看长度）

# ========== 5-7. 训练 + 预测 + 评估（手动调参） ==========
print("\n--- K值对比 ---")
best_k = 1
best_acc = 0
k_list = []      # 存所有 K 值
acc_list = []    # 存对应的准确率

for k in [1, 3, 5, 8, 10, 15, 20]:# 代码自动调参
    model = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    k_list.append(k)        # 记录 K 值
    acc_list.append(acc)    # 记录准确率

    mark = " ← 最优" if acc > best_acc else ""
    if acc > best_acc:
        best_acc = acc
        best_k = k
    print(f"K={k:2d}  |  Accuracy: {acc:.4f}{mark}")

print(f"\n最佳 K={best_k}，准确率={best_acc:.4f}")

# ========== 8. 画图 ==========
plt.plot(k_list, acc_list, marker='o', color='blue')
plt.xlabel('K 值')          # x轴标签
plt.ylabel('准确率')        # y轴标签
plt.title('KNN: K值 vs 准确率')  # 标题
plt.xticks(k_list)          # x轴刻度显示所有K值
plt.grid(True, alpha=0.3)   # 网格线（半透明）
plt.show()
