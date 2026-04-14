# . 现有数组arr = np.array([[1,2,3],[4,5,6],[7,8,9]])，
# 使用flatten()将其转换为一维数组，使用transpose()对原数
# 组进行转置，分别打印转换后的两个数组。
import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr1 = arr.flatten()
print(arr1)
arr2=np.transpose(arr)#转置
print(arr2)
