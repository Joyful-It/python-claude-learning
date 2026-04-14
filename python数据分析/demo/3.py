#  创建一个2行3列的全1数组和一个2行3列的全0数组，
# 分别对两个数组进行矢量化运算（+5、*3），然后打印
# 运算结果
import numpy as np
a1=np.ones((2,3))
a2=np.zeros((2,3))
a11=a1+5
a22=a2*3
print(a11)
print(a22)