import matplotlib.pyplot as plt

# 1. 你的原始数据
epochs = [1, 2, 3, 4, 5]
train_loss = [0.4356, 0.2953, 0.2373, 0.1910, 0.1529]
val_loss   = [0.3402, 0.3154, 0.3329, 0.3017, 0.3225]
acc        = [0.8389, 0.8700, 0.8876, 0.8875, 0.8780]
f1_score   = [0.8796, 0.9055, 0.9218, 0.9197, 0.9116]

# 2. 设置画布
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# 左图：损失曲线
ax1.plot(epochs, train_loss, 'o-', color='#1f77b4', label='训练损失 Train Loss', linewidth=2)
ax1.plot(epochs, val_loss, 's-', color='#ff7f0e', label='验证损失 Val Loss', linewidth=2)
ax1.set_title('BiLSTM 损失变化曲线', fontsize=14)
ax1.set_xlabel('Epoch 训练轮次')
ax1.set_ylabel('Loss 损失值')
ax1.legend()
ax1.grid(alpha=0.3)

# 右图：准确率 & F1
ax2.plot(epochs, acc, 'o-', color='#2ca02c', label='准确率 Acc', linewidth=2)
ax2.plot(epochs, f1_score, '^-', color='#d62728', label='F1 分数', linewidth=2)
ax2.set_title('BiLSTM 分类指标变化曲线', fontsize=14)
ax2.set_xlabel('Epoch 训练轮次')
ax2.set_ylabel('指标数值')
ax2.legend()
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()