import torch

print("--- 1. 创建 (Creation) ---")

# 1. torch.tensor(): 列表转张量
# 就像把 Python 的列表直接变成 PyTorch 能算的格式
data = [[1, 2], [3, 4]]
t1 = torch.tensor(data)
print(f"1. tensor() 列表转: \n{t1}\n形状: {t1.shape}\n")

# 2. torch.randn(): 正态随机
# 生成服从标准正态分布（均值0，方差1）的随机数，常用于初始化权重
# 这里生成一个 2行3列 的矩阵
t2 = torch.randn(2, 3)
print(f"2. randn() 正态随机 (2x3): \n{t2}\n形状: {t2.shape}\n")

# 3. torch.arange(): 等差数列
# 类似 python 的 range，生成 0 到 9
t3 = torch.arange(0, 10, step=1)
print(f"3. arange() 等差数列: \n{t3}\n形状: {t3.shape}\n")

print("--- 2. 变形 (Reshaping) ---")

# 基于 t3 (形状是 [10]) 进行变形操作

# 1. reshape(): 任意变形
# 把 10 个元素变成 2行5列 (必须保证元素总数不变)
t3_reshape = t3.reshape(2, 5)
print(f"1. reshape(2, 5): \n{t3_reshape}\n形状: {t3_reshape.shape}\n")

# 2. unsqueeze(): 加维度 (升维)
# dim=0 表示在最前面加一维，变成“行向量” (1, 10)
# dim=1 表示在最后面加一维，变成“列向量” (10, 1)
t3_col = t3.unsqueeze(1)
print(f"2. unsqueeze(1) 加维度: \n{t3_col}\n形状: {t3_col.shape}\n")

# 3. permute(): 换轴 (转置/维度的重新排列)
# 假设我们有一个模拟的“小图片”：2张图，3个通道，4x4像素 -> 形状 (2, 3, 4, 4)
img = torch.randn(2, 3, 4, 4)
# 想把通道放到最后 (变成 TensorFlow 格式或为了可视化): (2, 4, 4, 3)
# 0->0, 1->3, 2->1, 3->2
img_permuted = img.permute(0, 2, 3, 1)
print(f"3. permute() 换轴: \n原形状: {img.shape} -> 新形状: {img_permuted.shape}\n")

print("--- 3. 运算 (Operations) ---")

# 准备两个矩阵
m1 = torch.tensor([[1., 2.]])  # 形状 (1, 2)
m2 = torch.tensor([[3.], [4.]])  # 形状 (2, 1)

# 1. @ : 矩阵乘法
# (1, 2) @ (2, 1) = (1, 1)
mat_mul = m1 @ m2
print(f"1. @ 矩阵乘: \n{m1} @ \n{m2} = \n{mat_mul}\n")

# 2. .sum(dim=): 求和归约
t_sum = torch.tensor([[1., 2., 3.], [4., 5., 6.]]) # 形状 (2, 3)
# dim=1 表示“消灭第1维（列）”，即按行求和
sum_res = t_sum.sum(dim=1)
print(f"2. sum(dim=1) 按行求和: \n{t_sum} \n-> {sum_res} (形状变为: {sum_res.shape})\n")

# 3. .mean(dim=): 求平均值
# dim=0 表示“消灭第0维（行）”，即按列求平均
mean_res = t_sum.mean(dim=0)
print(f"3. mean(dim=0) 按列求平均: \n{t_sum} \n-> {mean_res} (形状变为: {mean_res.shape})")