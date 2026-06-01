# 学习会话记录 - 2026-05-30

## 今日内容

> C盘清理环境整治 + Python 虚拟环境概念 + IMDB 项目骨架六步实操

---

## 今日理解跃迁

> 从"tokenizer 和 model 是一起的" → "tokenizer 下词表(200KB)、model 下权重(400MB)，同名但不同物，必须配对使用"

---

## 一、Python 环境整理

### 环境清单

| Python | 路径 | 处理 |
|------|------|------|
| Conda base | `D:\program\miniconda\python.exe` | ✅ 保留，统一使用 |
| Python 3.13 | `C:\...\Python313\python.exe` | ❌ 已删除 (~2G) |
| mychatbot_env | `C:\Users\Lenovo\mychatbot_env` | ❌ 已删除 |
| Microsoft Store 壳 | `C:\...\WindowsApps\python.exe` | 忽略 |

### C 盘清理总结

| 操作 | 释放空间 |
|------|------|
| 删除 Python313 | 2G |
| 删除 mychatbot_env | 14M |
| Android 软链接到 D 盘 | 9.7G |
| .gradle 软链接到 D 盘 | 6.2G |
| pip cache purge | 1.6G |
| Windows 磁盘清理(Temp) | ~4G |
| 微信/网易 数据路径改 D 盘 | ~7G |

### 软链接命令（管理员 CMD）

```cmd
mklink /J "C:\原路径" "D:\目标路径"
```

### Conda 虚拟环境概念

```bash
conda create -n myenv python=3.12  # 创建
conda activate myenv               # 激活
conda env list                      # 查看所有环境
```

每个环境独立，Python 基础文件 ~几十MB，真正占空间的是 pip install 的库。库散装是好事——不同项目的版本冲突隔离开。目前只用 base 环境即可。

---

## 二、IMDB 情感分析项目——骨架六步

### 完整代码

```python
from transformers import(
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
    DataCollatorWithPadding
)
from datasets import load_dataset
import evaluate
import numpy as np

# ① 加载数据集
ds = load_dataset("imdb")
train_dataset = ds['train']
test_dataset = ds['test']

# ② 加载模型 + 分词器
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

# ③ 定义 token 化函数
def input_token(e):
    return tokenizer(
        e['text'],
        truncation=True,
        max_length=512,
        padding=False  # 不提前填，由 DataCollator 动态填充
    )

# ④ 应用 token 化
train_dataset = train_dataset.map(input_token, batched=True, remove_columns=["text"])
test_dataset = test_dataset.map(input_token, batched=True, remove_columns=["text"])

# ⑤ DataCollator + TrainingArguments
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_eval_batch_size=16,
    per_device_train_batch_size=16,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
)

# ⑥ 评估指标函数
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    acc = (preds == labels).mean()
    return {"accuracy": acc}

# ⑦ 组装 Trainer → 训练 → 保存
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)
trainer.train()
trainer.save_model("./saved_model")
```

### 骨架六步口诀

```
① 导库        → 全家桶六件套
② 加载数据    → load_dataset("imdb")
③ 加载模型+分词器 → from_pretrained("bert-base-uncased")
④ 数据 token 化 → dataset.map(tokenize_fn, batched=True)
⑤ 配置参数    → DataCollatorWithPadding + TrainingArguments
⑥ 组装训练    → Trainer(...) → train() → save_model()
```

### 关键理解

| 概念 | 一句话 |
|------|------|
| tokenizer vs model | 同名但下不同文件：词表(200KB) vs 权重(400MB)，必须配对 |
| `remove_columns=["text"]` | token 化后删原始文本，省显存 |
| `attention_mask` | 告诉模型哪些是真词(1)，哪些是填充的假词(0) |
| `DataCollatorWithPadding` | 动态填充——不到 512 的只填到该 batch 最长，省显存 |
| `batched=True` | 一次送一批，并行处理快 |
| `dataset.map()` | 对数据集中每条数据执行同一操作 |

### dataset.map() 为什么要用函数

`map()` 必须接收一个"可调用对象"——你把规则写好（函数），map 替你去循环每条数据。类比：流水线工人每来一个瓶子就拧盖子，你给的是"拧盖子"的动作，不是自己去拧每一个。

### lambda vs 普通函数

```python
# lambda：一行能写完，用完就扔
sorted(students, key=lambda s: s['score'])
list(filter(lambda x: x > 10, nums))
list(map(lambda w: w.upper(), words))

# def：多行/复杂逻辑/需要复用
def input_token(e):
    return tokenizer(e['text'], truncation=True, max_length=512, padding=False)
```

---

## 关键理解纠正

| 混淆 | 纠正 |
|------|------|
| `per_device_train_batch_size=16` 是 16 轮？ | ❌ 是每 GPU 一口吃 16 条，32 GPU→32×16=512 条同时 |
| `load_best_model_at_end=True` 是提前停？ | ❌ 是跑完后自动加载验证集最好的版本，不是 Early Stopping |
| tokenizer 和 model 是一体？ | ❌ 两个独立对象，同一个模型名下不同文件 |
