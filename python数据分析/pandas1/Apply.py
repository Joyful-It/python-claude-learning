import numpy as np
import pandas as pd

data = pd.DataFrame({
    'name': ['张三', '李四', '王五'],
    'age': [25, 30, 150]  # 150是异常值
})
print("原始数据：")
print(data)
mean_age=data['age'].mean()


data['age']=data['age'].apply(lambda x :x if 0<x<100 else mean_age)
print(data)