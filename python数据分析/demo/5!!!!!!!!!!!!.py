
# 5. 使用random模块创建一个3行3列的随机数组（元素范围0-1），
# 再创建一个3行3列的随机整数数组（元素范

import numpy as np

arr=np.random.randn(3,3)
arr1=np.random.randint(10,20,size=(3,3))
print(arr+arr1)