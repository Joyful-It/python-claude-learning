import numpy as np
a1=np.arange(1,13,1)
a2=a1.reshape(3,4)
print(a2.ndim)
print(a2.shape)
print(a2)
# #创建一个3行4列的二维数组，元素为1-12的连续整数（使用arange+reshape），
# 打印该数组的ndim、
# shape，并获取数组中第2行第3列的元素（索引从0开始）。
