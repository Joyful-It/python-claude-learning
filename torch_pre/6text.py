# ==================== 第1步：导入库 ====================
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import AdamW, get_linear_schedule_with_warmup
import torch
from torch.utils.data import DataLoader, Dataset
import pandas as pd

# ==================== 第2步：准备数据 ====================
# 假设你的数据长这样：
# text                label
# "这部电影很棒"        1      (1=正面, 0=负面)
# "太差了很失望"        0

texts = ["这部电影很棒", "太差了很失望", "一般般吧"]
labels = [1, 0, 1]  # 1=正面, 0=负面

# ==================== 第3步：Tokenize（分词+转ID）====================
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')

# 把文字变成数字
encoded = tokenizer(
    "这部电影很棒",
    padding='max_length',    # 补齐到固定长度
    max_length=128,           # 最大长度128
    truncation=True,          # 超出就截断
    return_tensors='pt'       # 返回PyTorch格式
)

print("原始文字:", "这部电影很棒")
print("分词结果:", tokenizer.convert_ids_to_tokens(encoded['input_ids']))
print("词ID:", encoded['input_ids'])

# ==================== 第4步：加载预训练模型 ====================
model = BertForSequenceClassification.from_pretrained(
    'bert-base-chinese',  # 中文预训练BERT
    num_labels=2           # 2分类：正面/负面
)

# ==================== 第5步：定义优化器 ====================
optimizer = AdamW(model.parameters(), lr=2e-5)  # 学习率

# ==================== 第6步：训练循环 ====================
model.train()  # 开启训练模式

for epoch in range(3):  # 训练3轮
    # 模拟一个batch
    inputs = tokenizer("这部电影很棒", return_tensors='pt')
    labels = torch.tensor([1])  # 标签：正面
    
    # Forward：算预测结果
    outputs = model(**inputs, labels=labels)
    loss = outputs.loss  # 损失
    
    # Backward：算梯度
    loss.backward()
    
    # 更新参数
    optimizer.step()
    optimizer.zero_grad()
    
    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

# ==================== 第7步：预测 ====================
model.eval()  # 关闭训练模式

with torch.no_grad():
    inputs = tokenizer("非常好，推荐", return_tensors='pt')
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=1)
    print(f"预测结果: {'正面' if predictions.item() == 1 else '负面'}")
