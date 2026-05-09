from sklearn.datasets import load_iris#导入数据集
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
iris=load_iris()#加载数据集

x=iris.data  #特征花的
y=iris.target#目标变量，花的品种
print("特征名称：",iris.feature_names)
print("标签名称：",iris.target_names)
print("x shape:",x.shape)
print("y shape",y.shape)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5,random_state=42)

# random_state = 固定随机抽签顺序
# ✅ 让实验结果可复现
# ✅ 方便调试和对比模型
# ✅ 避免随机因素干扰结论

# 逻辑回归
model=LogisticRegression(max_iter=200)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
acc=accuracy_score(y_test,y_pred)
print("逻辑回归 Accuracy:", acc)

# 决策树
model_dt = DecisionTreeClassifier(max_depth=3, random_state=42)
model_dt.fit(x_train, y_train)
y_pred_dt = model_dt.predict(x_test)
acc_dt = accuracy_score(y_test, y_pred_dt)
print("决策树 Accuracy:", acc_dt)
# 数据
# ↓
# 特征 X 和标签 y
# ↓
# 划分训练集、验证集、测试集
# ↓
# 选择模型
# ↓
# fit 训练
# ↓
# predict 预测
# ↓
# 评估指标判断好坏
# ↓
# 调参改进



