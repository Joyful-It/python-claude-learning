import pandas as pd
import numpy as np

data = {
    # id列：存在缺失值NaN，且因NaN自动为浮点型（后续需转int）
    "id": [1.0, np.nan, 3.0],
    # age列：存在重复值(25)、异常值(150，不合理年龄)
    "age": [25, 25, 150],
    # score列：正常数据，用于对比
    "score": [85, 92, 78]
}
print(data)
data1=pd.DataFrame(data)
print(data1)
print("整体消息")
data1.info()
print("统计")#统计摘要
print(data1.describe())

print(data1.head(1))
#descri 列表
#               id   age   score
# count    2.000000  3.0  3.000000    ← 有几个非空值
# mean     2.000000 66.7 85.000000    ← 平均值
# std      1.414214 62.0 7.000000     ← 标准差（波动大小）
# min      1.000000 25.0 78.000000   ← 最小值
# 25%      1.500000 25.0 81.500000   ← 25%位置的值
# 50%      2.000000 25.0 85.000000   ← 中位数
# 75%      2.500000 25.0 88.500000   ← 75%位置的值
# max      3.000000 150.0 92.000000  ← 最大值
print("\n处理删除值")
data2=data1.dropna()
print(data2)

data3=data1.fillna(2)
print(data3)
print("-----------")
data1['id']=data1["id"].fillna(data1["id"].mean()) #用平均值填充
print(data1)

# 部分                含义
# df['score']    选择 score 这一列
# .mean()        计算这一列的平均值
# .fillna(...)   用括号里的值填 NaN

print("------删除完全重复------")

data1 = data1.drop_duplicates()
print(data1.drop_duplicates(subset='age'))#

# 新建一个有完全重复行的例子
data2 = data1.copy()
data2.loc[3] = [1.0, 25, 85]  # 完全复制第0行

print("去重之前：")
print(data2)

print("\n去重之后：")
print(data2.drop_duplicates())#删除完全一样的行


print('-----处理异常值-----')
# 把 age > 100 的值变成 NaN
#data1.loc[data1['age'] > 100, 'age'] = np.nan
data1[data1["age"]>100]['age'] = np.nan

# 再用平均值填充
data1['age'] = data1['age'].fillna(data1['age'].mean())

print(data1)
