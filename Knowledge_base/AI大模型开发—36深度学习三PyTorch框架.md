# AI大模型开发之36PyTorch框架

> 作者：AI芯源-邢朋辉

# 0.课程内容

## 0.1 晨考



## 0.2 课程回顾



# 1.PyTorch

## 1.1 Pytorch是什么

深度学习的框架：

1.Thenno

2.Caffe

3.TensorFlow 静态图

4.PyTorch 动态图

目前主流是PyTorch框架作为深度学习的主流框架

Pytorch基于动态计算图，定义即执行的开源库

支持CPU和GPU

> 大量运算推荐使用GPU

## 1.2 安装Pytorch

Windows为例：采用conda

创建虚拟环境

conda create -n deepl

激活环境

conda activate deepl

下载所需环境

```bash
pip install torch torchvision torchaudio
```

创建Python项目，导入使用

```python
# torch 深度学习库
import torch
print("版本号：",torch.__version__)
print("CUDA：",torch.cuda.is_available())
```

查看效果

![1778898008080](D:\class\2603\随堂笔记\第七周\AI大模型开发-36深度学习三PyTorch框架.assets\1778898008080.png)

# 2.Pytorch基础

## 2.1 Numpy

Pytorch的基础类型单元为张量，那么张量就是多维数组，可以基于Numpy进行创建使用，也可以直接创建使用

Numpy的基础用法需要掌握：

```Python
#
import torch
import numpy as np

# 可以通过Numpy的数组 创建张量
# 3*3 矩阵
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("原来：")
print(arr1)
# 转换为张量 tensor
arr2=torch.from_numpy(arr1)
print("现在：")
print(arr2)
# 共享内存
arr1[0,2]=300
arr2[1,2]=666
print("numpy数组：\n",arr1)
print("tensor：\n",arr2)
# 创建张量
data2=torch.randint(1,100,(3,4))
print(data2)
# 把张量转换为 数组
data1=data2.numpy()
print(data1)
```

## 2.2 面向对象

Pytorch内部实现常用深度学习相关的封装，采用面向对象实现的

需要掌握Python语言中面向对象

```python
import numpy as np
import torch.nn as nn

# 定义类
class NeuralNetwork:
    # 构造函数
    def __init__(self, input_size, hidden_size):
        """构造函数，初始化网络参数"""
        self.weights1 = np.random.randn(input_size, hidden_size)
        self.bias1 = np.zeros(hidden_size)
        self.weights2 = np.random.randn(hidden_size, 1)
        self.bias2 = np.zeros(1)
    # 函数
    def forward(self, x):
        """前向传播方法"""
        h = np.dot(x, self.weights1) + self.bias1
        h = np.maximum(0, h)  # ReLU激活
        output = np.dot(h, self.weights2) + self.bias2
        return output
    # 重写函数
    def __str__(self):
        """字符串表示，便于调试"""
        return f"NeuralNetwork(input->{self.weights1.shape[0]}, hidden->{self.weights1.shape[1]})"


# 创建网络实例
model = NeuralNetwork(input_size=784, hidden_size=128)
print(model)  # 调用__str__方法
output = model.forward(np.random.randn(10, 784))
print(output)

# 继承 有父类 父类中属性和函数（非私有）都可以被子类继承
class CustomLayer(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()  # 必须调用父类初始化
        self.linear = nn.Linear(in_features, out_features)
        self.activation = nn.ReLU()

    def forward(self, x):
        return self.activation(self.linear(x))
```

## 2.3.张量

张量（Tensor）：多维数组（0-n），是深度学习的数据存储的结构

0维张量  标量

1维张量  一维数组/向量

2维张量 二维数组/矩阵

3维张量 三维数组

4维张量 四维数组

关键属性：

1.设备：cpu环境还是gpu环境

2.数据类型：dtype 精度和占用内存

基于PyTorch创建和使用张量

创建：

```python
# 张量的创建和使用
import numpy as np
import torch

# 创建
arr1=torch.tensor([[1, 2, 3], [4, 5, 6]])
print(arr1)
arr2=torch.tensor(np.array([[1, 2, 3], [4, 5, 6]]))
print(arr2)
# 随机
arr3=torch.randn(2,3)
print(arr3)
# randint 参数说明：1.起始值 2.结束值 3.形状
arr4=torch.randint(1,100,(3,4,3,4))
print(arr4)
# 指定好的创建 0 1 单位 等差 等间距
print("单位：",torch.eye(4))
print("值为1：",torch.ones((2,3)))
print("值为0：",torch.zeros((2,3)))
print("等差：",torch.arange(1,100,3))
print("等间距-均分：",torch.linspace(1,20,5))
```

张量相关运算

```python
# 张量运算
import numpy as np
import torch

# 数据
arr1=torch.tensor([[1.,2.,3.],[4.,5.,6.]],dtype=torch.int32)
print(arr1)
print(arr1+10)
print(arr1+torch.tensor([2,2,2]))
# matmul 矩阵乘积 对应元素相乘 求和
print(arr1.matmul(torch.tensor([2,2,2],dtype=torch.int32)))
arr3=torch.tensor([1,2,3],dtype=torch.int32)
arr4=torch.tensor([2,3,4],dtype=torch.int32)
# dot 点积  对应元素相乘 求和
print(torch.dot(arr3,arr4))
# 规约  统计
print(arr3.sum(dtype=torch.int32))
print(arr1.sum(dim=1,keepdim=True))
```

梯度下降：

```python
import torch
import numpy as np
#创建
# requires_grad 可以看导数 标记叶子节点 开启梯度变化
x=torch.tensor(2.0,requires_grad=True)
y=torch.tensor(5.0,requires_grad=True)
# z=x^2+3y
z=x**2+3*y
print(z)
# 前向传播
z.backward()
# 查看偏导数的值
print(x.grad)
print(y.grad)
x.grad.zero_()
# 累加 .grad
print("循环前：")
for i in range (1,4):
    #x^2=2x
    a=x**2
    a.backward()
    print(x.grad)
    x.grad.zero_()
print("结束：")
print(x.grad)
print("x叶子结点：",x.is_leaf)
print("y叶子结点：",y.is_leaf)
print("z叶子结点：",z.is_leaf)
```

# 3.自动微分

梯度是深度学习的引擎。

在神经网络中，梯度表示损失函数相对于参数的变化率，指导参数更新方向。手动计算梯度对于复杂网络几乎不可能，这就是自动微分（Autograd）的价值所在。

```python
import torch
import numpy as np
#创建
# requires_grad 可以看导数 标记叶子节点 开启梯度变化
x=torch.tensor(2.0,requires_grad=True)
y=torch.tensor(5.0,requires_grad=True)
# z=x^2+3y
z=x**2+3*y
print(z)
# 前向传播
z.backward()
# 查看偏导数的值
print(x.grad)
print(y.grad)
# 清零梯度
x.grad.zero_()
# 累加 .grad
print("循环前：")
for i in range (1,4):
    #x^2=2x
    a=x**2
    a.backward()
    print(x.grad)
    x.grad.zero_()
print("结束：")
print(x.grad)
print("x叶子结点：",x.is_leaf)
print("y叶子结点：",y.is_leaf)
print("z叶子结点：",z.is_leaf)
```

# 4.综合练习

## 第 1 题：张量创建 + 设备与数据类型

请完成以下任务：
创建一个 3 维张量，形状为 (2, 3, 4)
数据类型为 float16
打印：
张量的形状
所在设备
数据类型
将数据类型改为 float32

## 第 2 题：4 维张量 + 批量数据模拟

题目背景
在深度学习中，4 维张量是最常见的输入格式：
[batch_size, channels, height, width]
题目要求
创建一个 4 维张量，表示：
batch_size = 4
channels = 3（RGB）
height = 32
width = 32
使用 随机数初始化
数据类型为 float32
打印张量形状
取出：
第 1 个样本的 第 2 个通道
形状应为 [32, 32]
将该通道所有值乘以 2

# 5.作业

1.绘制本周思维导图