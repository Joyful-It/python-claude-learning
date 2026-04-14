import pandas as pd
import numpy as np

data=pd.DataFrame({'name':['张三', '李四', '王五'],
                   'age':[25,np.nan,30],
                  'scores':[95,88,np.nan] })
print("------isnull-----")
print(data.isnull())

print('\n----number----isnull----')
print(data.isnull().sum())
print('-----before-----')
print(data.dtypes)
print('\n-------after------')
data['age']=data['age'].fillna(data['age'].mean())
data['age']=data['age'].astype(int)#!!!!!!!!!!!astype后加数据类型，
print(data.dtypes)