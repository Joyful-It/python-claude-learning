# AI大模型开发之41Transformer一



# 0.课程内容

## 0.1 晨考



## 0.2 课程回顾

RNN 循环神经网络

实现序列数据建模

和时间有关系

擅长语义、短语、句子等处理

是主流的深度学习模型

> 数据的前置处理：把句子转换为数字数组
>
> 分词
>
> 词向量
>
> 填充对齐

1.词嵌入层

​	处理句子转换的词

2.nn.rnn()

> 怎么实现的最终解决了序列数据
>
> 时间线和数据



RNN变体

LSTM: 引入门控机

​	输入门

​	遗忘门

​	输出门

GRU：优化了门控机

​	更新门

​	重置门



# 1.Transformer

## 1.1 Transformer

Transformer 是一种基于注意力机制的深度学习模型，最初由 Vaswani 等人在 2017 年的论文《Attention is All You Need》中提出。

它彻底改变了自然语言处理（NLP）领域，并逐渐扩展到计算机视觉等几乎所有 AI 方向。

NLP 领域主要依赖 RNN（循环神经网络）系列模型（如 LSTM、GRU），它们按顺序处理文本，存在两个关键缺陷。

> NLP 自然语言处理，能听懂人话，还可以响应人话

RNN 的局限性

RNN 像人类"逐字阅读"一样处理文本，这带来了以下问题：

- **梯度消失：**处理长文本时，模型会"忘记"较早的信息。例如"我昨天在图书馆借了一本关于量子物理的书"中，读到"书"时早已忘记"我"是主语，长距离依赖极难捕捉。
- **无法并行：**RNN 必须按顺序处理每一个词，无法利用 GPU 的并行计算能力，训练超长文本时速度极慢。

![1779415631309](D:\class\2603\随堂笔记\第八周\AI大模型开发之41Transformer一.assets\1779415631309.png)

Transformer 的解决方案：

- **注意力机制**：让每个词直接 "看到" 所有词，建立全局关联
- **并行计算**：所有位置同时处理，训练速度提升数十倍
- **位置编码**：注入序列顺序信息，弥补无循环结构的缺陷

|              | RNN                      | Transformer                   |
| ------------ | ------------------------ | ----------------------------- |
| **计算方式** | 串行（一个接一个）       | 并行（同时计算所有词）        |
| **速度**     | 慢，序列越长越慢         | 快，GPU 并行加速              |
| **长程依赖** | 信息一步步传，远了就忘了 | 一步直达，无论距离多远        |
| **能否扩展** | 层数多了梯度消失         | 残差连接 + LayerNorm 保证稳定 |
| **结果**     | 难以训练超大模型         | 可以训练几千亿参数的大模型 ★  |

> **关键**：Transformer 的并行能力意味着——**只要 GPU 够多，就能训练更大的模型**。这就是大模型时代的基础！RNN 做不到，因为串行计算没法加速。

![1779436017553](D:\class\2603\随堂笔记\第八周\AI大模型开发之41Transformer一.assets\1779436017553.png)

## 1.2 Transformer架构图

![1779416063026](D:\class\2603\随堂笔记\第八周\AI大模型开发之41Transformer一.assets\1779416063026.png)

![1779427798561](D:\class\2603\随堂笔记\第八周\AI大模型开发之41Transformer一.assets\1779427798561.png)

Transformer核心组成：

![1779416100680](D:\class\2603\随堂笔记\第八周\AI大模型开发之41Transformer一.assets\1779416100680.png)

Transformer 模型由 编码器（Encoder） 和 解码器（Decoder） 两部分组成，每部分都由多层堆叠的相同模块构成。

![1779416235017](D:\class\2603\随堂笔记\第八周\AI大模型开发之41Transformer一.assets\1779416235017.png)

Transformer 就是一个"翻译机"：给它一串输入文字，它输出一串文字。

它可以是：

- 中→英翻译（输入中文，输出英文）
- 摘要生成（输入长文，输出摘要）
- 对话（输入你的问题，输出回答）—— ChatGPT 就是这么干的



## 1.3 自注意力机制

Self-Attention 的结构在计算每个 Token 的时候，总是会考虑到整个序列其他 Token 的表达。

目的是学习句子内部的词的依赖关系，捕获句子的内部结构。

> 我爱北京天安门，所以我想去______看____
>
> 我	爱	北京  天安门
>
> 0.2	0.5	0.4	0.3
>
> 0.1  0.45  0.3  0.15
>
> 爱 北京 天安门

查询 (Query):  "我在找什么？"     → Q
键   (Key):    "我是关于什么的？"  → K
值   (Value):  "我包含什么信息？"  → V

QKV范式

> 想象一下，你走进一座巨大的图书馆，要写一篇关于“恐龙灭绝”的报告。这个过程中你会用到三个动作：
>
> 1. **Query (查询)**：你大脑里的疑问，比如“小行星撞击对恐龙的影响是什么？”这就是你的**Q**。
> 2. **Key (关键词)**：你走到书架前，每本书的目录或侧脊标签就是它的**K**，比如“小行星”、“白垩纪”、“火山活动”。
> 3. **Value (内容)**：你翻开书，里面具体的一段段文字描述，就是这本书的**V**。
>
> Transformer做的第一件事，就是把输入的一句话（比如“小行星撞击导致了恐龙灭绝”），复制三份，分别通过三个“翻译官”（三个不同的参数矩阵 WQ, WK, WV），将每个词变成三种不同的“身份牌”：
>
> - **查询牌 (Q)**：“我关心什么？”
> - **关键词牌 (K)**：“我提供了什么线索？”
> - **内容牌 (V)**：“我的真实信息是什么？”
>
> 模型的目标就是：拿着每个词的“查询牌”(Q)，去和整句话里所有词的“关键词牌”(K)对比亲密度（计算相似度），然后根据这个亲密度，去加权融合所有词的“内容牌”(V)。这样，“撞击”这个词就能从“小行星”和“恐龙”那里都获取到重要信息。

计算过程：

1.投影 

X->Q K V



2.计算注意力分数

3.归一化处理

> 每行的权重和为1

4.加权求和

获取权重排名

![1779419561052](D:\class\2603\随堂笔记\第八周\AI大模型开发之41Transformer一.assets\1779419561052.png)

```python
# 单头注意力
import torch
import torch.nn.functional as F
import math
# 输入的内容 转换 QKV
# 3 个词的向量 (已经经过 Q/K/V 投影)
print("1.QKV投影")
Q = torch.tensor([
    [1.0, 0.0, 1.0, 0.0],   # 词1 的 Query
    [0.0, 1.0, 0.0, 1.0],   # 词2 的 Query
    [1.0, 1.0, 0.0, 0.0],   # 词3 的 Query
])

K = torch.tensor([
    [1.0, 0.0, 0.0, 1.0],   # 词1 的 Key
    [0.0, 1.0, 1.0, 0.0],   # 词2 的 Key
    [1.0, 0.0, 1.0, 0.0],   # 词3 的 Key
])

V = torch.tensor([
    [1.0, 2.0, 3.0, 4.0],   # 词1 的 Value
    [5.0, 6.0, 7.0, 8.0],   # 词2 的 Value
    [9.0, 10.0, 2.0, 3.0],  # 词3 的 Value
])

print("2.计算注意力分数")
# 点积
print("每个词的 Query 和所有词的 Key 做点积，看'有多相关'\n")
# 注意力分数
score1=Q@K.T
print(score1)
dk=Q.size(-1)
score1=score1/math.sqrt(dk)
print("注意力分数：\n",score1)
# 归一化处理 每个词的权重和=1
score2=F.softmax(score1,dim=-1)
print(score2)
# 加权求和 V
output = score2 @ V
print("自注意力计算结果：\n",output)
# 手动验证第1行
row0 = score2[0, 0] * V[0] + score2[0, 1] * V[1] + score2[0, 2] * V[2]
print(f"手动验证词1的输出: {row0.round()}")
print(f"和矩阵乘法结果一致: {torch.allclose(output[0], row0, atol=1e-3)}")
print("\n注意力机制 = 点积打分 → 缩放 → Softmax → 加权求和")
```

## 1.4 多头注意力

单头注意力的问题：
  - 只能学一种"关注模式"
  - 一个注意力头可能关注语法关系，另一个关注语义关系
  - 就像只让一个人读文章，他可能只注意到情节，忽略文风

多头注意力的思想：
  - 让模型同时从多个"视角"关注序列
  - 每个头学习不同的注意力模式
  - 最后拼接所有头的输出，融合多元信息

> 如果只用一个“寻宝团队”，可能只会关注一种信息。比如只关注“谁导致了谁”这种因果关系。但真实世界的信息是复杂的，我们可能还需要关注“时间顺序”、“地点关联”、“修饰关系”等等。
>
> 为此，Transformer组建了**多头注意力**机制。它会把“查询牌”、“关键词牌”、“内容牌”复制成好几组（比如8组或12组），每组交给一个独立的“专家团队”去处理，每个团队有不同的“翻译官”（不同的参数矩阵）。
>
> - **团队A** 可能专门分析语法结构，关注“主语-谓语”关系。
> - **团队B** 可能专门追踪指代，发现“它”指的是前面的“小行星”。
> - **团队C** 可能专门捕捉情感或修饰色彩。
>
> 最后，把所有“专家团队”的寻宝结果汇总起来，拼接成一个更全面的报告。多头机制让模型能**并行**地从多个角度分析同一句话，理解力大大增强。

计算过程：

1.投影

输入X转变为Q K V->复制多份 Q K V一组

2.每个头各自计算注意力分数

3.拼接所有头的结果

4.转换线性

> 我爱北京天安门，所以我想去北京
>
> Q  
>
> K
>
> V
>
> 2个头计算 
>
> 合并
>
> 线性
>
> 我 爱 北京 天安门
>
> 0.1 0.2 0.4 0.3

```python
# 多头 注意力机制
import torch
import torch.nn.functional as F
import math
from torch import nn

# 自注意力计算 权重
def scaled_dot_product_attention(Q, K, V, mask=None):
    """
    缩放点积注意力 —— 最核心的函数

    参数:
        Q: Query   形状 [..., seq_q, d_k]  "我在找什么"
        K: Key     形状 [..., seq_k, d_k]  "我的标签是什么"
        V: Value   形状 [..., seq_v, d_v]  "我的内容是什么"
        mask:      可选, 形状 [..., seq_q, seq_k]
                   True/1 = 可以看, False/0 = 遮住

    返回:
        output:    形状 [..., seq_q, d_v]  注意力输出
        attn_w:    形状 [..., seq_q, seq_k] 注意力权重
    """
    d_k = Q.size(-1)

    # Step 1: 点积打分
    scores = Q @ K.transpose(-2, -1)  # [seq_q, seq_k]

    # Step 2: 缩放
    scores = scores / math.sqrt(d_k)

    # Step 3: 应用掩码(如有) — 被遮住的位置设为 -1e9
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
        # -1e9 经过 softmax ≈ 0, 相当于"不看"这个位置

    # Step 4: Softmax → 注意力权重(每行加起来=1)
    attn_weights = F.softmax(scores, dim=-1)

    # Step 5: 加权求和
    output = attn_weights @ V  # [seq_q, d_v]

    return output, attn_weights

class MultiHeadAttention(nn.Module):
    """多头注意力"""

    def __init__(self, d_model, n_heads, dropout=0.1):
        super().__init__()
        # 基本检查: d_model 必须能被 n_heads 整除
        assert d_model % n_heads == 0, f"d_model={d_model} 不能被 n_heads={n_heads} 整除"

        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_model // n_heads  # 每个头的维度: 512/8 = 64

        # 4 个线性层: 把输入投影成 Q, K, V, 以及最终输出投影
        self.W_Q = nn.Linear(d_model, d_model)  # [512, 512]
        self.W_K = nn.Linear(d_model, d_model)
        self.W_V = nn.Linear(d_model, d_model)
        self.W_O = nn.Linear(d_model, d_model)

        self.dropout = nn.Dropout(dropout)

    def forward(self, query, key, value, mask=None):
        """
        多头注意力的完整流程

        参数:
            query:  [B, seq_q, d_model]  查询
            key:    [B, seq_k, d_model]  键
            value:  [B, seq_v, d_model]  值 (seq_k == seq_v)
            mask:   掩码, 可选

        返回:
            output:  [B, seq_q, d_model]
        """
        B = query.size(0)

        # ---- Step 1: 线性投影 ----
        Q = self.W_Q(query)  # [B, seq_q, 512]
        K = self.W_K(key)  # [B, seq_k, 512]
        V = self.W_V(value)  # [B, seq_v, 512]

        # ---- Step 2: 分头 ----
        # [B, seq, 512] → [B, seq, 8, 64] → [B, 8, seq, 64]
        # 把512维切成8份, 每份64维, 每份就是一个头
        Q = Q.view(B, -1, self.n_heads, self.d_k).transpose(1, 2)
        K = K.view(B, -1, self.n_heads, self.d_k).transpose(1, 2)
        V = V.view(B, -1, self.n_heads, self.d_k).transpose(1, 2)

        # ---- Step 3: 每个头独立计算注意力 ----
        attn_out, attn_weights = scaled_dot_product_attention(Q, K, V, mask)
        # attn_out: [B, 8, seq_q, 64]

        # ---- Step 4: 合并多头 ----
        # [B, 8, seq, 64] → [B, seq, 8, 64] → [B, seq, 512]
        attn_out = attn_out.transpose(1, 2).contiguous().view(B, -1, self.d_model)

        # ---- Step 5: 输出投影 ----
        output = self.W_O(attn_out)  # [B, seq_q, 512]

        return output, attn_weights


# ===== 用小例子验证 =====
d_model = 8  # 极小维度，方便观察
n_heads = 2  # 2个头
seq_len = 4  # 4个词

mha = MultiHeadAttention(d_model, n_heads)
# x = torch.randn(1, seq_len, d_model)  # [1, 4, 8]
x = torch.randint(1,100,(1,4,8),dtype=torch.float)  # [1, 4, 8]
print(x)
out, weights = mha(x, x, x)  # 自注意力: Q=K=V=x
print(f"输入形状: {x.shape}")  # [1, 4, 8]
print(f"输出形状: {out.shape}")  # [1, 4, 8]  ← 形状不变！
print(f"注意力权重形状: {weights.shape}")  # [1, 2, 4, 4]  ← 2个头，每个4×4
print(f"\n每个头学到了不同的注意力模式:")
print(f"  头1 权重:\n{weights[0, 0].detach().round()}")
print(f"  头2 权重:\n{weights[0, 1].detach().round()}")
```

## 1.5 位置编码

只有注意力是无法区分语句的位置关系，就会导致：

猫吃鱼和鱼吃猫 的注意力分数相同的，语义就理解错了

引入了位置编码

Transformer是使用的正弦函数解决的位置编码

sin和cos

但是大模型没有采用正弦函数而是采用RoPE 旋转位置编码

实现位置编码：

```python
def positional_encoding_simple(seq_len, d_model):
    """
    简化版位置编码，手动算一遍
    
    我们用 seq_len=4, d_model=4 的小例子
    """
    import numpy as np
    
    PE = torch.zeros(seq_len, d_model)
    
    for pos in range(seq_len):          # 每个位置
        for i in range(0, d_model, 2):  # 每两个维度一组
            # 计算频率: 10000^(2i/d_model)
            freq = 10000 ** (2 * i / d_model)
            
            # 偶数维度用 sin，奇数维度用 cos
            PE[pos, i]     = math.sin(pos / freq)   # 偶数
            if i + 1 < d_model:
                PE[pos, i + 1] = math.cos(pos / freq)  # 奇数
    
    return PE

# 用 4 个位置、4 个维度来算
pe = positional_encoding_simple(4, 4)
print("位置编码 (4个位置, 4个维度):")
print(pe.round(4))

# 可视化理解
print("\n直观理解:")
for pos in range(4):
    print(f"  位置{pos}: sin({pos}/1)={math.sin(pos):.3f}, "
          f"cos({pos}/1)={math.cos(pos):.3f}, "
          f"sin({pos}/100)={math.sin(pos/100):.4f}, "
          f"cos({pos}/100)={math.cos(pos/100):.4f}")

print("\n→ 前2维变化快(高频), 后2维变化慢(低频)")
```

Embedding 词嵌入层

一般词嵌入层（分词 词向量）+位置编码（记录顺序 词对应的位置）

想象你用 4 个维度来描述一个人：`[身高, 年龄, 收入, 颜值]`

```
张三 → [1.75, 25, 8000, 7]    # 高个子，25岁，月薪8k，颜值7分
李四 → [1.60, 30, 15000, 8]   # 矮一些，30岁，月薪1.5w，颜值8分
```

同样，我们用一串数字来描述一个词：

```
"猫" → [0.2, -0.5, 0.8, 0.1, ...]   # 512个数字
"狗" → [0.3, -0.4, 0.7, 0.2, ...]   # 512个数字，和"猫"很像
"汽车" → [-0.8, 0.9, -0.1, 0.5, ...] # 512个数字，和"猫"差很远
```

>  意思相近的词，数字也相近。这是 Embedding 自然而然学到的。

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

# ===== Step 1: 最简单的 Embedding =====
# 本质：一张"查表"，根据词的编号，查出对应的数字向量

vocab_size = 10    # 词表里只有 10 个词（简化演示）
d_model    = 4     # 每个词用 4 个数字表示（实际通常 512）

# 创建 Embedding 层：本质就是一个 [10, 4] 的查表矩阵
embedding = nn.Embedding(vocab_size, d_model)

# 假设我们的句子是: [词2, 词5, 词1]  (用编号代替文字)
token_ids = torch.tensor([[2, 5, 1]])   # shape: [1, 3] (1句话, 3个词)

# 查表得到向量
embeddings = embedding(token_ids)         # shape: [1, 3, 4] (1句话, 3个词, 每个4维)

print(f"输入: {token_ids}")
print(f"输入形状: {token_ids.shape}       → [句子数, 词数]")
print(f"输出: {embeddings}")
print(f"输出形状: {embeddings.shape}  → [句子数, 词数, 维度]")

# ★ Transformer 的一个小细节：输出要乘以 √d_model
# 原因：Embedding 的值通常很小，而位置编码的值在 [-1,1] 范围
# 乘以 √d_model 让两者量级匹配，相加时 Embedding 不会被淹没
embeddings_scaled = embeddings * math.sqrt(d_model)
print(f"\n缩放后: {embeddings_scaled}")
```



## 1.6 前馈网络

前馈网络 FFN

对注意力机制的结果重新消化吸收

先扩展（4倍）再压缩

基于全连接实现

Transformer实现机制：

1.全连接层 -扩展4倍

2.激活函数 ReLU/GeLU

3.Dropout 随机丢弃 过拟合

4.全连接层-压缩4倍



目前大模型（LLM）普遍采用MoE架构（混合专家 ）实现前馈网络



实现一下FFN

```python
# FFN 前反馈网络
class FeedForward(nn.Module):
    """前馈网络: 512 → 2048 → 512"""

    def __init__(self, d_model, d_ff, dropout=0.1):
        super().__init__()
        self.fc1 = nn.Linear(d_model, d_ff)  # 512 → 2048
        self.fc2 = nn.Linear(d_ff, d_model)  # 2048 → 512
        self.dropout = nn.Dropout(dropout)
        self.activation = nn.GELU()  # 比 ReLU 更平滑

    def forward(self, x):
        """
        x: [B, S, d_model]
        返回: [B, S, d_model]  形状不变!
        """
        x = self.fc1(x)  # 扩展
        x = self.activation(x)  # 激活
        x = self.dropout(x)  # 防过拟合
        x = self.fc2(x)  # 缩回
        return x
# 验证
ffn = FeedForward(512, 2048)
x = torch.randn(2, 10, 512)
print(f"FFN 输入: {x.shape}")
print(f"FFN 输出: {ffn(x).shape}")  # [2, 10, 512] — 形状不变
```



## 1.7 残差连接和层归一化

残差连接：避免梯度消失，回传时，直接给到输出

```python
# 残差连接就一行代码:
output = x + sublayer(x)

# 完整写法 (含 Dropout):
output = x + dropout(sublayer(x))

# 直观理解:
# 子层学习的是"增量"(残差), 不是从零学起
# 即使子层什么都没学到(输出≈0), 结果还是 ≈ x, 不会变差
```

层归一化：归一化处理，针对每一层，大的误差变为小范围。保证训练稳定性

```python
# PyTorch 自带 LayerNorm
norm = nn.LayerNorm(512)   # d_model = 512

x = torch.randn(2, 10, 512)  # [B, S, D]
y = norm(x)                   # [B, S, D] — 形状不变, 值被归一化

# 验证: 归一化后均值≈0, 方差≈1
print(f"归一化后均值: {y.mean(dim=-1)[0,0].item():.6f}")  # ≈ 0
print(f"归一化后方差: {y.var(dim=-1)[0,0].item():.6f}")    # ≈ 1
```



## 1.8 编码器

编码器：定义一个模型列表，用于理解NLP

组成：

输入-->层归一化-->多头注意力-->残差连接---输出

输入-->层归一化-->FFN前馈网络-->残差连接--输出



重在理解，语义



```Python
class EncoderBlock(nn.Module):
    """一个 Encoder 层"""
    
    def __init__(self, d_model, n_heads, d_ff, dropout=0.1):
        super().__init__()
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.attn  = MultiHeadAttention(d_model, n_heads, dropout)
        self.ffn   = FeedForward(d_model, d_ff, dropout)
        self.drop1 = nn.Dropout(dropout)
        self.drop2 = nn.Dropout(dropout)

    def forward(self, x, src_mask=None):
        # 子层1: 自注意力 + 残差 + LN
        nx = self.norm1(x)
        attn_out, _ = self.attn(nx, nx, nx, mask=src_mask)
        x = x + self.drop1(attn_out)         # 残差连接

        # 子层2: FFN + 残差 + LN
        nx = self.norm2(x)
        ffn_out = self.ffn(nx)
        x = x + self.drop2(ffn_out)          # 残差连接

        return x
```
## 1.9 解码器

解码器：定义一个模型列表，用于生成内容

组成：

输入-->层归一化-->掩码自注意力--残差--输出

输入-->层归一化-->交叉自注意力--残差--输出

输入-->层归一化-->FFN前馈网络--残差--输出

```python
class DecoderBlock(nn.Module):
    """一个 Decoder 层 — 比 Encoder 多一个交叉注意力"""
    
    def __init__(self, d_model, n_heads, d_ff, dropout=0.1):
        super().__init__()
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.norm3 = nn.LayerNorm(d_model)
        self.self_attn  = MultiHeadAttention(d_model, n_heads, dropout)  # 自注意力
        self.cross_attn = MultiHeadAttention(d_model, n_heads, dropout)  # 交叉注意力
        self.ffn = FeedForward(d_model, d_ff, dropout)
        self.drop1 = nn.Dropout(dropout)
        self.drop2 = nn.Dropout(dropout)
        self.drop3 = nn.Dropout(dropout)
    
    def forward(self, x, enc_out, src_mask=None, tgt_mask=None):
        # 子层1: Masked 自注意力 (看自己, 但不能看未来)
        nx = self.norm1(x)
        sa_out, _ = self.self_attn(nx, nx, nx, mask=tgt_mask)
        x = x + self.drop1(sa_out)
        
        # 子层2: 交叉注意力 (看 Encoder 的输出)
        nx = self.norm2(x)
        ca_out, _ = self.cross_attn(nx, enc_out, enc_out, mask=src_mask)
        x = x + self.drop2(ca_out)
        
        # 子层3: FFN
        nx = self.norm3(x)
        x = x + self.drop3(self.ffn(nx))
        
        return x
```



# 2.总结

Tranformer的组成部分进行理解：

1.自注意力

​	计算过程

2.多头自注意力

​	计算过程

3.位置编码

​	词嵌入层

​	位置编码--正弦

4.前馈网络

​	2层全连接神经网络，先扩展4倍，再缩小4倍

5.残差连接和层归一化

​	残差连接 避免梯度消失

​	层归一化 Transformer深层神经网络，训练稳定性，归一化

6.编码器

​	理解内容

7.解码器

​	生成内容



# 3.作业

## 3.1 基础代码全部实现一遍

8个点，实现之后，再理解每一个作用和实现原理

## 3.2 思维导图

## 3.3 思考团队项目

## 3.4 查漏补缺

机器学习至少搞懂6种全发

深度学习需要搞懂：神经网络，CNN，RNN

Transformer的（8块内容）核心组成的实现过程





