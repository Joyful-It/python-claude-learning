import numpy as np
import pandas as pd

data = pd.DataFrame({
    'name':['张三','lisi','wangwu','zhaoliu'],
    'score':[95,88,95,92]
})
print("----------original----------")
print(data)
print("------Need--min--Rank--------")
data['rank']=data['score'].rank(method='min',ascending=False)
print(data)
print('-----Need-----max------Rank------')
data['rank']=data['score'].rank(method='max',ascending=True)
#因为 rank() 是对一列数据操作的，返回的自然是一列
print(data)
print('------Need----average-----rank-----')
data['rank2']=data['score'].rank(method='average',ascending=False)
print(data)