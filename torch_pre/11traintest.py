"""
泰坦尼克号 PyTorch 完整流程（进阶版 + 逐行注解）
基于 10taitan.py 改进：Has_Cabin 提取 + 分组填 Age + 衍生特征 + 正确标准化顺序
"""
# ── 导入 ──────────────────────────────────────────────
# torch：整个 PyTorch 框架
# nn：神经网络层（Linear/ReLU/BCEWithLogitsLoss 都在里面）
# Dataset：告诉模型"第 i 个样本长什么样"
# DataLoader：把样本按 batch 打包，送进训练循环
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# numpy：PyTorch 的 tensor 和 numpy 数组可以互相转，数据处理阶段 numpy 更方便
import numpy as np
import pandas as pd

# train_test_split：一刀切分训练集/验证集
# StandardScaler：让数值列变成均值=0 方差=1，神经网络训练才稳定
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# ==================== ① 读取数据 ====================
# read_csv 返回 DataFrame，行列都有标签，比纯 numpy 直观
df = pd.read_csv('torch_pre/train.csv')


# ==================== ② 特征工程 ====================
# 为什么"全局做"？缺失值填充和衍生特征的逻辑不依赖切分结果，
# 先做一个统一的数据源，后面切分省事且不出错。

# ── Cabin：提取"有无船舱"而非直接扔掉 ──
# 为什么这样做？Cabin 列 891 行缺了 687（77%），直接填不靠谱。
# 但"有没有船舱号"本身就是信息——有船舱 = 高舱位/高社会地位 → 存活率更高。
# pd.notna(x) 判断是否非空（NaN 就是空），非空=1 有空=0
df['Has_Cabin'] = df['Cabin'].apply(lambda x: 1 if pd.notna(x) else 0)
# drop 删除原 Cabin 列，axis=1 表示删列（axis=0 是删行），inplace=True 原地修改不返回新对象
df.drop('Cabin', axis=1, inplace=True)

# ── 扔掉无关列 ──
# PassengerId：纯行号，1到891，和存活率零关系
# Name：文本乱码，名字里有头衔(Mr/Mrs/Captain)但不做 NLP 就无意义
# Ticket：长短不一的票号字符串，无规律
df.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)

# ── Age：分组填中位数 ──
# 为什么分组填？一等舱女性(富婆)和三等舱男性(劳工)年龄分布完全不同。
# 全局中位数会把头等舱老太太和三等舱小伙混在一起填，不精准。
# groupby(['Pclass','Sex'])：按舱位+性别分组
# transform('median')：每组算自己的中位数，返回和原 df 等长的 Series（广播回去）
# 为什么用中位数不用均值？年龄有极端值（0岁婴儿/80岁老人），均值会被拉偏，中位数稳
age_median = df.groupby(['Pclass', 'Sex'])['Age'].transform('median')
# fillna 填缺失，inplace=True 原地修改
df['Age'].fillna(age_median, inplace=True)

# ── Embarked：填众数 ──
# 为什么用众数？Embarked 是分类变量（S/C/Q 三个码头），分类变量填"出现最多的那个"最合理
# mode() 返回众数 Series，可能有并列，[0] 取第一个
# 缺失只有 2 个（0.2%），填什么都不影响大局
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# ── 衍生特征：FamilySize ──
# 为什么做？SibSp(兄弟姐妹)+Parch(父母子女) 单独看不如加起来有意义。
# +1 是把本人也算上。FamilySize=1 = 独自登船，4 = 四口之家。
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# ── 衍生特征：FamilyType ──
# 为什么分三档？独自(1)、小家庭(2-4)、大家庭(5+)——生存模式完全不同。
# 独自的人可能逃生更灵活，大家庭可能团灭也可能互相救助。
# apply(lambda) 对每行执行一次，s=FamilySize 的数值 → 返回 0/1/2
df['FamilyType'] = df['FamilySize'].apply(
    lambda s: 0 if s == 1 else (1 if s <= 4 else 2)
)

# ── 衍生特征：AgeGroup ──
# 为什么分组？年龄和存活不是线性关系——小孩和老人先上救生艇，壮年男性最后。
# 分组让模型更容易学到这种阶梯关系。
# <12(儿童) 12-29(青年) 30-59(壮年) 60+(老人) = 四档
df['AgeGroup'] = df['Age'].apply(
    lambda a: 0 if a < 12 else (1 if a < 30 else (2 if a < 60 else 3))
)

# ── Sex 编码：map 手动映射 ──
# 为什么 map 不用 One-Hot？Sex 只有男女两值，一列 0/1 就够，多开一列浪费。
# 神经网络里 One-Hot 也行，但二分类手动映射更简洁。
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# ── Embarked 编码：One-Hot ──
# 为什么 One-Hot？S/C/Q 三个值没法排大小（S>C>Q 没意义），拆成三列 0/1 最安全。
# 为什么 drop_first=False？统计模型（逻辑回归）丢第一列防多重共线性；
# 神经网络全连接会自动学权重，三列全保留让模型信息完整。
# prefix='Embarked'：新列命名为 Embarked_C, Embarked_Q, Embarked_S
df = pd.get_dummies(df, columns=['Embarked'], prefix='Embarked', drop_first=False)


# ==================== ③ 挑出 X 和 y ====================
# feature_cols：所有参与预测的列名清单（13 个特征）
feature_cols = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare',
                'Has_Cabin', 'FamilySize', 'FamilyType', 'AgeGroup',
                'Embarked_C', 'Embarked_Q', 'Embarked_S']

# .copy() 断开与原 df 的引用链。
# 不加的话 X 只是 df 的一个"窗口"，后面改 X_train 会触发 SettingWithCopyWarning
X = df[feature_cols].copy()
y = df['Survived'].copy()


# ==================== ④ 切分训练/验证集 ====================
# test_size=0.2：80%训练 20%验证
# stratify=y：按存活比例分层抽样。
#   比如原始 存活:遇难=38:62 → 切完后训练/验证集里也是 38:62。
#   不加 stratify 的话极端情况验证集里可能全是遇难者，评估就歪了。
# random_state=42：固定随机种子，每次运行切出同样的结果，可复现。
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)


# ==================== ⑤ 标准化 ====================
# 为什么只标准化这三列？Age/Fare/FamilySize 是连续数值，量纲差异大
# (Fare 最大 512，Age 最大 80)，神经网络对此敏感——量纲大的列梯度也大，训练不稳。
# Pclass/Sex/One-Hot 等 0/1 列不需要标准化——它们本身就是标准化的。
scale_cols = ['Age', 'Fare', 'FamilySize']

# StandardScaler：公式 (x - mean) / std，使每列均值≈0 方差≈1
scaler = StandardScaler()

# 再次 copy——train_test_split 返回的也可能是视图，后续修改会报警
X_train = X_train.copy()
X_val = X_val.copy()

# fit_transform：两步合一——fit 算出均值+方差，transform 用它们做标准化
# 为什么只在 X_train 上 fit？
#   如果用全部数据 fit → 验证集的信息"泄露"到训练阶段 → 评估分数虚高。
#   现实场景中模型上线前不可能看到未来数据，fit_transform(train) 模拟这个约束。
X_train[scale_cols] = scaler.fit_transform(X_train[scale_cols])

# transform：用训练集的均值和方差来标准化验证集
# 如果这里也 fit_transform → 验证集自己算了一套标准 → 两套标准不统一 → 失去可比性
X_val[scale_cols] = scaler.transform(X_val[scale_cols])


# ==================== ⑥ 转 PyTorch Tensor ====================
# 为什么 .astype(np.float32)？
#   DataFrame 里可能有 int64/bool/object 混合类型，.values 会变成 object 数组。
#   torch.tensor() 不接受 object 数组 → 必须先统一为 float32。
#   同时 GPU 上的 PyTorch 默认 float32，和模型权重数据类型一致。
# 为什么 .view(-1, 1)？把 y 从一维 (batch,) 变成二维 (batch, 1)。
#   BCEWithLogitsLoss 要求 y 的形状和预测值 y_pred 完全一致——y_pred 是 (batch, 1)。
X_train_t = torch.tensor(X_train.values.astype(np.float32), dtype=torch.float32)
X_val_t   = torch.tensor(X_val.values.astype(np.float32),   dtype=torch.float32)
y_train_t = torch.tensor(y_train.values.astype(np.float32), dtype=torch.float32).view(-1, 1)
y_val_t   = torch.tensor(y_val.values.astype(np.float32),   dtype=torch.float32).view(-1, 1)

print(f"X_train: {X_train_t.shape}, y_train: {y_train_t.shape}")
print(f"X_val:   {X_val_t.shape},   y_val:   {y_val_t.shape}")
print(f"特征数: {X_train_t.shape[1]}")


# ==================== ⑦ Dataset + DataLoader ====================
# 为什么需要 Dataset？
#   直接给 tensor 没法控制"第 i 个样本返回什么"。
#   Dataset = 厨师备菜——定义 __len__(总样本数) 和 __getitem__(取第 idx 个)。
#   训练循环里 for 循环每次拿到一个 (X, y) 对。
class TitanicDataset(Dataset):
    def __init__(self, X, y):
        # 构造函数：接收已经处理好的 tensor，存起来
        self.X = X
        self.y = y

    def __len__(self):
        # DataLoader 问"一共多少样本？"→ Dataset 答长度
        return len(self.X)

    def __getitem__(self, idx):
        # DataLoader 问"第 idx 个是啥？"→ Dataset 返回 (特征, 标签)
        return self.X[idx], self.y[idx]

train_ds = TitanicDataset(X_train_t, y_train_t)
val_ds   = TitanicDataset(X_val_t,   y_val_t)

# 为什么需要 DataLoader？
#   Dataset 只管单个样本，DataLoader 负责批量打包。
#   batch_size=32：每次送 32 个样本给 GPU，太大→显存不够，太小→梯度不稳定
#   shuffle=True(训练)：每轮打乱顺序 → 梯度方向更多样 → 不容易过拟合 → 收敛更快
#   shuffle=False(验证)：不打乱，评估不需要，保持顺序也不影响结果
train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
val_loader   = DataLoader(val_ds,   batch_size=32, shuffle=False)


# ==================== ⑧ 定义模型 ====================
# 为什么用 Sequential？
#   数据单向流动（输入→隐藏→隐藏→输出），Sequential 最简洁。
#   不用自己写 forward 里一层层调用。
# 为什么 128→64？
#   逐层递减是常见设计：先升维充分提取信息，再逐步压缩到 1 维输出。
#   13 → 128 → 64 → 1，参数总量 ≈ 13×128+128+128×64+64+64×1+1 ≈ 10k（非常小）
# 为什么中间用 ReLU？
#   没有激活函数 → 多层线性叠加 = 一层线性 → 白堆了。
#   ReLU：负值清零，正值保留，引入非线性，计算快（比 sigmoid/tanh 快几十倍）。
# 为什么最后一层不加激活？
#   BCEWithLogitsLoss 内部包含了 sigmoid，模型输出原始 logit 就行。
#   分开写（sigmoid+BCE）数值不稳定，合并在 loss 里 PyTorch 做了数值优化。
class TitanicModel(nn.Module):
    def __init__(self, in_features):
        super().__init__()  # 必须调用父类 nn.Module 的构造函数，否则参数注册不上
        self.net = nn.Sequential(
            nn.Linear(in_features, 128),  # 全连接：in→128，公式 y = x@W^T + b
            nn.ReLU(),                     # ReLU(x) = max(0, x)
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1)              # 输出 1 个 logit（未经 sigmoid 的原始值）
        )

    def forward(self, x):
        # forward 定义了前向传播路径。
        # model(x) 实际调用的是 forward(x)——__call__ 方法内部转发的
        return self.net(x)

# 实例化模型，in_features 取训练集的特征列数（13）
# 为什么动态取而不是写死？删除/新增特征后自动适配，不用改代码
model = TitanicModel(in_features=X_train_t.shape[1])


# ==================== ⑨ 训练配置 ====================
# BCEWithLogitsLoss = Sigmoid + BCELoss 合体。
#   BCELoss 算二分类交叉熵：-(y*log(p) + (1-y)*log(1-p))
#   先 sigmoid 再 BCE 有数值溢出风险，合体版内部用 log-sum-exp 技巧防炸。
# reduction='mean'（默认）：对 batch 求平均损失。
criterion = nn.BCEWithLogitsLoss()

# Adam：自适应学习率优化器。
#   普通 SGD 学习率固定，Adam 对每个参数单独调学习率——梯度大的参数少走，小得多走。
#   效果：收敛快，不用手动调学习率衰减。
# lr=0.001：Adam 默认学习率，大部分场景开箱即用。
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# epochs=100：数据量小(712训练样本)，100 轮跑不出过拟合（模型才 10k 参数）
epochs = 100


# ==================== ⑩ 训练循环 ====================
# 五步口诀：forward → loss → zero_grad → backward → step
for epoch in range(epochs):

    # ═══ 训练阶段 ═══
    model.train()  # 开启训练模式。Dropout/BatchNorm 会生效（虽然这里没用到）。
    train_loss = 0
    for X_batch, y_batch in train_loader:
        # ① forward：模型预测
        y_pred = model(X_batch)           # y_pred 形状 (32, 1)，是未经过 sigmoid 的 logit

        # ② loss：算差距
        loss = criterion(y_pred, y_batch)

        # ③ zero_grad：清空上一步的梯度缓存。
        #   为什么必须清？PyTorch 梯度默认累加，不清的话这次梯度加在上次上面→步长越来越大→训练崩
        optimizer.zero_grad()

        # ④ backward：反向传播，自动求每个参数的梯度（链式法则，从 loss 一路穿回第一层）
        loss.backward()

        # ⑤ step：按梯度和学习率更新所有参数 w = w - lr * grad
        optimizer.step()

        # loss.item()：取出 tensor 里的纯数字，并累加用于算平均
        train_loss += loss.item()

    # ═══ 验证阶段 ═══
    model.eval()  # 开启评估模式。关闭 Dropout，固定 BN 均值（这里没用到但养成习惯）
    val_loss = 0
    correct = 0   # 预测正确的样本数
    total = 0     # 验证集总样本数
    with torch.no_grad():  # 禁用梯度计算。
        # 为什么？验证不需要反向传播，关闭 autograd 省显存、加速计算
        for X_batch, y_batch in val_loader:
            y_pred = model(X_batch)
            val_loss += criterion(y_pred, y_batch).item()

            # sigmoid 把 logit 压到 0~1 → >0.5 判为存活(1)，否则遇难(0)
            preds = (torch.sigmoid(y_pred) > 0.5).float()
            correct += (preds == y_batch).sum().item()
            total += y_batch.size(0)  # y_batch.size(0) = batch 内样本数

    # 每 10 轮打印一次，省得刷屏
    # epoch+1 因为 range(100) 从 0 开始，人看习惯从 1 开始
    if (epoch + 1) % 10 == 0:
        print(f"Epoch {epoch+1:3d} | train_loss={train_loss/len(train_loader):.4f} | "
              f"val_loss={val_loss/len(val_loader):.4f} | val_acc={correct/total:.4f}")
