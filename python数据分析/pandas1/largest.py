import pandas as pd

data=pd.DataFrame({'name':['zhangsan','lisi','王五', '赵六', '钱七'],
                   'score':[95,88, 95, 92, 78]})
print('------original-------')
print(data)
print('-------max----first---')
print(data.nlargest(1,'score'))
print('====min===first====')
print(data.nsmallest(1,'score'))