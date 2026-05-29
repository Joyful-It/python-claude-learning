# AI大模型开发40RNN

> 作者：Ai芯源邢朋辉

# 0.课程内容

## 0.1 晨考



## 0.2 课程回顾

1.CNN

卷积神经网络，视觉处理，图片

卷积层：把图像对应的数组内容进行转换（特征提取）

​	输入特征+卷积核+填充+步长=新特征

激活函数：非线性 ReLU 

池化层：压缩 窗口大小+步长 常用：Max Pool、Avg Pool

全连接：Linear

> 经典实例：
>
> 1.手写数字
>
> 2.猫狗分类

2.OpenCV

开源，处理图片

加载图片转换为数组（彩图和灰图）、裁剪、缩放、存储、绘制……

3.YOLO

基于CNN训练好的模型-YOLO

识别图像、分析视频、外接摄像头

内置80类的分类，还可以自定义训练

机器视觉--通过摄像头获取感知

4.迁移学习

基于现成的模型进行二次训练进行扩展

1.冻结参数

2.修改模型（连接层、卷积层……）

避免从头训练一个新模型



# 1.RNN

## 1.1 RNN

RNN循环神经网络，是一种序列建模的算法思维

有序列：时间+内容，当前内容会受到之前内容的影响

序列数据：从自然语言处理的角度看，每个句子都是一个字符或单词的序列。"我爱北京天安门"这句话之所以有意义，不仅因为每个字本身，更因为它们在特定顺序下的组合。

之前的前馈网络（CNN）无法处理序列数据

核心实现是通过隐藏状态，记录时间步的以往信息



## 1.2 RNN初体验

下载依赖torch

导入使用

```python
# RNN 循环神经网络 处理序列数据 序列建模
import torch
from torch import nn

# 模型
class RNNNetModel(nn.Module):
    def __init__(self):
        super(RNNNetModel, self).__init__()
        # RNN
        # 参数：input_size 输入
        self.rnn = nn.RNN(input_size=3, hidden_size=5, num_layers=2,batch_first=True)
        # 全连接
        self.fc = nn.Linear(5, 2)
        # 激活函数
        self.softmax = nn.LogSoftmax(dim=1)
    def forward(self, x):
        # RNN
        out, _ = self.rnn(x)
        # 全连接
        out = self.fc(out)
        # 结果多分类
        out = self.softmax(out)
        return out
# 创建模型对象
model=RNNNetModel()
print(model)
# 使用RNN模型
data=torch.randn(3, 2, 3)
print("输入：",data)
with torch.no_grad(): # 不计算梯度
    op=model(data) # 使用 前向传播 获取预测结果
    print(op)
```

## 1.3 核心



长时短期记忆的问题，缓解梯度消失，提高长时记忆

LSTM：通过门控器实现：记忆和短时输出的分离

​	有3个门：

​	1.遗忘门：根据数学计算选择性丢弃

​	2.输入门：控制一定比例的输入-新增

​	3.输出门：控制-一定比例的输出

GRU：LSTM改进版

​	提出了，用2个门

​	1.更新门

​	2.重置门

RNN这类的隐藏状态计算



## 1.4 基于LSTM实现情感分析

1.数据和处理

句子 需要 分词

> 金融短语数据情感分析
>
> IMDb电影评论

2.定义模型

​	RNN

​	LSTM

​	GRU

3.模型训练

4.模型评测

> 再换成RNN、GRU分别进行测试
>
> 获取心得体会

第一次示例代码：

```python
# 基于LSTM 实现金融短语的情感分析
from collections import Counter
import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from torch import nn, optim
from torchtext.data.utils import get_tokenizer
from torch.utils.data import Dataset, DataLoader
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#1.数据加载和处理的函数
# 分词
def load_data():
    # 加载数据
    df = pd.read_json("data/financial_phrasebank_50agree.jsonl",lines=True)
    X=df["sentence"]
    y=df["label"]
    # 划分数据集
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
    # X处理 分词相关
    tokenizer=get_tokenizer("basic_english")
    vocab_train=build_vocab(X_train,tokenizer)
    vocab_test=build_vocab(X_test,tokenizer)
    train_ds=FinDataSet(X_train,y_train,vocab_train,tokenizer)
    test_ds=FinDataSet(X_test,y_test,vocab_test,tokenizer)
    train_loader=DataLoader(train_ds,batch_size=32,shuffle=True,collate_fn=collate_fn)
    test_loader=DataLoader(test_ds,batch_size=32,shuffle=False,collate_fn=collate_fn)
    return train_loader,test_loader,vocab_train

# 词向量转换 数字数组
def build_vocab(data_iter, tokenizer, max_size=10000):
    counter = Counter()
    for data in data_iter:
        counter.update(tokenizer(data))
    # 保留最常见词汇
    vocab = {word: idx+2 for idx, (word, _) in enumerate(counter.most_common(max_size))}
    vocab['<pad>'] = 0  # 填充标记
    vocab['<unk>'] = 1  # 未知词标记
    return vocab
def collate_fn(batch):
    texts, labels = zip(*batch)
    # 找到这个 batch 最长的句子
    max_len = max([len(t) for t in texts])
    # 填充
    padded_texts = torch.zeros(len(texts), max_len, dtype=torch.long)
    for i, text in enumerate(texts):
        length = len(text)
        padded_texts[i, :length] = text
    labels = torch.stack(labels)
    return padded_texts.to(DEVICE), labels.to(DEVICE)
# 数据集类
class FinDataSet(Dataset):
    def __init__(self,X,y,vocab,tokenizer):
        self.X=X
        self.y=y
        self.vocab = vocab
        self.tokenizer = tokenizer
    def __len__(self):
        return len(self.X)
    # def __getitem__(self, idx):
    #     return self.X[idx],self.y[idx]
    def __getitem__(self, idx):
        text = str(self.X.iloc[idx])  # 确保是字符串
        label = int(self.y.iloc[idx])  # 确保是 int
        # 1. 分词
        tokens = self.tokenizer(text)
        # 3. 转数字 (OOV用<unk>)
        token_ids = [self.vocab.get(token, self.vocab['<unk>']) for token in tokens]

        return torch.tensor(token_ids, dtype=torch.long), torch.tensor(label, dtype=torch.long)
# 2.模型
class LSTMModel(nn.Module):
    def __init__(self,vocab_size, embedding_dim,hidden_dim,output_dim):
        super(LSTMModel,self).__init__()
        # 词
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)
        # LSTM
        self.lstm = nn.LSTM(embedding_dim,hidden_dim,batch_first=True)
        # 双向
        self.fc = nn.Linear(hidden_dim,output_dim)
    def forward(self,x):
        embedded = self.embedding(x)
        _, (hidden, cell) = self.lstm(embedded)
        hidden = hidden.squeeze(0)
        return self.fc(hidden)
# 3.训练
def model_train(model,loader):
    model.train()
    #损失
    criterion = nn.CrossEntropyLoss()
    # 优化器
    optimizer = optim.Adam(model.parameters(),lr=0.001)
    for i in range(10):
        total_loss=0
        for data,label in loader:
            # 前向传播
            y1=model(data)
            # 计算损失
            loss=criterion(y1,label)
            total_loss+=loss.item()
            # 清零梯度
            optimizer.zero_grad()
            # 反向传播
            loss.backward()
            # 优化器更新参数
            optimizer.step()
        print(f"当前：{i+1}/{20}轮，损失：{total_loss/len(loader):.2f}")

# 4.评测
def model_test(model,loader):
    # 开启评测
    model.eval()
    with torch.no_grad():
        y_yred=[]
        y_test=[]
        for data,label in loader:
            # 前向传播
            preds=model(data).squeeze(1)
            preds = torch.argmax(preds, dim=1)
            # 记录结果 三分类
            y_yred.extend(preds.numpy())
            y_test.extend(label.numpy())
            print(y_yred[0:3])
            print(y_test[0:3])
        print(f"准确率：{accuracy_score(y_test,y_yred)*100:0.2f}%")

# 统一调用
# 1.数据
load_train,load_test,vocab=load_data()
# 2.模型
model=LSTMModel(len(vocab),128,128,3)
# 3.训练
model_train(model,load_train)
# 4.评测
model_test(model,load_test)
```

![1779348929236](D:\class\2603\随堂笔记\第八周\AI大模型开发之40RNN.assets\1779348929236.png)

改进：双层+Dropout

```python
# 双层 Dropout
# 基于LSTM 实现金融短语的情感分析
from collections import Counter
import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from torch import nn, optim
from torchtext.data.utils import get_tokenizer
from torch.utils.data import Dataset, DataLoader
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#1.数据加载和处理的函数
def load_data():
    """
    加载金融短语数据，并进行分词、构建词表、封装 Dataset 和 DataLoader
    """
    # 读取 jsonl 格式的金融情感数据（每行一个 JSON）
    df = pd.read_json("data/financial_phrasebank_50agree.jsonl", lines=True)
    # X：句子文本
    X = df["sentence"]
    # y：标签（例如：0=负面，1=中性，2=正面）
    y = df["label"]
    # 划分训练集和测试集（80% 训练，20% 测试）
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    # 使用 TorchText 提供的英文基础分词器
    # basic_english：小写 + 按空格和标点分词
    tokenizer = get_tokenizer("basic_english")
    # 根据训练集构建词表（防止测试集泄露）
    vocab_train = build_vocab(X_train, tokenizer, max_size=10000)
    # 构造训练数据集
    train_ds = FinDataSet(X_train, y_train, vocab_train, tokenizer)
    # 测试集使用训练集的词表（未登录词用 <unk>）
    test_ds = FinDataSet(X_test, y_test, vocab_train, tokenizer)
    # 训练数据加载器（打乱顺序，批量加载）
    train_loader = DataLoader(
        train_ds,
        batch_size=32,
        shuffle=True, # 是否随机打乱
        collate_fn=collate_fn  # 自定义批处理函数
    )
    # 测试数据加载器（不打乱）
    test_loader = DataLoader(
        test_ds,
        batch_size=32,
        shuffle=False,
        collate_fn=collate_fn
    )
    return train_loader, test_loader, vocab_train

# 词向量转换 数字数组
def build_vocab(data_iter, tokenizer, max_size=10000):
    """
    根据训练语料构建词表
    参数：
    - data_iter: 文本数据（pandas Series）
    - tokenizer: 分词器
    - max_size: 词表最大大小（保留最常见的词）
    返回：
    - vocab: {单词: 索引}
    """
    counter = Counter()
    # 遍历每一条文本
    for data in data_iter:
        # 分词并统计词频
        counter.update(tokenizer(data))
    # 构建词表：最常见的前 max_size 个词
    vocab = {
        word: idx + 2
        for idx, (word, _) in enumerate(counter.most_common(max_size))
    }
    # 填充符：用于对齐句子长度
    vocab['<pad>'] = 0
    # 未知词：测试集中没见过的词
    vocab['<unk>'] = 1
    return vocab
# 填充对齐
def collate_fn(batch):
    """
    将一个 batch 的数据进行填充对齐
    参数：
    - batch: [(token_ids, label), ...]
    返回：
    - padded_texts: (batch_size, max_len)
    - labels: (batch_size,)
    """
    # 解包 batch
    texts, labels = zip(*batch)
    # 找到该 batch 中最长的句子长度
    max_len = max([len(t) for t in texts])
    # 初始化填充后的张量（全 0）
    padded_texts = torch.zeros(len(texts), max_len, dtype=torch.long)
    # 逐个句子填充
    for i, text in enumerate(texts):
        length = len(text)
        padded_texts[i, :length] = text
    # 标签拼接成一个张量
    labels = torch.stack(labels)
    return padded_texts.to(DEVICE), labels.to(DEVICE)
# 数据集类
class FinDataSet(Dataset):
    """
    金融短语数据集
    """
    def __init__(self, X, y, vocab, tokenizer):
        self.X = X                     # 句子
        self.y = y                     # 标签
        self.vocab = vocab             # 词表
        self.tokenizer = tokenizer     # 分词器
    def __len__(self):
        # 数据集大小
        return len(self.X)
    def __getitem__(self, idx):
        # 取出第 idx 条数据
        text = str(self.X.iloc[idx])   # 转为字符串
        label = int(self.y.iloc[idx])  # 转为整数标签
        # 分词
        tokens = self.tokenizer(text)
        # 将词转换为索引（未登录词用 <unk>）
        token_ids = [
            self.vocab.get(token, self.vocab['<unk>'])
            for token in tokens ]
        return (
            torch.tensor(token_ids, dtype=torch.long),  # 输入
            torch.tensor(label, dtype=torch.long)       # 标签
        )
# 2.模型
class LSTMModel(nn.Module):
    """
    双向 LSTM 情感分类模型
    """
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim, dropout):
        super(LSTMModel, self).__init__()
        # 1.词嵌入层 句子 分词
        # padding_idx=0：<pad> 不参与训练
        self.embedding = nn.Embedding(
            vocab_size, embedding_dim, padding_idx=0
        )
        # 2.LSTM 层
        self.lstm = nn.LSTM(
            input_size=embedding_dim,   # 输入维度
            hidden_size=hidden_dim,     # 隐藏层维度
            num_layers=2,              # 双层 LSTM
            bidirectional=True,        # 双向
            batch_first=True,           # 输入格式 (batch, seq, feature)
            dropout=dropout # 层间 Dropout
        )
        # 全连接层（双向 × hidden_dim）
        self.fc = nn.Linear(hidden_dim * 2, output_dim)
        # 双层 Dropout（嵌入后 + 隐藏层后）
        self.dropout = nn.Dropout(dropout)
    def forward(self, x):
        """
        x: (batch_size, seq_len)
        """
        # 词嵌入 + Dropout
        embedded = self.dropout(self.embedding(x))
        # embedded: (batch, seq_len, embed_dim)
        # LSTM 前向传播
        output, (hidden, cell) = self.lstm(embedded)
        # hidden: (num_layers*2, batch, hidden_dim)
        # 拼接最后一层正反向隐藏状态
        hidden = self.dropout(
            torch.cat((hidden[-2, :, :], hidden[-1, :, :]), dim=1)
        )
        # hidden: (batch, hidden_dim*2)
        # 全连接输出
        return self.fc(hidden)
# 3.训练
def model_train(model, loader):
    """
    模型训练函数
    """
    model.train()
    # 交叉熵损失（适用于多分类）
    criterion = nn.CrossEntropyLoss()
    # Adam 优化器
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    for i in range(10):  # 训练 10 个 epoch
        total_loss = 0
        for data, label in loader:
            y_pred = model(data)              # 前向
            loss = criterion(y_pred, label)    # 计算损失
            total_loss += loss.item()
            optimizer.zero_grad()  # 清零梯度
            loss.backward()        # 反向传播
            optimizer.step()       # 更新参数
        print(f"Epoch {i+1}/10, Loss: {total_loss/len(loader):.2f}")

# 4.评测
def model_test(model,loader):
    # 开启评测
    model.eval()
    with torch.no_grad():
        y_pred=[]
        y_test=[]
        for data,label in loader:
            # 前向传播
            preds=model(data)
            preds = torch.argmax(preds, dim=1)
            # 记录结果 三分类
            y_pred.extend(preds.numpy())
            y_test.extend(label.numpy())
        print(f"准确率：{accuracy_score(y_test,y_pred)*100:0.2f}%")

# 统一调用
# 1.数据
load_train,load_test,vocab=load_data()
# 2.模型
model=LSTMModel(len(vocab),256,256,3,0.2)
# 3.训练
model_train(model,load_train)
# 4.评测
model_test(model,load_test)

```

准确率：75.57%



> CNN 图像相关
>
> RNN 循环 序列
>
> GCN 图神经网络 推荐系统--你喜欢，商品-关键，朋友……
>
> > 图 数据结构，社交类
>
> GCN实现过程：1.邻接矩阵--找朋友 2.度矩阵--朋友多不多 3.归一化-公平 
>
> LightGCN



## 1.5 中文分词

- **jieba**：支持精确模式、全模式和搜索引擎模式三种分词方式，提供自定义词典、词性标注、关键词提取、词语位置定位等功能，适用于多种文本处理场景。
- **jiagu**：集成分词、词性标注、命名实体识别、情感分析、知识图谱关系抽取等功能，适合综合性NLP任务，如新词发现和文本聚类。
- **snownlp**：提供分词、情感分析、简繁转换、拼音转换、文本摘要等功能，适合简单的情感分析或文本转换需求。
- **thulac**：由清华大学开发，支持分词和词性标注，输出格式灵活，适合学术和研究用途。
- **LAC**：百度开发的词法分析工具，集成分词、词性标注、实体识别和词语重要性分析，支持自定义词典，适合需要实体识别和关键词语提取的场景。

# 2.今日总结

RNN 循环神经网络

处理序列数据-NLP(自然语言处理)

词嵌入层（处理句子）

RNN层

激活函数

全连接层

Dropout

> 一般推荐双层

nn.RNN

升级：

LSTM：

​	引入 门控机

​	输入门

​	遗忘门

​	输出门

长时记忆

nn.LSTM

Gru

​	更新门

​	重置门

nn.GRU



可以采用这3种实现对金融数据情感分析，观察效果

seq2seq 编码器2解码器

先阅读再输出

自注意力机制：

阅读的时候记一下，输出的可以查阅记录

也就是Transformer的核心，目前最为主流的生成式模型，序列建模新机制

GPT系列的大模型就是基于Transformer



NLP（自然语言处理）+Transformer