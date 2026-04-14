import numpy as np

arr=np.array([[12,34,55],[23,45,12]],dtype=np.int8)
print("weidu",arr.ndim)
print(np.__version__)
print(arr.dtype)
print(arr.itemsize)
print(arr.size)
print(arr.shape)
arr1=np.zeros(6)
print("all o",arr1)
print("change",arr1.reshape(2,3))
arr2=np.arange(0,20,2)
print("deng cha",arr2)
print(arr[0][2])#获取数据，用索引
