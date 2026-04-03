import numpy as np

arry=np.array([12,34,32,12,34,56])
print(arry+10)

arry1=np.array([[12,34,567,86],[34,67,93,13]])
# print(arry+arry1)
arr1=arry.reshape(2,3)
print(np.max(arry))#数组的最大值
print(np.min(arry))
print(np.average(arr1))
print(np.median(arr1))
arry4=np.array([[13,12],[43,32]])
A_arry=np.linalg.inv(arry4)
print(A_arry)
print(np.std(arry))
arry5=np.array([43,21,56,54,32,45])
print(np.dot(arry,arry5))