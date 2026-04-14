import numpy as np
scores = np.array([85, 92, 78, 96, 88])
print(np.argmax(scores))
print(np.argmin(scores))#这两个函数返回的是位置索引 最大值和最小值
print(scores>85) #返回的是布尔类型
print(np.where(scores>85))#  返回符合条件的数组