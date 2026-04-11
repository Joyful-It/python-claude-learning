# 学习会话记录 - 2026-04-10

## 会话概览
- **日期**: 2026-04-10
- **时长**: 约3小时
- **形式**: 线上学习（Claude Code）
- **核心主题**: PyTorch nn.Linear / BERT vs Transformer / HuggingFace / transformers安装

## 学员提出的问题

### 关于PyTorch
1. "layer中weight什么意思" - 理解了weight是5×3矩阵
2. "4个样本什么意思" - 理解了batch概念
3. "linear扮演什么角色" - 理解了是计算器，包含W和b
4. "loss固定的吗" - 理解了不同任务用不同Loss
5. "怎么变的，为什么变" - 理解了训练过程

### 关于BERT/Transformer
1. "QKV是什么意思" - 理解了Query/Key/Value
2. "bert和transformer什么关系" - 理解了Encoder/Decoder
3. "bert只会预测，gpt只能生成" - ✅ 核心区别理解
4. "mlm什么意思" - 理解了Masked Language Model = 完形填空
5. "nsp下一句预测" - 理解了Next Sentence Prediction

### 关于HuggingFace
1. "hf这个公司和模型" - 了解了HF故事
2. "transformers怎么安装" - pip install transformers
3. "bert和transformer代码怎么体现" - 看了BERT Encoder代码

## 讲解的概念

### PyTorch
- nn.Linear(3,5) = 输入3个输出5个
- weight形状 = (5,3)，bias形状 = (5,)
- batch_size = 一次喂多少样本
- Loss函数 = 固定公式，CrossEntropyLoss用于分类

### BERT vs GPT
- BERT = Encoder = 双向 = 理解
- GPT = Decoder = 单向 = 生成
- MLM = 完形填空 = 盖住词猜
- NSP = 下一句预测 = 判断句子关系

### Transformer
- Multi-Head Attention = 多个Attention并行
- Encoder = 看完整个句子
- Decoder = 从左到右生成

### HuggingFace
- transformers库 = 预训练模型库
- BERT/RoBERTa/Qwen/LLaMA 都是预训练模型

## 优先复习清单
1. round() 保留2位小数
2. 三目运算
3. f-string 格式化输出
4. type() 输出数据类型

## 掌握的考点

### PyTorch
- Tensor/梯度/nn.Linear ✅
- backward() 和 x.grad ✅
- batch概念 ✅

### BERT/GPT
- Encoder vs Decoder ✅
- MLM vs NSP ✅
- BERT理解/GPT生成 ✅

### Transformer
- Multi-Head Attention ✅
- QKV概念 ✅

## 学员状态
- 对深度学习兴趣浓厚
- 正在准备BERT情感分析作业
- 有10天期限

## 学习效果评估
- PyTorch基础: 55%
- BERT/GPT理解: 70%
- Transformer: 50%
- transformers库: 刚接触

## 下次继续
- transformers 实战
- Fine-tune BERT 情感分析
- 复习：round/三目/f-string
