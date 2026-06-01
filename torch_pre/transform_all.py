# ① 导库——六件套
from transformers import(
    AutoTokenizer,                          # 自动加载分词器（文字→token ID）
    AutoModelForSequenceClassification,     # 自动加载分类模型
    Trainer,                                # 训练器，封装训练/评估流程
    TrainingArguments,                      # 训练超参数配置
    DataCollatorWithPadding                 # 动态填充，同批次对齐长度
)
from datasets import load_dataset          # 从 HuggingFace Hub 下载数据集
import evaluate                            # 加载评估指标（accuracy/f1等）
import numpy as np                         # 数组运算，argmax 用到

# ② 加载数据集
ds = load_dataset("stanfordnlp/imdb")      # 下载 IMDB 电影评论数据集
train_dataset = ds['train']                # 25000 条训练数据
test_dataset = ds['test']                  # 25000 条测试数据

# ③ 加载分词器 + 模型（必须同一个名字，词表要配套）
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=2                           # 二分类：正面/负面
)

# ④ 定义 token 化函数
def input_token(e):
    return tokenizer(
        e['text'],
        truncation=True,                   # 超过 max_length 就截断
        max_length=512,                    # BERT 最大支持 512 个 token
        padding=False                      # 不提前填，由 DataCollator 动态填
    )

# 对整个数据集应用 token 化，删掉原始文本列（省显存）
train_dataset = train_dataset.map(input_token, batched=True, remove_columns=["text"])
test_dataset = test_dataset.map(input_token, batched=True, remove_columns=["text"])

# ⑤ 配置训练参数
# DataCollator：把一批长短不一的序列填充到同一长度
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

training_args = TrainingArguments(
    output_dir="python/torch_pre/results", # 检查点保存路径
    num_train_epochs=3,                    # 训练 3 轮
    per_device_train_batch_size=16,        # 每个 GPU 每次吃 16 条
    per_device_eval_batch_size=16,         # 评估时每次 16 条
    eval_strategy="epoch",                 # 每轮结束后评估一次
    save_strategy="epoch",                 # 每轮结束后保存一次
    fp16=True,                             # 半精度训练，省一半显存（T4 必开）
    load_best_model_at_end=True,           # 训练结束后加载验证集最好的版本
)

# 加载评估指标（放函数外，只加载一次）
f1_metric = evaluate.load("f1")

# ⑥ 定义评估函数（Trainer 每次评估后自动调用）
def compute_metrics(eval_pred):
    # Trainer 自动传入 (模型原始输出, 真实标签) 元组
    logits, labels = eval_pred

    # logits 是每类的得分，取最大值下标作为预测类别
    # 例：[0.2, 0.8] → argmax → 1 → POSITIVE
    preds = np.argmax(logits, axis=-1)

    # 准确率：预测对的比例
    acc = (preds == labels).mean()

    # F1：.compute() 返回字典 {"f1": 0.85}，["f1"] 取出数值
    f1 = f1_metric.compute(
        predictions=preds,
        references=labels,
        average="binary"                   # 二分类专用
    )["f1"]

    return {"accuracy": acc, "f1": f1}


# ⑦ 组装 Trainer → 训练 → 保存
trainer = Trainer(
    model=model,                           # 要训练的模型
    args=training_args,                    # 训练参数
    train_dataset=train_dataset,           # 训练集
    eval_dataset=test_dataset,             # 验证集
    processing_class=tokenizer,            # 新版 API 替代 tokenizer=
    data_collator=data_collator,           # 动态填充
    compute_metrics=compute_metrics,       # 评估函数
)

trainer.train()                            # 开始训练

# 保存模型 + 分词器（必须一起保存，部署时缺一不可）
trainer.save_model("python/torch_pre/saved_model")
tokenizer.save_pretrained("python/torch_pre/saved_model")
