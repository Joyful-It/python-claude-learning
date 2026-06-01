# AI大模型开发之42Transformer二

> 作者：AI芯源邢朋辉

# 0.课程内容

## 0.1晨考

https://ks.wjx.com/vm/Ybka8HE.aspx# 

## 0.2 课程回顾



# 1.Colab应用

## 1.1 Colab平台概述

Google Colaboratory (Colab) = 免费 GPU 云端 Notebook

 免费 GPU (T4, 有时 A100)
 预装 PyTorch / TensorFlow / CUDA
 与 Google Drive 无缝集成
 协作共享 (类似 Google Docs)
 无需本地 GPU 硬件

 12小时超时断连（有的5小时）
 GPU 配额限制 (约12h/天)
 内存有限 (12~25GB)
 偶尔分配不到 GPU

| GPU 型号 | 显存 | 算力 | 适用场景         | Colab 可用性 |
| -------- | ---- | ---- | ---------------- | ------------ |
| **T4**   | 16GB | 中等 | 教学、小模型训练 | 免费         |
| **V100** | 16GB | 强   | 中等模型训练     | Colab Pro    |
| **A100** | 40GB | 很强 | 大模型训练       | Colab Pro+   |
| **L4**   | 24GB | 强   | 性价比训练       | Colab Pro    |

> T4 显存 16GB，足够训练 ~100M 参数的 Transformer。



## 1.2 Colab使用

https://colab.research.google.com/

1.访问并创建NoteBook

![1779673917181](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779673917181.png)

2.连接

观察是否连接成功

![1779673979985](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779673979985.png)

3.更改运行时类型

选择GPU 免费的T4 16G显存

![1779674043245](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779674043245.png)

重新连接，等待

![1779674100774](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779674100774.png)

4.编写代码查看GPU环境

```
import torch

print("版本号:",torch.__version__)
cuda_available=torch.cuda.is_available()
print("是否支持GPU:",cuda_available)

if cuda_available:
    # GPU 型号
    gpu_name = torch.cuda.get_device_name(0)
    print(f"GPU 型号: {gpu_name}")

    # CUDA 版本
    print(f"CUDA 版本: {torch.version.cuda}")
    print(f"cuDNN 版本: {torch.backends.cudnn.version()}")

    # PyTorch 版本
    print(f"PyTorch 版本: {torch.__version__}")
else:
    print("未检测到 GPU！请确认运行时类型设置为 GPU")
```

![1779674455691](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779674455691.png)

5.查看环境和依赖下载

```python
# 
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"训练设备: {device}")

import sys
import subprocess

# Python 版本
print(f"Python: {sys.version}")

# 已安装的关键包
packages = {
    "torch": torch.__version__,
    "numpy": __import__('numpy').__version__,
    "matplotlib": __import__('matplotlib').__version__,
}

for name, version in packages.items():
    print(f"  {name}: {version}")

import transformers

print("Transformers版本号",transformers.__version__)
```

![1779674808497](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779674808497.png)

6.加载数据集

```python
from datasets import load_dataset

# 加载 WikiText-2 (语言建模经典数据集，体积小适合 Colab)
dataset = load_dataset("wikitext", "wikitext-2-raw-v1")

print(f"训练集大小: {len(dataset['train'])} 条")
print(f"验证集大小: {len(dataset['validation'])} 条")
print(f"测试集大小: {len(dataset['test'])} 条")

# 查看数据
print(f"\n示例:")
print(dataset['train'][100]['text'][:200])

def clean_text(example):
    """清洗文本：去除空行、过短文本"""
    text = example['text'].strip()
    # 过滤空行和太短的行
    example['text'] = text
    example['is_valid'] = len(text) > 20  # 至少20字符
    return example

# 清洗
dataset = dataset.map(clean_text)

# 过滤无效数据
train_data = dataset['train'].filter(lambda x: x['is_valid'])
val_data = dataset['validation'].filter(lambda x: x['is_valid'])
test_data = dataset['test'].filter(lambda x: x['is_valid'])

print(f"清洗后训练集: {len(train_data)} 条")
print(f"清洗后验证集: {len(val_data)} 条")

# 拼接为长文本 (语言建模需要连续文本)
full_train_text = "\n".join(train_data['text'])
full_val_text = "\n".join(val_data['text'])

print(f"\n训练文本总长度: {len(full_train_text):,} 字符")
print(f"验证文本总长度: {len(full_val_text):,} 字符")

# save_to_drive("/content/tokenizer.json")
```

![1779675412276](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779675412276.png)

# 2.Transformer

## 2.1 NLP

自然语言处理（NLP）的核心挑战在于让机器理解人类语言——这种充满歧义、依赖语境、且不断演变的符号系统。

神经网络语言模型（NNLM）的突破在于将离散的词映射为连续向量。2003年Bengio提出的前馈神经网络语言模型首次使用词嵌入（word embedding）——每个词被表示为稠密向量，语义相似的词在向量空间中距离相近。模型通过三层神经网络计算概率：嵌入层将词索引映射为向量，隐藏层进行非线性变换，输出层通过softmax计算词汇表上的概率分布。

从静态到动态，从单向到双向，从浅层到深层——词嵌入技术的演进反映了NLP从表象到本质的认知深化。

从概率计算到文本生成，语言模型经历了从工具到创造者的转变。

编码器-解码器架构将序列到序列建模分为两步：编码器将输入序列压缩为固定长度向量（上下文向量），解码器基于该向量生成输出序列。这种架构在机器翻译中表现优异，但瓶颈在于上下文向量容量有限——需要将整个输入序列信息压缩到固定维度。(Transformer)

注意力机制的引入打破了这一限制。解码器在生成每个词时，可以动态关注输入序列的不同部分，而不是依赖单一的上下文向量。这就像翻译时随时回看原文相关段落，而不是只凭一次阅读的记忆。

从RNN到LSTM，从编码器-解码器到注意力机制，序列建模的演进方向是更精细的信息流动控制和更灵活的记忆访问机制。

注意力机制的本质是信息检索：查询是问题，键是索引，值是内容。模型学会根据当前需要，从记忆库中提取相关信息。这种机制不仅用于NLP，还扩展到计算机视觉、语音处理等领域，成为深度学习的基础构件。

Transformer的核心优势是完全基于注意力，消除了循环连接，使训练高度并行化。它能够直接建模任意距离的依赖关系，不受梯度消失困扰。这种架构成为大语言模型的基础，催生了BERT、GPT、T5等系列模型。

## 2.2 Transformer模型实现NLP

Transformer模型（框架）

大语言模型的底座

使用GPU设备进行Transformer库的使用

使用环境依赖：

pip install -q transformers tokenizers datasets jieba



> 谷歌的Colab

输入以下代码进行验证环境

```python
import torch
import transformers
import numpy as np

def check_environment():
    """验证开发环境是否正常"""
    
    # 检查PyTorch
    print(f"PyTorch版本: {torch.__version__}")
    print(f"CUDA可用: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"CUDA版本: {torch.version.cuda}")
        print(f"GPU设备: {torch.cuda.get_device_name(0)}")
        print(f"GPU数量: {torch.cuda.device_count()}")
    
    # 检查Transformers
    print(f"\nTransformers版本: {transformers.__version__}")
    
    # 简单张量计算测试
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    x = torch.randn(3, 3).to(device)
    y = torch.randn(3, 3).to(device)
    z = torch.matmul(x, y)
    print(f"\nGPU计算测试: 矩阵乘法完成，结果形状 {z.shape}")
    
    # 内存测试
    if torch.cuda.is_available():
        print(f"当前GPU内存占用: {torch.cuda.memory_allocated() / 1024**2:.2f} MB")
        print(f"GPU总内存: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f} GB")
    
    return True

if __name__ == "__main__":
    check_environment()
```

![1779680090142](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779680090142.png)



## 2.3 Transformer

Hugging Face Transformers 是一个开源的自然语言处理（NLP）库，提供了数千个预训练模型，支持以下任务：

- 📝 **文本分类**（情感分析、垃圾邮件检测）
- 🔍 **信息抽取**（命名实体识别、关系抽取）
- ❓ **问答系统**
- 📖 **文本摘要**
- 🌐 **机器翻译**
- ✍️ **文本生成**
- 🎵 **语音识别**
- 🖼️ **图像分类**

Transformers 

统一的API接口，简单易用
支持PyTorch、TensorFlow、JAX三大框架
超过10万个预训练模型
活跃的社区支持
生产级别的性能

![1779680692566](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779680692566.png)

Pipeline 是 Transformers 库中最简单的推理方式，将 **预处理→模型推理→后处理** 封装成一个完整的流程。

输入文本 → [Tokenizer] → [Model] → [后处理] → 输出结果

## 2.4 Transformer初体验

实现如下代码：

```python
# NLP 情感分类
from transformers import pipeline

# 创建情感分析Pipeline
classifier = pipeline("sentiment-analysis")

# 单个文本
result = classifier("I love using Transformers library!")
# result=classifier("我讨厌深度学习！")
print(result)
```

![1779681001932](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779681001932.png)

文本生成：

```python
# 文本生成
from transformers import pipeline

# 创建文本生成Pipeline
generator = pipeline("text-generation", model="gpt2")

# 基础文本生成
result = generator(
    "Once upon a time in a land far away,",
    max_length=100,          # 最大生成长度
    num_return_sequences=3,  # 返回3个不同的生成结果
    temperature=0.8,         # 控制随机性（越高越随机）
    do_sample=True           # 启用采样
)

for i, text in enumerate(result):
    print(f"\n--- 生成结果 {i+1} ---")
    print(text['generated_text'])
```

![1779681322673](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779681322673.png)

## 2.5 NLP文本分类

情感分析:     "这部电影太棒了！" → 积极
新闻分类:     "特斯拉发布新车型" → 科技
垃圾邮件检测:  "恭喜中奖100万"  → 垃圾
意图识别:     "帮我订一张机票"  → 订票意图

采用Transformer模型直接实现

不训练直接使用

```python
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

# 模型
model = AutoModelForSequenceClassification.from_pretrained(
    "bert-base-chinese",
    num_labels=2,
)
tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
classifier = pipeline(
    "text-classification",  # 任务类型：文本分类
    model=model,           # 训练好的模型
    tokenizer=tokenizer,   # 对应的分词器
    device=0,              # 指定推理设备
)
str1="我不怎么喜欢深度学习！"
r1=classifier(str1)
print(r1)
```

![1779690914273](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779690914273.png)

重新训练模型

```python
# Transformer 实现NLP的文本分类

# 导入 Hugging Face 的数据集处理库，Dataset 是处理数据的核心类
from datasets import Dataset

# 导入 Transformers 库中的核心组件
from transformers import (
    AutoTokenizer,                 # 自动加载分词器（将文本转为ID）
    AutoModelForSequenceClassification, # 自动加载带分类头的预训练模型
    TrainingArguments,              # 训练参数配置类
    Trainer,                        # 负责训练和评估的高级API
    pipeline,                       # 便捷的推理管道
)
# import numpy 是为了后面计算准确率时使用 mean() 方法
import numpy as np

# ---------- 1. 准备数据 ----------
# 在实际工业项目中，通常使用 load_dataset("csv", data_files="train.csv") 从文件读取
# 这里我们构造一个字典来模拟数据
data = {
    "text": [
        "这部电影太精彩了，强烈推荐！",
        "质量很差，非常失望",
        "还不错吧，中规中矩",
        "服务态度极差，再也不来了",
        "超出预期，物超所值！",
        "包装破损，退货了",
        "性价比很高，值得购买",
        "配送太慢了，等了一周",
    ],
    # 标签：1代表正面（Positive），0代表负面（Negative）
    "label": [1, 0, 1, 0, 1, 0, 1, 0],
}

# 将 Python 字典转换为 Hugging Face 的 Dataset 对象，便于后续处理
dataset = Dataset.from_dict(data)
# 将数据集拆分为训练集和测试集
# test_size=0.25 表示 25% 的数据作为测试集（这里是 2 条），其余 75% 作为训练集（6 条）
# seed=42 设置随机种子，确保每次运行分割结果一致（可复现性）
dataset = dataset.train_test_split(test_size=0.25, seed=42)
# ---------- 2. 加载模型与分词器 ----------
# 指定预训练模型名称，这里使用的是谷歌官方的 bert-base-chinese
MODEL_NAME = "bert-base-chinese"
# 加载分词器：负责将中文句子切分成 Token 并转换为模型能理解的 ID
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
# 加载模型：
# num_labels=2 表示这是一个二分类任务（正面/负面）
# from_pretrained 会自动下载模型权重并初始化分类头
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=2,
)
# ---------- 3. 数据预处理 ----------
# 定义预处理函数，用于将原始文本转换为模型输入格式
def preprocess(examples):
    return tokenizer(
        examples["text"],       # 输入的文本数据
        padding="max_length",   # 将所有样本填充到最大长度（这里是128）
        truncation=True,        # 如果文本超过最大长度，则截断
        max_length=128,         # 设定序列的最大长度（BERT通常支持512，这里128足够）
    )
# 使用 map 函数批量处理数据集
# batched=True 表示一次性处理一批数据，速度更快
tokenized = dataset.map(preprocess, batched=True)
# ---------- 4. 训练配置 ----------
# 定义训练参数
training_args = TrainingArguments(
    output_dir="./results",     # 训练结果（模型权重、日志）的保存目录
    num_train_epochs=10,         # 整个数据集遍历 3 遍
    per_device_train_batch_size=8,  # 训练时每个 GPU/CPU 的设备批次大小为 8
    per_device_eval_batch_size=16,  # 评估时的批次大小
    learning_rate=2e-5,         # 学习率：BERT 微调时的黄金标准（通常在 2e-5 到 5e-5 之间）
    weight_decay=0.01,          # 权重衰减（L2正则化），防止过拟合
    eval_strategy="epoch",       # 每个 epoch 结束后进行一次评估
    save_strategy="epoch",       # 每个 epoch 结束后保存一次模型
    load_best_model_at_end=True,# 训练结束时，加载在评估集上表现最好的模型
    metric_for_best_model="accuracy", # 依据准确率来挑选最佳模型
    logging_steps=10,           # 每 10 步打印一次日志
    fp16=True,                  # 开启混合精度训练（FP16），利用 GPU Tensor Cores 加速并节省显存
)
# 定义评估函数，用于计算模型性能
def compute_metrics(eval_pred):
    # eval_pred 是一个元组，包含 (logits, labels)
    logits, labels = eval_pred
    # logits 形状为 (batch_size, num_labels)，取 argmax 得到预测类别（0 或 1）
    predictions = np.argmax(logits, axis=-1)
    # 计算准确率：(预测正确的数量 / 总数量)
    accuracy = (predictions == labels).mean()
    return {"accuracy": accuracy}
# ---------- 5. 训练 ----------
# 初始化 Trainer（训练器）
trainer = Trainer(
    model=model,                # 待训练的模型
    args=training_args,         # 训练参数
    train_dataset=tokenized["train"],   # 训练数据集
    eval_dataset=tokenized["test"],    # 评估/测试数据集
    compute_metrics=compute_metrics,    # 评估指标计算函数
)
# 开始训练！这一步会启动微调过程
trainer.train()
# ---------- 6. 推理 ----------
# 方式A: 使用 Pipeline（最简单，封装了预处理和后处理）
# device=0 表示使用第一块 GPU；如果是 CPU 则设为 -1
classifier = pipeline(
    "text-classification",  # 任务类型：文本分类
    model=model,           # 训练好的模型
    tokenizer=tokenizer,   # 对应的分词器
    device=0,              # 指定推理设备
)

# 进行单条预测
result = classifier("我不怎么喜欢深度学习！")
print(f"预测结果: {result}")  # 输出

```

![1779691132995](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779691132995.png)

![1779691469393](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779691469393.png)

练习：基于Transformer模型实现中文相关的文本分类

数据集：https://www.modelscope.cn/datasets?Tags=text-classification&dataType=text&page=1



## 2.6 NLP命名实体抽取

从文本中提取实体:

  "马云于1999年在杭州创立阿里巴巴"
​    ↓ NER
  马云 → 人名(PER)    1999 → 时间(DATE)
  杭州 → 地点(LOC)    阿里巴巴 → 组织(ORG)

应用: 信息抽取、知识图谱构建、智能客服

代码示例：

```Python
# NLP 文本特征抽取
# ============================================================
# NER 实战: 使用 BERT 进行中文命名实体识别 (全注释版)
# ============================================================

# 导入必要的库
from transformers import (
    AutoTokenizer,  # 用于加载分词器，将文本转为ID
    AutoModelForTokenClassification,  # 用于加载带分类头的BERT模型（Token级）
    TrainingArguments,  # 训练参数配置类
    Trainer,  # 负责训练和评估的高级API
    DataCollatorForTokenClassification,  # 专门用于Token分类的数据整理器（自动Padding）
    pipeline,  # 便捷的推理管道
)
from datasets import Dataset  # Hugging Face 的数据集管理类
import torch  # PyTorch 库
import numpy as np  # 数值计算库（虽然这里没直接用，但通常是标配）

# ---------- 1. 准备数据 ----------
# 注意：真实项目中，数据通常是 CoNLL 格式或 JSON。
# 这里我们用一个极简的例子演示。
# tokens: 已经分好词的列表（注意：BERT 会再次进行子词切分）
# ner_tags: 对应的 BIO 标签索引 (基于下面的 label_list)
data = {
    "tokens": [
        ["马", "云", "于", "杭", "州", "创", "立", "阿", "里", "巴", "巴"],
        ["李", "彦", "宏", "创", "立", "百", "度"],
    ],
    "ner_tags": [
        [1, 2, 0, 5, 6, 0, 0, 3, 4, 4, 4],  # 马云(PER), 杭州(LOC), 阿里巴巴(ORG)
        [1, 2, 2, 0, 0, 3, 4],  # 李彦宏(PER), 百度(ORG)
    ]
}

# 定义标签列表（BIO 体系）
# 注意：顺序很重要，索引 0 通常对应 "O"
label_list = ["O", "B-PER", "I-PER", "B-ORG", "I-ORG", "B-LOC", "I-LOC"]

# 创建标签到 ID 和 ID 到标签的映射字典（模型内部使用数字 ID 进行训练）
label2id = {l: i for i, l in enumerate(label_list)}  # 如 {"O": 0, "B-PER": 1, ...}
id2label = {i: l for i, l in enumerate(label_list)}  # 如 {0: "O", 1: "B-PER", ...}

# 将 Python 字典转换为 Hugging Face 的 Dataset 对象，便于后续处理
dataset = Dataset.from_dict(data)

# ---------- 2. 加载模型与分词器 ----------
# 指定预训练模型名称，这里使用的是谷歌官方的 bert-base-chinese
MODEL_NAME = "bert-base-chinese"

# 加载分词器：负责将中文句子切分成 Token 并转换为模型能理解的 ID
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# 加载模型：
# num_labels=7 表示这是一个 7 分类任务（对应 label_list 的长度）
# id2label/label2id: 传入映射关系，方便模型在推理时输出标签字符串而不是数字
model = AutoModelForTokenClassification.from_pretrained(
    MODEL_NAME,
    num_labels=len(label_list),
    id2label=id2label,
    label2id=label2id,
)


# ---------- 3. 数据预处理 (核心难点：标签对齐) ----------
def tokenize_and_align_labels(examples):
    # 分词器处理：
    # is_split_into_words=True: 告诉分词器输入已经是单词列表，而不是一个长字符串
    # return_offsets_mapping=True: 获取偏移量，用于对齐标签（虽然下面删除了，但调试时有用）
    tokenized_inputs = tokenizer(
        examples["tokens"],
        truncation=True,
        is_split_into_words=True,
        return_offsets_mapping=True,
    )

    labels = []
    # 遍历 batch 中的每一个样本
    for i, label in enumerate(examples["ner_tags"]):
        # 获取当前样本的 word_ids
        # word_ids 是一个列表，比如 [None, 0, 1, 1, 2, None...]
        # (None表示特殊符号[CLS]/[SEP]，数字表示该token对应原句中的第几个词)
        word_ids = tokenized_inputs.word_ids(batch_index=i)

        previous_word_idx = None
        label_ids = []

        # 遍历每一个 token 的 word_id
        for word_idx in word_ids:
            if word_idx is None:
                # 特殊符号 ([CLS], [SEP], [PAD]) 的标签设为 -100
                # 计算 loss 时会自动忽略 -100 的标签
                label_ids.append(-100)
            elif word_idx != previous_word_idx:
                # 这是一个新词的开头（或者 BERT 没拆分的词）
                # 直接赋予该词对应的标签
                label_ids.append(label[word_idx])
            else:
                # 这是同一个词的后续 subword (例如 "阿" 和 "##里")
                # 通常策略是给后续 subword 打上对应的 I-xxx 标签
                # 这里我们采用常用策略：如果是 B-xxx，后续 subword 变为 I-xxx
                current_label = label[word_idx]
                if current_label == 1 or current_label == 3 or current_label == 5:  # B-xxx
                    label_ids.append(current_label + 1)  # 转为 I-xxx (因为列表里 B 和 I 是挨着的)
                else:
                    label_ids.append(current_label)

            previous_word_idx = word_idx

        labels.append(label_ids)

    tokenized_inputs["labels"] = labels
    # 训练时不需要 offsets，删掉节省内存
    tokenized_inputs.pop("offset_mapping")
    return tokenized_inputs


# 应用预处理函数
# batched=True 表示一次性处理一批数据，速度更快
tokenized_dataset = dataset.map(tokenize_and_align_labels, batched=True)

# ---------- 4. 配置训练参数 ----------
# 检查是否有 GPU，决定后续是否开启混合精度
has_gpu = torch.cuda.is_available()

args = TrainingArguments(
    output_dir="ner-bert-chinese",  # 训练结果（模型权重、日志）的保存目录
    eval_strategy="no",  # 数据太少，不进行评估（旧版参数名 evaluation_strategy）
    learning_rate=2e-5,  # 学习率：BERT 微调时的黄金标准
    per_device_train_batch_size=2,  # 训练时每个设备的批次大小（数据少，设小点）
    num_train_epochs=3,  # 整个数据集遍历 3 遍
    weight_decay=0.01,  # 权重衰减（L2正则化），防止过拟合
    fp16=has_gpu,  # 如果有 GPU 则开启混合精度训练（FP16），加速并节省显存
)

# ---------- 5. 定义评估指标 (可选，这里简单演示) ----------
# NER 通常用 F1 Score

# ---------- 6. 训练 ----------
# Data Collator: 自动将不同长度的序列 padding 到同一长度
# 它会根据 tokenizer 自动找到对应的 pad_token，并对 labels 进行特殊处理（将 -100 对应的 pad 也设为 -100）
data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)

# 初始化 Trainer（训练器）
trainer = Trainer(
    model=model,  # 待训练的模型
    args=args,  # 训练参数
    train_dataset=tokenized_dataset,  # 训练数据集
    data_collator=data_collator,  # 数据整理器
)

# 开始训练！这一步会启动微调过程
trainer.train()

# ---------- 7. 推理验证 ----------
# 训练完后，我们可以用管道测试
# aggregation_strategy="simple": 将同一个实体的子词合并成一个完整的词
ner_pipe = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")
result = ner_pipe("马云在杭州创立了阿里巴巴。")
print(result)
```

![1779692532778](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779692532778.png)

## 2.7 NLP摘要生成

长文档 → 短摘要:

  输入 (500字新闻):
​    "今日，国务院新闻办公室举行新闻发布会...
​     (省略400字) ...
​     专家表示，这一政策将对经济产生深远影响。"

  输出 (50字摘要):
​    "国新办发布会宣布新经济政策，专家预计将产生深远影响。"

模型类型: Encoder-Decoder (T5, BART, Pegasus)

代码示例：

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM  # 用于加载 Seq2Seq 模型（编码器-解码器结构）和分词器
import torch                                             # PyTorch 库，用于张量计算和 GPU 加速

# ---------- 中文摘要 ----------
print("\n正在加载中文摘要模型 (mT5-small)...")

# 定义中文模型名称
# google/mt5-small 是 Google 的多语言 T5 模型 (small 版本较小，方便下载和测试)
model_name_zh = "google/mt5-small"

# 加载分词器和模型
tokenizer_zh = AutoTokenizer.from_pretrained(model_name_zh)
model_zh = AutoModelForSeq2SeqLM.from_pretrained(model_name_zh)
device = "cuda" if torch.cuda.is_available() else "cpu"
# 将中文模型移动到设备
model_zh.to(device)

# 定义中文长文本
chinese_text = """
Transformer架构彻底改变了自然语言处理领域。2017年提出的自注意力机制
替代了循环神经网络，实现了并行计算并更好地处理长距离依赖关系。
BERT、GPT、T5等模型均基于Transformer架构构建，在众多基准测试中
取得了最先进的结果。Transformer的成功已从NLP扩展到计算机视觉(ViT)、
音频(Whisper)和多模态应用(CLIP、BLIP)。
"""

# --- 数据预处理 ---
# 注意：mT5 模型通常不需要特定的任务前缀也能做摘要，但有些模型可能需要 "summarize: "
# 这里为了通用性，直接输入文本
inputs_zh = tokenizer_zh(chinese_text, return_tensors="pt", max_length=1024, truncation=True).to(device)

# --- 模型推理 ---
summary_ids_zh = model_zh.generate(
    inputs_zh["input_ids"],
    max_length=80,           # 中文摘要相对较长，设为 80
    min_length=20,
    do_sample=False,
    num_beams=4,            # 使用 Beam Search 保证质量
)

# --- 结果解码 ---
summary_text_zh = tokenizer_zh.decode(summary_ids_zh[0], skip_special_tokens=True)
print(f"中文摘要: {summary_text_zh}")
```

![1779693018328](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779693018328.png)

## 2.8 NLP翻译

把一种语言转换为另一种语言

中->英

中-->日

支持100多种语言翻译的模型

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
# 将模型移动到 GPU (如果可用)，加速推理
device = "cuda" if torch.cuda.is_available() else "cpu"
# ---------- 3. m2m100 多语言互译 (Many-to-Many) ----------
print("\n正在加载多语言翻译模型 (facebook/m2m100_418M)...")

# m2m100 是一个支持 100+ 语言互译的模型
model_name_m2m = "facebook/m2m100_418M"
tokenizer_m2m = AutoTokenizer.from_pretrained(model_name_m2m)
model_m2m = AutoModelForSeq2SeqLM.from_pretrained(model_name_m2m)
model_m2m.to(device)


def translate_m2m(text, src_lang, tgt_lang):
    """
    使用 m2m100 进行翻译的函数
    :param text: 待翻译文本
    :param src_lang: 源语言代码 (如 'en', 'zh', 'fr')
    :param tgt_lang: 目标语言代码
    """
    # 设置源语言 (告诉分词器这是什么语言)
    tokenizer_m2m.src_lang = src_lang

    # 分词
    encoded = tokenizer_m2m(text, return_tensors="pt").to(device)

    # 生成翻译
    # forced_bos_token_id: 强制模型在开始时生成目标语言的 Token
    # 这是 m2m100 模型特有的要求
    generated_tokens = model_m2m.generate(
        **encoded,
        forced_bos_token_id=tokenizer_m2m.get_lang_id(tgt_lang),
        max_length=128
    )

    # 解码并返回结果
    return tokenizer_m2m.batch_decode(generated_tokens, skip_special_tokens=True)[0]


# 示例调用
# 注意：m2m100 的语言代码通常是标准的 (en, zh, fr, ja, ko 等)
print("英→法:","原文：Hello, how are you?", translate_m2m("Hello, how are you?", "en", "fr"))
print("中→日:","原文：你好，你好吗", translate_m2m("你好，你好吗？", "zh", "ja"))
print("法→韩:","原文：Bonjour", translate_m2m("Bonjour", "fr", "ko"))
```

![1779693706124](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779693706124.png)



# 3.Transformer核心

| 组件          | 作用          | 主要类                         |
| ------------- | ------------- | ------------------------------ |
| **Tokenizer** | 文本转Token   | `AutoTokenizer`                |
| **Model**     | 特征提取/预测 | `AutoModel`, `AutoModelForXxx` |
| **Pipeline**  | 端到端推理    | `pipeline()`                   |

Transformer目前不仅仅支持NLP(自然语言处理 文本内容)还支持多模态（图片、音频、视频）

## 3.1 Tokenizer

把内容（文本、音频、图片、视频）转换为词元（Token）

原始内容 → 分词 → 转为Token ID → 添加特殊Token → 填充/截断 → 模型输入
"Hello World" → ["Hello", "World"] → [7592, 2088] → [101, 7592, 2088, 102]

推荐使用AutoTokenizer

```python
# 词元处理
# Auto类可以自动识别模型类型，无需手动指定
from transformers import AutoTokenizer, BertTokenizer

# 方式一：使用Auto类（推荐）
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
# 查看tokenizer信息
print("---AutoTokenizer---")
print(f"词汇表大小: {tokenizer.vocab_size}")
print(f"最大长度: {tokenizer.model_max_length}")
print(f"特殊Token: {tokenizer.special_tokens_map}")
# 方式二：使用特定Tokenizer类
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
# 查看tokenizer信息
print("---BertTokenizer---")
print(f"词汇表大小: {tokenizer.vocab_size}")
print(f"最大长度: {tokenizer.model_max_length}")
print(f"特殊Token: {tokenizer.special_tokens_map}")
# 加载中文tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
print("---AutoTokenizer中文---")
# 查看tokenizer信息
print(f"词汇表大小: {tokenizer.vocab_size}")
print(f"最大长度: {tokenizer.model_max_length}")
print(f"特殊Token: {tokenizer.special_tokens_map}")
```

![1779697954292](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779697954292.png)



具体的工作流程

```python
# 词元转换
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "Hello, I'm learning Transformers library!"
print("原文：",text)
# 1. 分词
tokens = tokenizer.tokenize(text)
print(f"分词结果: {tokens}")
# ['hello', ',', 'i', "'", 'm', 'learning', 'transformers', 'library', '!']

# 2. 转为ID
token_ids = tokenizer.convert_tokens_to_ids(tokens)
print(f"Token IDs: {token_ids}")

# 3. 完整编码（推荐方式）
encoding = tokenizer(text)
print(f"\n完整编码结果:")
print(f"input_ids: {encoding['input_ids']}")
print(f"attention_mask: {encoding['attention_mask']}")
print(f"token_type_ids: {encoding['token_type_ids']}")
```

![1779698180349](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779698180349.png)

可以详细详细设置参数：

```
# 编码时的常用参数
encoding = tokenizer(
    text,
    max_length=128,              # 最大序列长度
    padding="max_length",        # 填充到最大长度
    truncation=True,             # 超出时截断
    return_tensors="pt",         # 返回PyTorch张量（'tf'为TensorFlow）
    add_special_tokens=True,     # 添加[CLS]和[SEP]等特殊token
    return_attention_mask=True,  # 返回attention mask
    return_token_type_ids=True   # 返回token type ids
)
```

也可以处理句对

```
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# 句对任务（如问答、自然语言推理）
question = "What is the capital of France?"
context = "France is a country in Western Europe. Paris is its capital city."

encoding = tokenizer(
    question,  # 第一个句子
    context,   # 第二个句子
    max_length=128,
    padding="max_length",
    truncation=True,
    return_tensors="pt"
)

# token_type_ids区分两个句子：0表示第一句，1表示第二句
print(f"token_type_ids: {encoding['token_type_ids']}")
```

解码：

```
# 编码
text = "Hello, Transformers!"
encoding = tokenizer(text)
input_ids = encoding['input_ids']

print(f"原始文本: {text}")
print(f"编码后IDs: {input_ids}")

# 解码方式一：decode（还原单个序列）
decoded = tokenizer.decode(input_ids)
print(f"解码结果（含特殊token）: {decoded}")

# 方式二：跳过特殊token
decoded_clean = tokenizer.decode(input_ids, skip_special_tokens=True)
print(f"解码结果（不含特殊token）: {decoded_clean}")

# 方式三：批量解码
batch_ids = [[101, 7592, 102], [101, 2088, 102]]
batch_decoded = tokenizer.batch_decode(batch_ids, skip_special_tokens=True)
print(f"批量解码: {batch_decoded}")
```

## 3.2 Pipeline

Pipeline 是 Transformers 库中最简单的推理方式，将 **预处理→模型推理→后处理** 封装成一个完整的流程。

输入文本 → [Tokenizer] → [Model] → [后处理] → 输出结果

比如实现问答：

```
from transformers import pipeline

# 创建问答Pipeline
qa = pipeline("question-answering")

# 准备上下文和问题
context = """
Hugging Face is a company based in New York City. 
It was founded in 2016 by Clément Delangue, Julien Chaumond, and Thomas Wolf.
The company is known for its Transformers library which provides thousands 
of pretrained models for natural language processing tasks.
"""

question = "When was Hugging Face founded?"

result = qa(question=question, context=context)
print(f"答案: {result['answer']}")
print(f"置信度: {result['score']:.4f}")
print(f"答案位置: {result['start']} - {result['end']}")
```

![1779698894378](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779698894378.png)

> 可用的Pipeline任务：available tasks are ['any-to-any', 'audio-classification', 'automatic-speech-recognition', 'depth-estimation', 'document-question-answering', 'feature-extraction', 'fill-mask', 'image-classification', 'image-feature-extraction', 'image-segmentation', 'image-text-to-text', 'image-to-image', 'keypoint-matching', 'mask-generation', 'ner', 'object-detection', 'question-answering', 'sentiment-analysis', 'table-question-answering', 'text-classification', 'text-generation', 'text-to-audio', 'text-to-speech', 'token-classification', 'video-classification', 'visual-question-answering', 'vqa', 'zero-shot-audio-classification', 'zero-shot-classification', 'zero-shot-image-classification', 'zero-shot-object-detection', 'translation_XX_to_YY']"

零样本分类：

```
from transformers import pipeline

# 创建零样本分类Pipeline（无需专门训练即可分类）
classifier = pipeline("zero-shot-classification")

text = "I need to buy a new laptop for programming"

# 自定义候选标签
candidate_labels = ["technology", "sports", "cooking", "shopping", "travel"]

result = classifier(text, candidate_labels)

print("零样本分类结果:")
for label, score in zip(result['labels'], result['scores']):
    print(f"  {label}: {score:.4f}")
```

![1779699017282](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779699017282.png)

## 3.3 Model

Transformer提供了很多模型（预训练模型），可以加载使用，进行二次训练（微调）

https://huggingface.co/models

![1779699560809](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779699560809.png)

```python
from transformers import AutoModel, AutoTokenizer
import torch

# 加载模型和Tokenizer
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# 查看模型信息
print(f"模型类型: {type(model)}")
print(f"模型参数量: {sum(p.numel() for p in model.parameters()):,}")
print(f"模型配置:\n{model.config}")
```

![1779699444056](D:\class\2603\随堂笔记\第九周\AI大模型开发之42Transformer二.assets\1779699444056.png)

# 4.今日总结



# 5.作业

