# 学习会话记录 - 2026-05-24

## 今日理解跃迁

> 从"所有 import 都要写" → "深度学习只有 torch/torch.nn/Dataset+DataLoader 三件套是必写的，其余全是按需加载——核心不变，外围可替换"

> 从"torch.nn 里什么模型都有" → "nn 只给你砖和水泥（Linear/Conv/LSTM），摩天大楼（BERT/GPT/YOLO）要去找各自的开发商（HuggingFace/ultralytics）"

---

## 第一节：深度学习 import 三分类——必需 vs 按需

### ⚡ 一定需要的（核心三件套，任何 PyTorch 项目少不了一个）

```python
import torch                           # PyTorch 本体
import torch.nn as nn                  # 层/激活/损失 都在里面
from torch.utils.data import Dataset, DataLoader  # 数据加载必经之路
```

### 📦 看数据格式选的

| import | 什么时候要 | 什么时候不要 |
|--------|----------|-------------|
| `numpy as np` | 数据是 CSV/表格 | 数据已经是 tensor |
| `pandas as pd` | 读 CSV/Excel | 读图像(用 PIL/OpenCV) |

### 🛠️ sklearn 的——辅助工具，可自己写

```python
from sklearn.model_selection import train_test_split  # 手写切分可替代
from sklearn.preprocessing import StandardScaler      # 手写标准化可替代
```

手写替代：
```python
mean, std = X.mean(dim=0), X.std(dim=0)
X = (X - mean) / std
```

---

## 第二节：所有深度学习项目 = 不变核心 + 可变外圈

```
═══════════════════════════════════════════
  不变核心（所有 DL 项目一样，背！）
═══════════════════════════════════════════
  import torch
  import torch.nn as nn
  from torch.utils.data import Dataset, DataLoader
  class XxxDataset(Dataset): ...
  class XxxModel(nn.Module): ...
  DataLoader → 训练循环五步
═══════════════════════════════════════════

═══════════════════════════════════════════
  可变外圈（不同项目换不同的）
═══════════════════════════════════════════
  数据读取：CSV(pandas) / 图像(PIL/OpenCV) / 文本(json)
  预处理：  StandardScaler / 图像增强 / Tokenizer
  模型架构：Linear(表格) / CNN(图像) / LSTM(序列) / Transformer(NLP)
  损失函数：分类→BCE/CrossEntropy / 回归→MSE
  优化器：  Adam / SGD / AdamW
═══════════════════════════════════════════
```

> 五块模板里真正换的只有前三块（数据读取/模型/损失），后两块（优化器/训练循环）基本不动。

---

## 第三节：torch.nn 有什么、没有什么

### torch.nn 里有（基础积木——自己盖房子）

```
层：
  nn.Linear          全连接（表格数据）
  nn.Conv2d          二维卷积（图像）
  nn.LSTM / nn.GRU   循环层（序列）
  nn.TransformerEncoderLayer  Transformer 单层
  nn.MultiheadAttention       多头注意力

辅助：
  ReLU / Sigmoid / Tanh      激活函数
  Dropout / BatchNorm         正则化
  BCEWithLogitsLoss / CrossEntropyLoss / MSELoss  损失函数
```

### torch.nn 里**没有**（完整模型——要去找开发商）

| 模型 | 在哪拿 | 安装 |
|------|-------|------|
| ResNet / VGG / MobileNet | `torchvision.models` | `pip install torchvision` |
| BERT / GPT / T5 / LLaMA | `transformers` (HuggingFace) | `pip install transformers` |
| YOLO | `ultralytics` | `pip install ultralytics` |
| CLIP | `open_clip` 或 `transformers` | 同上 |

### 一句话类比

```
nn.Linear / nn.Conv2d = 砖和水泥 → 你可以盖任何房子
BERT / GPT / YOLO     = 摩天大楼 → 直接找开发商拿成品户型图

你能用 nn.Linear 手写三层网络，但 GPT 的上百层+预训练权重不可能从零写
→ HuggingFace 提供"拎包入住"
```

---

## 第四节：Titanic 代码速查——十步清单

| 步 | 做什么 | 关键代码 | 核心坑 |
|----|-------|---------|--------|
| ① | 读数据 | `pd.read_csv()` | — |
| ② | 特征工程 | fillna / map / get_dummies | 衍生特征有意义才加 |
| ③ | 挑 X, y | `X = df[cols].copy()` | 必须 .copy() |
| ④ | 切分 | `train_test_split(stratify=y)` | stratify 保留比例 |
| ⑤ | 标准化 | `fit_transform(train) / transform(val)` | 绝不能反！ |
| ⑥ | 转 tensor | `.astype(np.float32)` + `.view(-1,1)` | object→float32 |
| ⑦ | Dataset+DataLoader | 厨师+服务员 | Capital D |
| ⑧ | 模型 | `nn.Sequential(Linear→ReLU→Linear→1)` | 最后无 sigmoid |
| ⑨ | 配置 | BCEWithLogitsLoss + Adam + epochs | — |
| ⑩ | 训练循环 | forward→loss→zero_grad→backward→step | 顺序固定 |

---

## 第五节：错题本

| 问 | 模糊点 | 正确 |
|---|-------|------|
| DataLoader 大小写？ | 写成 dataloader | **DataLoader**，Python 区分大小写 |
| 所有模型都在 torch.nn？ | 以为都在 | nn 只有基础积木，完整模型在 torchvision/transformers/ultralytics |
| 深度学习 import 哪些必须？ | 每行都要 | 只有 torch/nn/Dataset+DataLoader 三件套必写 |

---

## 更新学习效果评估

- **import 三分类**：三件套必写 / 数据处理按需 / sklearn 可替代 ✓
- **不变 vs 可变**：能说出核心不变 5 块 + 外围可变 5 块 ✓
- **torch.nn 边界**：基础积木在 nn / 完整模型在外部库 ✓
- **泰坦尼克号十步清单**：能背出顺序和每步关键坑 ✓
- **DataLoader 命名**：已纠正大小写 ✓
