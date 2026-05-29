# AI大模型开发之38PyTorch全连接神经网络

> 作者：AI芯源邢朋辉

# 0.课程内容

## 0.1晨考



## 0.2 课程回顾

# 1.Pytorch

## 一、PyTorch神经网络实操

### 1.PyTorch核心特性

动态计算图（Define-by-Run）：前向传播时动态构建计算图，每个操作立即执行，支持 pdb 调试，灵活易用。

Pythonic 设计：API 遵循 Python 惯例（如 add_() 表示原地操作），与 NumPy 高度兼容，深层集成 Python 生态（pickle、multiprocessing）。

相比 TensorFlow  静态图的优势：调试方便、代码简洁、适合研究。

### 2.张量（Tensor）基本语义

0维：标量（loss损失）

1维：向量（特征）

2维：矩阵（权重）

3维：序列（文本批次）

4维：图像批次 [batch, channel, height, width]

### 3.设备与数据类型

device='cpu' / 'cuda:0'；

GPU 张量不可直接转 NumPy（需先 .cpu()）。

dtype：常见 float32、float16、int64。

混合精度训练用 float16 + float32。

### 4.自动微分 Autograd

反向模式自动微分：适合多输入单输出的神经网络。

叶子张量：用户创建且 requires_grad=True 的张量，梯度保留在 .grad 中。

非叶子节点：中间计算结果，梯度默认释放（为节省内存）。

### 5.nn.Module

所有网络需继承 nn.Module，实现 **init**（定义层）和 forward（数据流向，前向传播）。

参数自动注册：nn.Parameter 和子模块自动被 parameters() 收集。

使用 model(x) 调用 forward，不要直接 model.forward(x)（**call** 会添加钩子）。

钩子函数：前向传播和反向传播

## 二、API

## 1. 张量创建与操作

```python
# 创建
torch.tensor([1])          # 从列表
torch.zeros(2,3)             # 全零
torch.ones(2,3)              # 全一
torch.randn(2,3)             # 标准正态
torch.arange(0,10,2)         # 等差数列
torch.linspace(0,1,5)        # 等间隔

# 形状变换
reshape vs view：view 要求内存连续，reshape 自动处理连续性
transpose / permute：交换维度，permute 可同时排列多个轴
squeeze / unsqueeze：移除/增加 size=1 的维度

# 数学运算
torch.matmul / @             # 矩阵乘法
torch.bmm                    # 批量矩阵乘法
.sum(dim=), .mean(dim=)      # 归约运算（keepdim 保持维度）
```

### 2. 自动微分

```python
x = torch.tensor(1.0, requires_grad=True)
y = x**2
y.backward()                 # 反向传播
x.grad                       # 获取梯度
```

- **梯度清零**：`optimizer.zero_grad()` 或在循环中 `p.grad = None`
- **梯度冻结**：`param.requires_grad = False`
- **梯度分离**：`z = y.detach()` 创建无梯度副本
- **上下文管理**：`with torch.no_grad():` 禁用梯度（推理/参数更新/评测）

示例：

```python
# 自动微分
import torch
x=torch.tensor(3.0,requires_grad=True)
# y=2x+x**3+5x**2=6+27+45
print(2*x+x**3+5*x**2)
y=2*x+x**3+5*x**2
# 反向
y.backward()
# 梯度值 偏导数的值
# y'=2+3*x**2+10x=2+27+30
print(x.grad)
```

![1779156471481](D:\class\2603\随堂笔记\第八周\AI大模型开发之38PyTorch全连接神经网络.assets\1779156471481.png)

### 3. 模型层（nn.xxx）

- `nn.Linear(in, out, bias=True)`：全连接
- `nn.Conv2d(in_ch, out_ch, kernel_size, stride, padding)`：2D卷积
- `nn.MaxPool2d / AvgPool2d / AdaptiveAvgPool2d`
- `nn.LSTM(input_size, hidden_size, num_layers, batch_first, bidirectional)`
- `nn.Embedding(num_embeddings, embedding_dim)`
- `nn.BatchNorm2d / LayerNorm / Dropout`

### 4. 激活函数 & 损失函数

| **用途**   | **常用**                                                     | **说明**              |
| ---------- | ------------------------------------------------------------ | --------------------- |
| 隐藏层     | `ReLU`, `LeakyReLU`, `GELU`                                  | GELU 用于 Transformer |
| 二分类输出 | `Sigmoid`                                                    | 输出 (0,1) 概率       |
| 多分类输出 | `Softmax` / `LogSoftmax`                                     | 互斥                  |
| 回归输出   | 无激活 / `Tanh`                                              | 范围限制              |
| 损失函数   | `MSELoss`, `L1Loss`, `CrossEntropyLoss`, `BCEWithLogitsLoss` |                       |

### 5. 优化器

```python
torch.optim.SGD(params, lr, momentum, weight_decay, nesterov)
torch.optim.Adam(params, lr, betas, weight_decay)
torch.optim.AdamW(params, lr, weight_decay)   # 修正权重衰减
```

### 6. 学习率调度

- `StepLR`, `ExponentialLR`, `CosineAnnealingLR`
- `ReduceLROnPlateau(monitor_mode, factor, patience)`
- 自定义：在 epoch 循环中手动修改 `param_group['lr']`

## 三、流程必会

### 1.标准四步法

1. **数据到设备**：`inputs, targets = inputs.to(device), targets.to(device)`
2. **前向传播**：`outputs = model(inputs); loss = criterion(outputs, targets)`
3. **反向传播**：`optimizer.zero_grad(); loss.backward()`
4. **参数更新**：`optimizer.step()`

> 一般都需要训练多次

### 2.验证模式

模型评测或评估

```python
model.eval()
with torch.no_grad():
    for inputs, targets in dataloader:
        outputs = model(inputs)
```

### 3.模型保存与加载

```python
# 推荐：只保存 state_dict
torch.save(model.state_dict(), 'model.pth')
model.load_state_dict(torch.load('model.pth', map_location='cpu'))

# 保存检查点（含 optimizer 等）
torch.save({
    'epoch': epoch,
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'loss': loss,
}, 'checkpoint.pth')
```

- 多GPU保存前 `model.module.state_dict()`（`DataParallel`）

### 4.自定义 Dataset

```python
pythonclass MyDataset(Dataset):
    def __init__(self, ...): ...
    def __len__(self): return len(...)
    def __getitem__(self, idx): return sample, label
```

- DataLoader 参数：`batch_size`, `shuffle`, `num_workers`, `pin_memory`, `drop_last`
- 不能接受稀疏矩阵，一般需要toArray进行

## 四、综合案例

### 4.1 金融短语情感分析

金融短语库（情感分析）https://www.modelscope.cn/datasets/modelgod2025/financial_phrasebank_50agree

![1779155598600](D:\class\2603\随堂笔记\第八周\AI大模型开发之38PyTorch全连接神经网络.assets\1779155598600.png)

> 情感分析的结果：1.积极 2.中性 3.消极

代码示例：

```python
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from torch import device
from torch.utils.data import Dataset, DataLoader

# 1.数据到设备
print("---数据加载和处理---")
# 加载数据
data=pd.read_json("datas/financial_phrasebank_50agree.jsonl",lines=True)
X=data["sentence"].astype(str).tolist()
y=data["label"].tolist()
# 划分数据集
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=42)
# 机器学习（深度学习）不懂字符串，只认数字 需要坐文本处理
# 词频 统计单词出现的次数
cv=CountVectorizer(max_features=5000,ngram_range=(1,2))
X_train=cv.fit_transform(X_train).toarray()
X_test=cv.transform(X_test).toarray()

# Pytoch库要求 数据必须 数据集
class FinData(Dataset):
    def __init__(self,data,label):
        self.data=torch.tensor(data,dtype=torch.float)
        self.label=torch.tensor(label,dtype=torch.long)
    def __len__(self):
        return len(self.data)
    def __getitem__(self,idx):
        return self.data[idx],self.label[idx]
# 把数据 转换为数据集
fd_train=FinData(X_train,y_train)
fd_test=FinData(X_test,y_test)

# 数据加载
loader_train=DataLoader(fd_train,batch_size=128,shuffle=True)
loader_test=DataLoader(fd_test,batch_size=128,shuffle=False)

print("----2.模型----")
class FinModelClass(nn.Module):
    def __init__(self,input_size,hidden_size,output_size):
        super(FinModelClass,self).__init__()
        # 输入层 隐藏层 输出层
        self.fc1=nn.Linear(input_size,hidden_size)
        # 设置激活函数
        self.relu=nn.ReLU()
        self.fc2=nn.Linear(hidden_size,output_size)
    def forward(self,x):
        res = self.relu(self.fc1(x))
        res = self.fc2(res)
        return res

model=FinModelClass(5000,128,3)
print("模型：",model)

# 训练
print("-----开始训练-----")
model.train()
# 损失函数
criterion = nn.CrossEntropyLoss()
# 优化器
optimizer=torch.optim.Adam(model.parameters(),lr=0.001)
# 训练多次
for i in range(20):
    total_loss=0
    # 数据分批次
    for data,label in loader_train:
        # 前向传播
        op=model(data)
        # 计算损失
        loss=criterion(op,label)
        total_loss+=loss.item()
        # 梯度清0
        optimizer.zero_grad()
        # 反向传播
        loss.backward()
        # 更新
        optimizer.step()
    # 本次训练结束
    print(f"训练次数：{i+1}/20")
    print(f"{i+1}次，损失：{total_loss}")
print("-----训练结束----")
# 评测
print("----开始评测----")
model.eval()
with torch.no_grad(): # 不计算梯度
    # 预测结果
    y_pred=[]
    # 目标结果
    y_test=[]
    for data,label in loader_test:
        # 前向传播 获取预测结果
        op=model(data)
        # 获取概率最大的
        _,pred=torch.max(op,1)
        # 预测结果添加到数组中
        y_pred.extend(pred.tolist())
        y_test.extend(label.numpy().tolist())
    # 所有测试数据的预测结果获取
    # 准确率
    acc=accuracy_score(y_test,y_pred)*100
    print(f"ACC准确率：{acc:0.2f}%",)
print("---结束评测---")
# 持久化
torch.save(model.state_dict(),"model.pth")

```

![1779163455494](D:\class\2603\随堂笔记\第八周\AI大模型开发之38PyTorch全连接神经网络.assets\1779163455494.png)

![1779163437440](D:\class\2603\随堂笔记\第八周\AI大模型开发之38PyTorch全连接神经网络.assets\1779163437440.png)

如果要读取持久化的

> 数据处理

```python
# 加载本地模型
model2=torch.load("model.pth")
with torch.no_grad():
    y_pred=[]
    y_test=[]
    for data,label in loader_test:
        op=model2(data)
        _,pred=torch.max(op,1)
        y_pred.extend(pred.tolist())
        y_test.extend(label.numpy().tolist())

    print("预测：")
    print(y_pred[0:5])
    print("目标：")
    print(y_test[0:5])
```

### 4.2 MNIST 数据集

MNIST 数据集（一堆 28x28 的手写数字图片）

MNIST手写数字数据集来源于是美国国家标准与技术研究所，是著名的公开数据集之一，通常这个数据集都会被作为深度学习的入门案例。数据集中的数字图片是由250个不同职业的人纯手写绘制，数据集获取的网址为：<http://yann.lecun.com/exdb/mnist/>。

具体来看，MNIST手写数字数据集包含有60000张图片作为训练集数据，10000张图片作为测试集数据，且每一个训练元素都是28*28像素的手写数字图片，每一张图片代表的是从0到9中的每个数字。该数据集样例如下图所示：

![img](https://ima-notebook-prod.image.myqcloud.com/2/anhNBeYBeHxGbqq98fofxe/file_manager/019e3de478b777909b123b7a2ebb0400.webp?q-sign-algorithm=sha1&q-ak=REDACTED&q-sign-time=REDACTED&q-key-time=REDACTED&q-header-list=&q-url-param-list=&q-signature=REDACTED)

如果我们把每一张图片中的像素转换为向量，则得到长度为28*28=784的向量。因此我们可以把MNIST数据训练集看作是一个[60000,784]的张量，第一个维度表示图片的索引，第二个维度表示每张图片中的像素点。而图片里的每个像素点的值介于0-1之间。

![img](https://ima-notebook-prod.image.myqcloud.com/2/anhNBeYBeHxGbqq98fofxe/file_manager/019e3de4d06671d2a5ddfe81e2009308.webp?q-sign-algorithm=sha1&q-ak=REDACTED&q-sign-time=REDACTED&q-key-time=REDACTED&q-header-list=&q-url-param-list=&q-signature=REDACTED)

此外，MNIST数据集的类标是介于0-9的数字，共10个类别。通常我们要用独热编码（One_Hot Encoding）的形式表示这些类标。所谓的独热编码，直观的讲就是用N个维度来对N个类别进行编码，并且对于每个类别，只有一个维度有效，记作数字1 ；其它维度均记作数字0。例如类标1表示为：([0,1,0,0,0,0,0,0,0,0])；同理标签2表示为：([0,0,1,0,0,0,0,0,0,0])。最后我们通过softmax函数输出的是每张图片属于10个类别的概率。

```python
# 1. 导入必要的库
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# ==========================================
# 2. 数据准备 (对应清单：Dataset & DataLoader)
# ==========================================
# transforms.Compose: 将多个变换组合在一起
transform = transforms.Compose([
    transforms.ToTensor(), # 将 PIL Image 或 numpy.ndarray 转换为 Tensor，并自动缩放到 [0, 1]
    transforms.Normalize((0.1307,), (0.3081,)) # 标准化：减去均值，除以标准差。这是 MNIST 的标准参数
])

# 下载并加载数据集
train_data = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_data = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

# DataLoader: 批量化、打乱、并行加载数据
# batch_size=64: 每次喂给模型 64 张图
# shuffle=True: 每个 epoch 打乱数据顺序，防止模型记忆顺序 (对应清单：DataLoader 参数)
train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
test_loader = DataLoader(test_data, batch_size=1000, shuffle=False)

# ==========================================
# 3. 定义模型 (对应清单：nn.Module 设计哲学)
# ==========================================
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__() # 必须调用父类初始化
        # 定义网络层
        self.flatten = nn.Flatten() # 展平层：将 [1, 28, 28] 变成 [1, 784]
        self.fc1 = nn.Linear(28 * 28, 128) # 全连接层：输入特征数 784，输出 128
        self.relu = nn.ReLU() # 激活函数：引入非线性
        self.dropout = nn.Dropout(0.2) # Dropout：训练时随机丢弃 20% 神经元，防止过拟合
        self.fc2 = nn.Linear(128, 10) # 输出层：10 个数字类别 (0-9)

    def forward(self, x):
        # 定义数据流向
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.dropout(x) 
        x = self.fc2(x)
        return x

# 设备配置 (对应清单：device='cpu' / 'cuda:0')
# 如果有 GPU 就用 GPU，没有就用 CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = SimpleNet().to(device) # 将模型搬到指定设备 (GPU/CPU)

# ==========================================
# 4. 定义损失和优化器 (对应清单：损失函数 & 优化器)
# ==========================================
# CrossEntropyLoss: 集成了 Softmax 和 Negative Log Likelihood Loss，用于多分类
criterion = nn.CrossEntropyLoss() 
# Adam: 自适应学习率优化器，通常比 SGD 收敛快
optimizer = optim.Adam(model.parameters(), lr=0.001)

# ==========================================
# 5. 训练循环 (对应清单：标准四步法)
# ==========================================
model.train() # 设定为训练模式：Dropout 生效，BatchNorm 更新参数
for epoch in range(3): 
    for batch_idx, (data, target) in enumerate(train_loader):
        # 步骤 1：数据搬运 (对应清单：数据到设备)
        # .to(device) 将数据移动到 GPU 显存或 CPU 内存
        data, target = data.to(device), target.to(device)
        
        # 步骤 2：前向传播 (对应清单：前向传播)
        output = model(data) # 调用 model(data) 实际上调用了 forward()
        loss = criterion(output, target) # 计算损失
        
        # 步骤 3：反向传播 (对应清单：反向传播)
        optimizer.zero_grad() # 清空上一轮的梯度，防止梯度累加
        loss.backward()      # 自动计算所有 requires_grad=True 的参数的梯度
        
        # 步骤 4：参数更新 (对应清单：参数更新)
        optimizer.step()     
        
        if batch_idx % 100 == 0:
            print(f'Epoch {epoch+1} | Batch {batch_idx} | Loss: {loss.item():.4f}')

# ==========================================
# 6. 模型保存 (对应清单：保存 state_dict)
# ==========================================
# 推荐只保存权重字典，不保存整个模型结构，这样更灵活
torch.save(model.state_dict(), 'mnist_model.pth')
print("模型已保存！")

# ==========================================
# 7. 测试/推理 (对应清单：model.eval() & no_grad)
# ==========================================
model.eval() # 设定为评估模式：Dropout 关闭，BatchNorm 使用移动平均值
test_loss = 0
correct = 0
# with torch.no_grad(): 上下文管理器，在该区域内不计算梯度，节省显存和算力
with torch.no_grad():
    for data, target in test_loader:
        data, target = data.to(device), target.to(device)
        output = model(data)
        test_loss += criterion(output, target).item()
        # pred = output.argmax(dim=1): 在维度1（类别维度）上取概率最大的索引作为预测结果
        pred = output.argmax(dim=1, keepdim=True) 
        correct += pred.eq(target.view_as(pred)).sum().item()

print(f'\nTest set: Accuracy: {correct}/{len(test_loader.dataset)} ({100. * correct / len(test_loader.dataset):.0f}%)\n')
```

![1779163306960](D:\class\2603\随堂笔记\第八周\AI大模型开发之38PyTorch全连接神经网络.assets\1779163306960.png)

![1779163396473](D:\class\2603\随堂笔记\第八周\AI大模型开发之38PyTorch全连接神经网络.assets\1779163396473.png)

## 五 原理必懂

### 5.1 动态图 vs 静态图

- 动态图：每步构建计算图，灵活，可调试；静态图：先定义再运行，优化好但调试难。
- PyTorch 动态图通过 `grad_fn` 连接反向传播。

### 5.2 链式法则 & 反向传播

- 反向传播从 `loss` 开始，沿着 `grad_fn` 链应用链式法则，计算每个叶子张量的梯度。
- `backward(retain_graph=True)` 可保留图用于多次反向。

### 5.3 梯度累积

```python
# 模拟更大 batch
for i, (inputs, targets) in enumerate(loader):
    loss = loss / accumulation_steps
    loss.backward()
    if (i+1) % accumulation_steps == 0:
        optimizer.step()
        optimizer.zero_grad()
```

### 5.4 混合精度训练（AMP）

```python
from torch.cuda.amp import autocast, GradScaler
scaler = GradScaler()
with autocast():
    outputs = model(inputs)
    loss = criterion(outputs, targets)
scaler.scale(loss).backward()
scaler.step(optimizer)
scaler.update()
```

### 5.5 梯度消失/爆炸

- 监控梯度范数：`torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm)`
- 使用合适的初始化（Xavier, Kaiming）、激活函数（ReLU 族）、BatchNorm。

### 5.6 过拟合与正则化

- Dropout（训练时随机丢弃，评估时缩放）、权重衰减（weight_decay）、早停、数据增强。

## 六、调试必知

### 1.常见问题及排查

| **问题**     | **可能原因**                                       | **解决思路**                                               |
| ------------ | -------------------------------------------------- | ---------------------------------------------------------- |
| 验证集表现差 | 过拟合、数据泄露、分布偏移                         | 增加正则化、检查数据划分、交叉验证                         |
| NaN 损失     | 输入含 NaN/log(0)/梯度爆炸/学习率过大              | 检查数据、减小 lr、加 eps、梯度裁剪、检查 loss 函数        |
| GPU 内存不足 | batch 太大、模型太大、未释放中间结果               | 减小 batch、梯度累积、AMP、梯度检查点、模型并行            |
| 训练不收敛   | lr 不当、梯度消失/爆炸、数据未标准化               | 使用 lr 查找器、检查梯度、标准化数据、合适的初始化         |
| 数据加载慢   | num_workers 太少、transform 复杂、CPU-GPU 频繁传输 | 增加 num_workers、pin_memory、简化 transform、使用内存映射 |

### 2.核心调试技巧

- 梯度检查：`torch.autograd.gradcheck` 验证自定义梯度。
- 数值梯度验证：对比 `autograd` 与有限差分。
- 使用 `torchviz` 可视化计算图。

## 七、高频追问

- **为什么 PyTorch 在学术界流行？** → 动态图、Pythonic、易调试、生态丰富。
- **detach() 和 with torch.no_grad() 区别？** → `detach()` 创建新张量（共享数据，不连图），`no_grad()` 上下文内所有操作不建图。
- **DataParallel 与 DistributedDataParallel 区别？** → DP 单进程多线程，DDP 多进程更高效，推荐 DDP。
- **如何设计一个可复现的实验？** → 固定随机种子（torch.manual_seed + numpy + python random），`torch.use_deterministic_algorithms(True)`，确定 GPU 的 cudnn 确定性。
- **解释 checkpoint 保存什么？** → `model.state_dict()` + `optimizer.state_dict()` + epoch + loss + 配置；用于断点续训或最佳模型选择。
- **什么是 gradient checkpointing？** → 用显存换时间：前向时丢弃中间激活，反向时重新计算。通过 `torch.utils.checkpoint` 实现。
- **广播机制的规则？** → 从尾部维度对齐，要么相等，要么其中一个为 1，然后扩展。

## 八、综合练习题

### 8.1 编程题一：手动实现线性回归

背景：

要求不依赖 nn.Linear等高阶 API，仅使用 torch.tensor手动实现一个简单的线性回归模型 y=wx+b，并利用 PyTorch 的自动微分机制完成一次参数更新。

题目要求：

定义样本数据：x = [1.0, 2.0, 3.0]，y = [2.0, 4.0, 6.0]（模拟 y=2x的关系）。

初始化参数 w和 b为 1.0，并设置 requires_grad=True。

定义前向计算（直接使用乘法和加法）。

定义损失函数（均方误差 MSE）。

执行反向传播，并打印出 w和 b的梯度。

手动使用梯度下降法更新 w和 b（学习率设为 0.01），并打印更新后的参数值。

考察点：

张量的创建与属性 (requires_grad)

计算图的构建 (y_pred = w*x + b)

反向传播 (loss.backward())

梯度获取 (.grad) 与参数更新

> 参考代码实现：
>
> ```python
> import torch
> 
> # 1. 准备数据
> x = torch.tensor([1.0, 2.0, 3.0])
> y = torch.tensor([2.0, 4.0, 6.0])
> 
> # 2. 初始化参数
> w = torch.tensor(1.0, requires_grad=True)
> b = torch.tensor(1.0, requires_grad=True)
> lr = 0.01
> 
> # 3. 前向传播
> y_pred = w * x + b
> print(f"更新前预测值: {y_pred.data}")
> 
> # 4. 计算损失 (MSE: 1/n * sum((y-y_pred)^2))
> loss = torch.mean((y_pred - y) ** 2)
> print(f"初始损失: {loss.item()}")
> 
> # 5. 反向传播
> loss.backward()
> 
> # 6. 查看梯度
> print(f"w 的梯度: {w.grad.item()}")
> print(f"b 的梯度: {b.grad.item()}")
> 
> # 7. 手动更新参数 (对应笔记中的 optimizer.step()，这里演示原理)
> # 注意：更新参数时不要参与计算图，所以要使用 data 或直接操作
> with torch.no_grad():
>     w.data -= lr * w.grad
>     b.data -= lr * b.grad
>     
>     # 梯度清零 (对应 optimizer.zero_grad())
>     w.grad.zero_()
>     b.grad.zero_()
> 
> print(f"更新后 w: {w.data}, b: {b.data}")
> ```

### 8.2 编程题二：泰坦尼克号生存预测

目标：根据乘客的信息（如舱位等级、性别、年龄、票价等），预测该乘客是否在泰坦尼克号沉没事故中幸存（0=遇难，1=幸存）。

数据下载：可以从 Kaggle 官网下载 train.csv和 test.csv

关键特征：

Pclass: 舱位等级 (1, 2, 3)

Sex: 性别 (male, female)

Age: 年龄 (含缺失值)

SibSp: 船上兄弟姐妹/配偶数

Parch: 船上父母/子女数

Fare: 票价

Embarked: 登船港口 (C, Q, S, 含少量缺失值)

题目要求：

数据预处理 (Python + Pandas)：

加载数据。

特征工程：选取 Pclass, Sex, Age, SibSp, Parch, Fare, Embarked作为特征。

处理缺失值：Age用中位数填充，Embarked用众数填充。

编码：将 Sex映射为 0/1；将 Embarked进行 One-Hot 编码（或 Label Encoding）。

标准化：对 Age和 Fare进行标准化（减去均值，除以标准差），因为神经网络对尺度敏感。

切分：将数据切分为训练集和验证集（如 8:2）。

构建 PyTorch 模型 (nn.Module)：

继承 nn.Module。

定义一个包含 2个隐藏层 的全连接网络。

输入层维度取决于你的特征数（例如：Pclass(1) + Sex(1) + Age(1) + SibSp(1) + Parch(1) + Fare(1) + Embarked(3个one-hot) = 9维）。

隐藏层1：128个神经元，接 ReLU 激活。

隐藏层2：64个神经元，接 ReLU 激活。

输出层：1个神经元（因为是二分类），接 Sigmoid 激活（或者直接用 BCEWithLogitsLoss，输出层不加激活）。

训练与评估 (标准四步法)：

损失函数。

使用 Adam优化器。

编写训练循环（至少 20 个 Epoch）。

在验证集上计算 Accuracy。

> 参考实现：
>
> ```python
> import torch
> import torch.nn as nn
> import torch.optim as optim
> from torch.utils.data import Dataset, DataLoader
> import pandas as pd
> import numpy as np
> from sklearn.model_selection import train_test_split
> from sklearn.preprocessing import StandardScaler
> from sklearn.metrics import accuracy_score
> 
> # ==========================================
> # 1. 数据处理 (Pandas & Sklearn)
> # ==========================================
> df = pd.read_csv('train.csv') # 请确保 train.csv 在当前目录
> 
> # 特征选择
> features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
> target = 'Survived'
> 
> # 处理缺失值
> df['Age'].fillna(df['Age'].median(), inplace=True)
> df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
> 
> # 特征工程
> df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
> # Embarked One-Hot
> embarked_dummies = pd.get_dummies(df['Embarked'], prefix='Embarked').astype(int)
> df = pd.concat([df, embarked_dummies], axis=1)
> features.extend(['Embarked_C', 'Embarked_Q', 'Embarked_S'])
> 
> # 提取 X 和 y
> X = df[features].values.astype(np.float32)
> y = df[target].values.astype(np.float32)
> 
> # 数据标准化 (非常重要！)
> scaler = StandardScaler()
> X = scaler.fit_transform(X)
> 
> # 划分数据集
> X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
> 
> # ==========================================
> # 2. 自定义 Dataset
> # ==========================================
> class TitanicDataset(Dataset):
>     def __init__(self, data, labels):
>         self.X = torch.tensor(data, dtype=torch.float32)
>         self.y = torch.tensor(labels, dtype=torch.float32).view(-1, 1)
>         
>     def __len__(self):
>         return len(self.X)
>     
>     def __getitem__(self, idx):
>         return self.X[idx], self.y[idx]
> 
> train_ds = TitanicDataset(X_train, y_train)
> val_ds = TitanicDataset(X_val, y_val)
> 
> train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
> val_loader = DataLoader(val_ds, batch_size=32, shuffle=False)
> 
> # ==========================================
> # 3. 定义模型
> # ==========================================
> class TitanicNet(nn.Module):
>     def __init__(self, input_size):
>         super(TitanicNet, self).__init__()
>         self.net = nn.Sequential(
>             nn.Linear(input_size, 128),
>             nn.ReLU(),
>             nn.Dropout(0.2), # 加入 Dropout 防止过拟合
>             nn.Linear(128, 64),
>             nn.ReLU(),
>             nn.Linear(64, 1) # BCEWithLogitsLoss 包含 Sigmoid，这里不用加
>         )
>     
>     def forward(self, x):
>         return self.net(x)
> 
> input_dim = X_train.shape[1] # 应该是 10 (原7个 + 3个one-hot)
> model = TitanicNet(input_dim)
> 
> # ==========================================
> # 4. 训练配置
> # ==========================================
> device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
> model.to(device)
> criterion = nn.BCEWithLogitsLoss() # 自带 Sigmoid，更稳定
> optimizer = optim.Adam(model.parameters(), lr=0.001)
> 
> # ==========================================
> # 5. 训练循环
> # ==========================================
> model.train()
> epochs = 50
> for epoch in range(epochs):
>     total_loss = 0
>     for data, labels in train_loader:
>         data, labels = data.to(device), labels.to(device)
>         
>         # 标准四步法
>         outputs = model(data)
>         loss = criterion(outputs, labels)
>         
>         optimizer.zero_grad()
>         loss.backward()
>         optimizer.step()
>         
>         total_loss += loss.item()
>     
>     # 简单验证
>     model.eval()
>     correct = 0
>     total = 0
>     with torch.no_grad():
>         for data, labels in val_loader:
>             data, labels = data.to(device), labels.to(device)
>             outputs = model(data)
>             predicted = (torch.sigmoid(outputs) > 0.5).float() # 阈值 0.5
>             total += labels.size(0)
>             correct += (predicted == labels).sum().item()
>     
>     acc = correct / total * 100
>     print(f'Epoch [{epoch+1}/{epochs}], Loss: {total_loss/len(train_loader):.4f}, Val Acc: {acc:.2f}%')
> ```



# 2.CNN

## 2.1 CNN

CNN卷积神经网络 ，处理图像相关内容

图像-机器视觉

> 把图像转换为数字

## 2.2 CNN核心

1.卷积层

2.激活函数

3.池化层

4.全连接



## 2.3 CNN实战体验

基于手写数字实现手写数字识别

```python
# 基于CNN实现手写数字的识别
import torch
import torch.nn as nn
import torchvision # 基于Pytorch实现的视觉
import torchvision.transforms as transforms
from torch import optim

# 数据 和 处理
# 将图片转换为 Tensor (张量)，并归一化到 [-1, 1] 之间
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])
# 下载训练集和测试集
train_dataset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)

train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=32, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=32, shuffle=False)

# 模型
class MNISTModel(nn.Module):
    def __init__(self):
        super(MNISTModel, self).__init__()
        # cnn 卷积层 池化层
        self.cn1=nn.Conv2d(1,16,kernel_size=3,padding=1)
        # 激活函数
        self.relu = nn.ReLU()
        # 池化
        self.pool=nn.MaxPool2d(kernel_size=2,stride=2)
        self.cn2=nn.Conv2d(16,32,3,1,1)
        # 全连接层
        self.fc1=nn.Linear(32*7*7,128)
        self.fc2=nn.Linear(128,10)
    def forward(self,x):
        # 处理视觉 图片
        op1=self.pool(self.relu(self.cn1(x)))
        op1=self.pool(self.relu(self.cn2(op1)))
        # 展开 变为一维 内存连续
        op1=op1.view(-1,32*7*7)
        # 全连接
        op1=self.relu(self.fc1(op1))
        op1=self.fc2(op1)
        return op1
# 训练
# 创建模型
model=MNISTModel()
print("模型的结构：",model)
# 创建损失函数
criterion = nn.CrossEntropyLoss()
# 创建优化器
optimizer = optim.Adam(model.parameters(), lr=0.001)
# 标记 训练
model.train()
# 运行设备
device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
# 多次训练
for i in range(10):
    total_loss=0
    print(f"第{i+1}次训练开始")
    # 分批次学习样本
    for j,(image,label) in enumerate(train_loader):
        # 前向传播
        image=image.to(device)
        label=label.to(device)
        output=model(image)
        # 计算损失
        loss = criterion(output, label)
        # 反向传播
        loss.backward()
        total_loss+=loss.item()
        # 更新参数
        optimizer.step()
        # 清零 梯度
        optimizer.zero_grad()
    print(f"训练：{(i+1)}次/10次")
    print(f"损失值变化：{total_loss/len(test_loader):.2f}")
# 评测
model.eval()
with torch.no_grad():
    num1,num2=0,0
    for i,(image,label) in enumerate(test_loader):
        image=image.to(device)
        label=label.to(device)
        # 预测 前向传播
        output=model(image)
        p=torch.argmax(output,dim=1)
        num1+=(p==label).sum().item()
        num2+=label.size(0)
    print(f"准确率：{100*num1/num2:.2f}%")

```

![1779184847333](D:\class\2603\随堂笔记\第八周\AI大模型开发之38PyTorch全连接神经网络.assets\1779184847333.png)

# 3.综合练习

## 3.1 猫狗大战

编程实战题：Kaggle 猫狗大战 (Dogs vs. Cats)

https://www.modelscope.cn/datasets/XCsunny/cat_vs_dog_class/files

数据集简介：

任务：二分类问题。输入一张图片，判断是猫（0）还是狗（1）。


题目要求：

数据预处理 (Transforms)：

使用 transforms.Compose将图片统一缩放到 128x128（为了训练快一点，正式比赛通常用 224x224）。

将图片转换为 Tensor，并进行标准化（mean=[0.5], std=[0.5]适用于灰度图，或者 RGB 的三通道均值）。

构建 CNN 模型 (nn.Module)：

设计一个简单的 CNN，包含：

Conv Block 1: Conv2d(3, 16, kernel_size=3) -> ReLU -> MaxPool2d(2)。

Conv Block 2: Conv2d(16, 32, kernel_size=3) -> ReLU -> MaxPool2d(2)。

全连接层: 展平后接入 Linear 层，输出 2 个类别（猫或狗）。

训练与验证：

使用 CrossEntropyLoss（因为我们有 2 类，输出层不用加 Softmax）。

使用 Adam优化器。

编写一个训练循环，并在每个 Epoch 结束后在验证集上看一眼损失变化。



