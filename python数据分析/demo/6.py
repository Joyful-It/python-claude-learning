#  现有一维数组arr = np.array([5,2,9,1,7,3,8])，
# 计算该数组的最大值、最小值、总和、平均值、标准差，并打
# # 印所有结果
import numpy as np
arr = np.array([5,2,9,1,7,3,8])
print(arr.dtype)
print(arr.itemsize)
print(arr.size)
print(arr.shape)
print(np.max(arr))#数组的最大值
print(np.min(arr))
print(np.average(arr))
print(np.median(arr))
print(np.std(arr))