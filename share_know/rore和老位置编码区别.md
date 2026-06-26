这是 Transformer 演化里非常关键的一步。

你可以把它理解成：

**原始 Positional Encoding（PE） = 把位置信息加到词向量里**

而

**RoPE（Rotary Position Embedding） = 把位置信息加到 Attention 计算过程里**

这是本质区别。

------

# 1 原始 Transformer 的正弦余弦位置编码

论文《Attention Is All You Need》里的做法：

对于位置 (pos)

构造：

[
PE(pos,2i)=\sin(pos/10000^{2i/d})
]

[
PE(pos,2i+1)=\cos(pos/10000^{2i/d})
]

例如：

```text
位置0
[0.00,1.00,0.00,1.00...]

位置1
[0.84,0.54,0.01,0.99...]

位置2
[0.91,-0.41,0.02,0.99...]
```

然后直接加到词向量：

[
x = token + PE
]

------

例如：

```text
"猫"

token embedding

[0.2,0.5,-0.1...]

位置编码

[0.84,0.54,0.01...]

相加

[1.04,1.04,-0.09...]
```

------

这样模型知道：

```text
猫在第1个位置
```

而不是：

```text
猫这个词本身
```

------

# 2 这种方法的问题

假设：

```text
A B C
```

和

```text
B C D
```

------

Attention真正关心的是：

```text
A离B多远
B离C多远
```

即：

### 相对位置

而不是：

```text
A在第5个位置
B在第6个位置
```

即：

### 绝对位置

------

原始PE告诉模型：

```text
A在5
B在6
```

模型需要自己学习：

```text
哦
5和6差1
```

比较绕。

------

# 3 RoPE怎么做

RoPE不加到Embedding上。

而是作用在：

[
Q,K
]

上。

------

普通Attention：

[
Attention=QK^T
]

RoPE：

[
Attention=(R_mQ)(R_nK)^T
]

其中：

[
R_m
]

表示位置m对应的旋转矩阵。

------

# 4 什么叫旋转

假设Q的一部分：

[
[1,0]
]

位置0：

```text
→
```

------

位置1：

旋转1个角度

```text
↗
```

------

位置2：

再转一点

```text
↑
```

------

位置3：

```text
↖
```

------

就像钟表指针一样。

------

数学上：

# [ \begin{bmatrix} x'\ y' \end{bmatrix}

\begin{bmatrix}
\cos\theta & -\sin\theta\
\sin\theta & \cos\theta
\end{bmatrix}
\begin{bmatrix}
x\
y
\end{bmatrix}
]

------

# 5 为什么这样就有相对位置

这是RoPE最厉害的地方。

计算Attention：

[
(R_mQ)^T(R_nK)
]

展开后会变成：

[
Q^TR_{m-n}K
]

注意：

位置 m 和 n 不见了。

只剩：

[
m-n
]

------

例如：

```text
位置10 和 11
```

得到：

```text
11-10=1
```

------

位置100 和 101

得到：

```text
101-100=1
```

------

结果一致。

模型天然感知：

```text
距离1
```

而不是：

```text
绝对位置是多少
```

------

# 6 长文本为什么更强

原始PE：

训练：

```text
长度2048
```

推理：

```text
长度8192
```

模型没见过。

效果容易崩。

------

RoPE：

位置只是旋转角度。

理论上：

```text
2048
4096
8192
16384
```

都能继续旋转。

因此：

### 外推能力（Extrapolation）更强

这也是 Llama、Qwen、DeepSeek、Gemma 等模型都采用 RoPE 的原因。

------

# 7 从工程角度看演化

Transformer(2017)

```text
Token Embedding
+
Sin/Cos Absolute PE
```

↓

Transformer-XL

```text
Relative Position
```

↓

T5

```text
Relative Bias
```

↓

GPT-NeoX
LLaMA
Qwen
DeepSeek

```text
RoPE
```

↓

Qwen3
Llama4
DeepSeek-V3

```text
RoPE + 长上下文扩展(YARN/NTK等)
```

------

一句话总结：

**正弦余弦位置编码是“把位置向量加到输入里，让模型自己学习位置关系”；RoPE是“直接把位置编码进 Q/K 的几何关系里，让 Attention 天然感知相对距离”。**

因此 RoPE 同时具备：

- 相对位置感知
- 参数量为0
- 长文本外推能力强
- 与 Transformer 完全兼容

所以已经基本取代了最早的绝对位置编码。你的观察非常敏锐。

实际上：

> **最原始 Transformer 的 Sin/Cos 位置编码，和 GPT-2 的位置编码，最终都是加到 Token Embedding 上的。**

区别不在于「怎么加」，而在于「位置向量是怎么得到的」。

------

## 1 GPT-2 怎么做

GPT-2 不用 Sin/Cos。

它直接学习一个位置表：

```python
position_embedding = nn.Embedding(max_len, hidden_size)
```

比如：

```text
位置0
[0.12, 0.87, ...]

位置1
[-0.33, 0.44, ...]

位置2
[0.91, -0.15, ...]
```

这些数值是训练出来的。

然后：

[
x = token_embedding + position_embedding
]

和你举的例子完全一样。

------

## 2 Transformer 原版怎么做

Transformer 不学习位置表。

直接用公式算：

[
PE(pos,2i)=\sin\left(\frac{pos}{10000^{2i/d}}\right)
]

[
PE(pos,2i+1)=\cos\left(\frac{pos}{10000^{2i/d}}\right)
]

得到一个固定向量。

例如：

```text
位置5

[sin(...),
 cos(...),
 sin(...),
 cos(...)]
```

然后一样：

[
x = token + PE
]

所以：

```text
Transformer
Token + SinCos

GPT2
Token + Learned Position
```

结构上几乎一样。

------

# 3 那为什么要 sin 和 cos

这里才是重点。

很多人第一次看公式都会问：

> 为什么不用随机数？
>
> 为什么不用编号 1、2、3、4？
>
> 为什么非得是 sin/cos？

因为它想让模型能够推导出位置关系。

------

假设隐藏维度 d=4

位置0：

[
[\sin(0),\cos(0),\sin(0),\cos(0)]
]

=

```text
[0,1,0,1]
```

------

位置1：

[
[\sin(1),\cos(1),\sin(0.01),\cos(0.01)]
]

≈

```text
[0.84,0.54,0.01,0.99995]
```

------

位置2：

```text
[0.91,-0.41,0.02,0.9998]
```

------

你会发现：

第一对变化很快：

```text
sin(0)
sin(1)
sin(2)
```

------

第二对变化很慢：

```text
sin(0)
sin(0.01)
sin(0.02)
```

------

因此：

```text
低维度 = 短距离信息

高维度 = 长距离信息
```

------

# 4 为什么必须同时有 sin 和 cos

这是最关键的数学性质。

有一个三角函数公式：

# [ \sin(a+b)

\sin a \cos b
+
\cos a \sin b
]

以及

# [ \cos(a+b)

## \cos a \cos b

\sin a \sin b
]

------

假设知道：

```text
位置10
```

的

```text
sin(10)
cos(10)
```

那么通过线性变换就能得到：

```text
位置11
```

的

```text
sin(11)
cos(11)
```

------

论文利用的就是这个性质：

### 相邻位置之间存在线性关系

模型容易学习：

```text
当前位置
↓
下一个位置
```

这种规律。

------

# 5 GPT2 的学习位置为什么后来不流行了

因为它有一个致命问题。

假设训练：

```text
最大长度1024
```

位置表：

```text
0~1023
```

都有参数。

------

推理：

```text
长度2048
```

突然出现：

```text
位置1024
```

没有Embedding。

直接废了。

------

所以 GPT2：

```text
长度1024
=> 只能1024
```

------

而 Sin/Cos：

位置10000：

[
\sin(10000)
]

照样能算。

------

位置50000：

[
\sin(50000)
]

也能算。

------

因此：

### 理论上无限长

这就是它最大的优势。

------

# 6 RoPE其实和Sin/Cos是一家人

很多人以为：

```text
SinCos PE
```

和

```text
RoPE
```

是两种完全不同的东西。

其实不是。

RoPE本质上还是：

[
\sin
]

和

[
\cos
]

------

只是不用来构造：

```text
PE向量
```

然后加到Embedding。

而是构造：

```text
旋转角度
```

去旋转Q和K。

------

所以可以理解成：

```text
Transformer PE
↓
Sin/Cos 加到输入

GPT2 PE
↓
学习的位置向量加到输入

RoPE
↓
Sin/Cos 直接参与Attention
```

本质上，RoPE其实是把原始 Sin/Cos 位置编码的思想发挥到了更适合 Attention 的形式，而不是彻底抛弃了 Sin/Cos。