import numpy as np

a1=np.array([1,2,3,4,5],dtype=int)
a2=np.arange(5,10,2,dtype=int)
a3=np.zeros(5,dtype=float)
print(np.size(a2))
print(np.shape(a3))
print(a1.dtype)
print(a1)
print(a2)
print(a3)
# #  使用3种不同的方法（array、arange、zeros/ones）创建一维数组，
# 要求数组元素个数为5，元素类型为
# int64，最后打印每个数组的size、shape、dtype属性。
# （提示：dtype参数可指定数据类型）