import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ===================== 1. 数据加载与预处理 =====================
# 1.1 加载数据（把路径改成你自己的train.csv路径）
df = pd.read_csv('C:/project/python/torch_pre/train.csv')

# 1.2 特征工程：选取指定特征和标签
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
X = df[features].copy()
y = df['Survived']  # 标签：0=遇难，1=幸存

# 1.3 处理缺失值
# Age用中位数填充 不受极端值影响
X['Age'] = X['Age'].fillna(X['Age'].median())
# Embarked用众数填充 字母只能用数量最多的表示
X['Embarked'] = X['Embarked'].fillna(X['Embarked'].mode()[0])

# 1.4 特征编码
# Sex映射为0/1：male=0, female=1
X['Sex'] = X['Sex'].map({'male': 0, 'female': 1})
# Embarked进行One-Hot编码   将字母编程数字的手段   一行一个1 剩下全是0
X = pd.get_dummies(X, columns=['Embarked'], drop_first=False)

# 1.5 切分训练集和验证集（8:2） 
# stratify=y 按照y的比例去分配，如果y存活和没有存活是是4比6分，那训练集测试集也是这样
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 1.6 标准化：对Age和Fare进行标准化（神经网络对尺度敏感）
scaler = StandardScaler()
# 只在训练集上拟合，避免数据泄露
X_train = X_train.copy()
X_val = X_val.copy()
X_train[['Age', 'Fare']] = scaler.fit_transform(X_train[['Age', 'Fare']])
X_val[['Age', 'Fare']] = scaler.transform(X_val[['Age', 'Fare']])

# 打印最终特征维度
print(f"最终输入特征维度: {X_train.shape[1]}")
print(f"训练集大小: {len(X_train)}, 验证集大小: {len(X_val)}")
print(f"\nX_train 列类型:\n{X_train.dtypes}")

# ===================== 2. 构建PyTorch数据集 =====================
class TitanicDataset(Dataset):
    def __init__(self, X, y):
        # 转换为numpy数组，再转成torch张量
        self.X = torch.tensor(X.values.astype(np.float32), dtype=torch.float32)
        self.y = torch.tensor(y.values.astype(np.float32), dtype=torch.float32).view(-1, 1)  # 形状转为[batch_size, 1]
    
    def __len__(self):
        return len(self.X)
    
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# 创建数据集和数据加载器
train_dataset = TitanicDataset(X_train, y_train)
val_dataset = TitanicDataset(X_val, y_val)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

# ===================== 3. 构建神经网络模型 =====================
class TitanicNN(nn.Module):
    def __init__(self, input_dim=9):
        super(TitanicNN, self).__init__()
        # 输入层 → 隐藏层1（128个神经元）
        self.fc1 = nn.Linear(input_dim, 128)
        # 隐藏层1 → 隐藏层2（64个神经元）
        self.fc2 = nn.Linear(128, 64)
        # 隐藏层2 → 输出层（1个神经元，二分类）
        self.fc3 = nn.Linear(64, 1)
        # 激活函数
        self.relu = nn.ReLU()
    
    def forward(self, x):
        # 前向传播
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        # 输出层不加Sigmoid，配合BCEWithLogitsLoss使用（数值更稳定）
        x = self.fc3(x)
        return x

# 实例化模型
model = TitanicNN()
print("\n模型结构:")
print(model)

# ===================== 4. 训练配置 =====================
# 损失函数：二分类用BCEWithLogitsLoss（内部包含Sigmoid）
criterion = nn.BCEWithLogitsLoss()
# 优化器：Adam，学习率0.001
optimizer = optim.Adam(model.parameters(), lr=0.001)
# 训练轮数
num_epochs = 30
# 设备：有GPU用GPU，没有用CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

# ===================== 5. 训练与评估循环 =====================
print("\n开始训练...")
for epoch in range(num_epochs):
    # ---------------------- 训练阶段 ----------------------
    model.train()
    train_loss = 0.0
    train_correct = 0
    train_total = 0
    
    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)
        
        # 1. 前向传播
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        
        # 2. 反向传播与参数更新
        optimizer.zero_grad()  # 清空梯度
        loss.backward()        # 计算梯度
        optimizer.step()       # 更新参数
        
        # 统计训练指标
        train_loss += loss.item() * inputs.size(0)
        # 预测：输出>0.5为1（幸存），否则为0（遇难）
        predicted = (torch.sigmoid(outputs) > 0.5).float()
        train_total += labels.size(0)
        train_correct += (predicted == labels).sum().item()
    
    # 计算训练集平均损失和准确率
    train_loss = train_loss / len(train_dataset)
    train_acc = train_correct / train_total
    
    # ---------------------- 验证阶段 ----------------------
    model.eval()
    val_loss = 0.0
    val_correct = 0
    val_total = 0
    
    # 验证时不需要计算梯度
    with torch.no_grad():
        for inputs, labels in val_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            
            val_loss += loss.item() * inputs.size(0)
            predicted = (torch.sigmoid(outputs) > 0.5).float()
            val_total += labels.size(0)
            val_correct += (predicted == labels).sum().item()
    
    val_loss = val_loss / len(val_dataset)
    val_acc = val_correct / val_total
    
    # 打印每个epoch的结果
    print(f"Epoch [{epoch+1}/{num_epochs}]")
    print(f"训练损失: {train_loss:.4f} | 训练准确率: {train_acc:.4f}")
    print(f"验证损失: {val_loss:.4f} | 验证准确率: {val_acc:.4f}\n")

print("✅ 训练完成！")
print(f"最终验证集准确率: {val_acc:.4f}")