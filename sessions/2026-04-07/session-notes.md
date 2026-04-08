# 学习会话记录 - 2026-04-07

## 会话概览
- **日期**: 2026-04-07
- **时长**: 约4小时
- **形式**: 线上学习（Claude Code）
- **核心主题**: Transformer/BERT/GPT / PyTorch基础 / 情感分析作业规划

## 学员提出的问题

### 关于Transformer/BERT/GPT
1. "bert只是理解语义然后判断是吧" - 理解了BERT的核心功能
2. "为什么BERT提升有限，为什么GPT越大越强" - 理解了训练目标不同导致的效果差异
3. "GPT不是理解语义，为什么用它" - 理解了GPT也能理解语义，只是选择生成赛道

### 关于PyTorch
1. "ndim后面为啥不跟括号" - 理解了属性vs方法的区别
2. "flatten()报错了" - 理解了DataFrame没有flatten，需要转NumPy
3. "ndim后面有时候跟括号有时候不跟" - 理解了属性(无括号)vs方法(有括号)
4. "我怎么知道是方法还是属性" - 学会了用type()判断
5. "backward只是求导是吗" - 理解了backward()和x.grad的关系
6. "y = x @ W^T + b 这个没看懂" - 矩阵乘法维度规则，待明天继续

### 关于情感分析作业
1. "这个作业符合我早上给你发的作业要求吗" - 分析了同学论文
2. "这个选题先不急" - 想先复习
3. "BERT/Transformer/Embedding我要学习这些东西" - 新作业：用这三个模型做情感预测
4. "十天后截止，学校没有GPU，可以调用云账号" - 明确了作业deadline和资源

## 讲解的概念与教学方法

### Transformer/BERT/GPT
- Self-Attention机制：Q/K/V向量，每个词关注其他所有词
- BERT用Encoder（看完句子理解+判断）
- GPT用Decoder（单向生成）
- 为什么GPT越大越强：训练目标（预测下一个词）让模型学到更多
- BERT瓶颈：完形填空目标限制提升

### PyTorch基础
- Tensor = 多维数组，和NumPy类似但支持GPU
- requires_grad=True 追踪计算
- Forward = 算输出
- backward() = 自动求导
- x.grad = 梯度结果
- nn.Linear(3,5) = 输入3个输出5个
- 矩阵乘法维度规则

### pandas基础
- 属性 vs 方法：属性不加括号，方法加括号
- DataFrame没有flatten，需要转np.array

### NumPy搜索函数
- argmax = 最大值的索引
- argmin = 最小值的索引
- where = 满足条件的索引

## 学员的回答/理解

### 掌握良好的
- ✅ BERT vs GPT核心区别（Encoder vs Decoder）
- ✅ 属性vs方法的区别
- ✅ argmax/argmin/where
- ✅ requires_grad vs 普通tensor
- ✅ backward() vs x.grad
- ✅ 损失函数概念（CrossEntropy）

### 待明天继续
- ⚠️ 矩阵乘法维度规则 (batch, in_features) @ (out, in)^T = (batch, out)
- ⚠️ nn.Linear的weight含义
- ⚠️ 为什么4个样本/什么是batch_size

## 识别的知识漏洞

| 漏洞 | 严重程度 | 状态 |
|-----|---------|------|
| 矩阵乘法维度规则 | 中 | 待明天补充 |
| nn.Linear权重形状 | 中 | 待明天补充 |
| batch_size概念 | 低 | 待明天补充 |
| 多态概念 | 低 | 未开始复习 |

## 掌握的考点

### PyTorch
- Tensor创建：torch.tensor, torch.zeros, torch.randn
- requires_grad追踪计算
- backward()自动求导
- x.grad读取梯度
- nn.Linear基本概念

### NumPy
- argmax/argmin/where搜索函数
- 属性vs方法区分

### Transformer
- Self-Attention基本原理
- Q/K/V概念
- BERT用Encoder，GPT用Decoder
- 为什么GPT越大越强

## 完成的任务

- [x] 分析同学发来的Deep Learning作业
- [x] pandas iloc和属性vs方法
- [x] NumPy argmax/argmin/where复习
- [x] Transformer深入：Self-Attention
- [x] BERT vs GPT深入理解
- [x] PyTorch基础：Tensor/梯度/nn.Linear
- [x] 规划新作业学习路径（10天计划）
- [x] 复习清单标记：round/三目/f-string/type

## 体现的核心理解

- 能用自己的话解释BERT和GPT的区别
- 能解释为什么GPT架构成为主流
- 能区分属性和方法
- 能解释反向传播和梯度求导的关系

## 需跟进的知识点

1. 矩阵乘法维度规则
2. nn.Linear权重形状
3. batch_size/batch概念
4. 多态巩固练习
5. json文件操作
6. while/for循环

## 学习效果评估

- Transformer基础：55%（理解Self-Attention原理，但QKV计算待深入）
- PyTorch基础：45%（基本概念清晰，矩阵乘法待巩固）
- NumPy：60%（搜索函数掌握）
- BERT/GPT理解：65%（核心区别理解清楚）
- 整体：对深度学习兴趣浓厚，10天计划可行

## 明日计划

1. 继续PyTorch：nn.Sequential构建网络
2. 补充矩阵乘法维度规则
3. 复习：round/三目/f-string/type（刚标记的优先项）
4. 继续Transformer：Multi-Head Attention（可选）
