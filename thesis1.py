import matplotlib.pyplot as plt
import os

# ---------------------- 1. 修复：Windows中文显示问题 ----------------------
# 方案1：用Windows自带中文字体（黑体），无需额外安装
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows默认黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

# ---------------------- 2. 你的BiLSTM完整数据 ----------------------
epochs = [1, 2, 3, 4, 5]
train_loss = [0.4356, 0.2953, 0.2373, 0.1910, 0.1529]
val_loss   = [0.3402, 0.3154, 0.3329, 0.3017, 0.3225]
acc        = [0.8389, 0.8700, 0.8876, 0.8875, 0.8780]
precision  = [0.9477, 0.9447, 0.9198, 0.9412, 0.9488]
recall     = [0.8206, 0.8695, 0.9238, 0.8992, 0.8771]
f1         = [0.8796, 0.9055, 0.9218, 0.9197, 0.9116]

# ---------------------- 3. 修复：Windows本地保存路径 ----------------------
# 方案1：保存到当前脚本所在文件夹（推荐，易找到）
save_path = "./"  # ./ 代表当前目录
# 方案2：指定具体路径（比如桌面），示例：save_path = "C:/Users/Lenovo/Desktop/"

# 确保路径存在（防止手动建文件夹）
os.makedirs(save_path, exist_ok=True)

# ====================== 图1：损失曲线 ======================
plt.figure(figsize=(10, 6))
plt.plot(epochs, train_loss, 'o-', color='#1f77b4', linewidth=2, label='训练损失 Train Loss')
plt.plot(epochs, val_loss, 's-', color='#ff7f0e', linewidth=2, label='验证损失 Val Loss')
plt.title('BiLSTM 训练与验证损失变化', fontsize=15)
plt.xlabel('训练轮次 Epoch', fontsize=12)
plt.ylabel('损失值 Loss', fontsize=12)
plt.legend(fontsize=11)
plt.grid(alpha=0.3)
plt.tight_layout()
# 保存到本地路径
plt.savefig(os.path.join(save_path, "BiLSTM_Loss.png"), dpi=300)
plt.show()

# ====================== 图2：评价指标曲线 ======================
plt.figure(figsize=(10, 6))
plt.plot(epochs, acc, 'o-', linewidth=2, label='准确率 Accuracy')
plt.plot(epochs, precision, '^-', linewidth=2, label='精确率 Precision')
plt.plot(epochs, recall, 's-', linewidth=2, label='召回率 Recall')
plt.plot(epochs, f1, 'd-', linewidth=2, label='F1分数')
plt.title('BiLSTM 各评价指标变化', fontsize=15)
plt.xlabel('训练轮次 Epoch', fontsize=12)
plt.ylabel('指标数值', fontsize=12)
plt.legend(fontsize=11)
plt.grid(alpha=0.3)
plt.tight_layout()
# 保存到本地路径
plt.savefig(os.path.join(save_path, "BiLSTM_Metrics.png"), dpi=300)
plt.show()