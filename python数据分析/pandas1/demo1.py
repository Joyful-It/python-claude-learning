import numpy as np
import pandas as pd

a=pd.Series([1,2,3,4,5,6],dtype='Int16',index=['a','b','c','d','e','f'])
print(a.ndim)
print(a.dtype)
print(a.size)
print(a.shape)
print(a)
print(a["a"])
print(a.values)
print(a.index)
a['f']=100
print(a['f'])
b=pd.Series(np.random.default_rng().integers(30,90,5))
print("b:",b)#  np.random.default_rng() 随机生成 integrs整数