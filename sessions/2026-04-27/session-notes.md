# 学习会话记录 - 2026-04-27

## 会话概览
- 日期：2026-04-27
- 形式：一对一教学
- 核心主题：Attention Is All You Need 论文概念理解 + DeepSeek API 调用

## 学员提出的问题/需求
1. 复习 Attention Is All You Need 论文中的词语理解
2. 学习 DeepSeek API 调用

## 讲解的概念与教学过程

### 1. 归一化（Normalization）
学员理解：
- 不是把数据变成同一个值
- 将数据调整为均值≈0、方差≈1的标准分布
- 保留数据原本的大小关系
- 统一数据尺度
- 让模型训练更稳定、更快
- 防止梯度消失/爆炸

### 2. 词向量维度（d_model=512）
- 1个词语对应1个512维向量
- 用512个数字描述词义
- 不是512个向量

### 3. Layer Norm vs Batch Norm

**Layer Norm（Transformer 专用）：**
- 只对单个词自己的512维向量做归一化
- 不依赖批次大小和句子长度
- 不破坏词语的语义特殊性
- 不会让不同词语归一化后变成相同向量

**Batch Norm：**
- 对整个批次里所有词的同一个维度（通道）统一归一化
- 强依赖批次大小
- 不适合 NLP 变长序列任务

### 4. DeepSeek API 调用

#### 安装 openai 库
```bash
pip install openai
```

#### 基本调用代码
```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-a18b770419fb4bed87d887c2013ef32e",
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "hello"}]
)

print(response.choices[0].message.content)
```

#### 参数讲解
| 参数 | 意思 |
|-----|------|
| `temperature` | 控制输出随机程度（0.0~1.0） |
| `max_tokens` | 最大回答字数 |
| `stream` | 是否用流式输出（边回答边显示） |

#### 流式输出写法
```python
stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "hello"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

#### 错误排查
- `402 Insufficient Balance` = 账户余额不足
- `stream=True` 时不能用 `.choices[0].message.content`，要用 `delta.content`
- URL 必须是 `https://api.deepseek.com`，不是 `http`

## 识别的知识漏洞
- DeepSeek API 调用已初步掌握
- Attention 机制理解了 Layer Norm 和 Batch Norm 的区别

## 已掌握的考点
- DeepSeek API 调用 ✅
- temperature、max_tokens 参数 ✅
- 流式输出 vs 非流式输出 ✅

## 明日计划
1. 继续学习 Attention 机制
2. 继续 DeepSeek API 练习
3. 回顾 Matplotlib/Seaborn（还未学习）

## 学习效果评估
- 对 Layer Norm 和 Batch Norm 的理解：正确
- DeepSeek API 调用：成功运行

---

## 下次继续
```
继续学习，请读取：
1. progress/python-tracker.md
2. sessions/2026-04-27/session-notes.md

上次学完发现：
- DeepSeek API 调用成功 ✅
- Attention 论文概念初步理解
- SQLAlchemy 还没学
- Matplotlib/Seaborn 还没学
```