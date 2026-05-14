# AI大模型开发—14数据分析Numpy和Pandas

# 0.课程内容

## 0.1 晨考

https://ks.wjx.com/vm/Y3rsE1G.aspx# 

## 0.2 课程回顾

基础语法：数据类型 变量 运算符 注释 输入输出 分支 循环

函数：实现特定功能的代码块

定义函数

调用函数

形参：定义函数的时候，指定的参数 

实参：调用函数的时候，传递的值

定义函数的时候，参数可以设置默认值

可变参数：0或多个

​	*参数名  内部就是元组

​	**参数名 内部字典

特殊的函数：

​	递归-函数

​	lambda函数 一行函数

面向对象：思想，类 和 对象

类：定义类

```
class 类名:
	# 构造函数 创建对象完成属性初始化
	def __init__(self,参数,……):
		# 属性
		self.属性名=参数
		……
	# 函数
	def 函数名(self,参数,……):
		实现特定功能的代码块
		return 返回值
	……
```

对象：使用对象 通过对象使用类中定义的属性和函数

```
对象名=类名(值,……)
# 使用属性
对象名.属性名=修改的值
# 函数
变量名=对象名.函数名(值,……)
```

三大特征：封装 继承 多态

文件操作：

```
with open("文件路径和文件名","模式：r a",encoding="utf-8") as f:
	f.write("写出的内容")
	变量名=f.read()
```

正则表达式：一种特殊的字符串，由元字符和量词组成

元字符

量词对应模块：re 常用函数：match

模块 ：py文件，可以导入 import

包：特殊的文件夹，内部由 init文件，分类

Python提供的库：datetime random json re

三方库：requests 请求接口的

json数据格式：一种特殊的字符串

json语法格式：

1.json对象 {"属性名":值,……}

2.json数组 [值,……]

实现json数据的操作：

1.解析json

把json字符串转换为字典或列表  json.loads

2.生成json

把字典或列表 转换为json字符串 json.dumps





# 1.Numpy

## 1.0 数据分析

​	数据分析是指运用统计学、计算机、业务知识，对收集到的结构化 / 非结构化海量数据进行清洗、转换、建模、分析，提取隐藏的规律、趋势、关联关系，最终为业务决策、问题解决、优化改进提供数据支撑的全过程。



## 1.1 Numpy

Numpy：科学计算的基础库，数值计算

底层：c语言开发，性能相对于Python自带的高很多

核心：

一维数组（向量）：内部数据类型一致

二维数组（矩阵）：内部元素又是一个一维数组

> 三方库

Numpy初体验：

1.下载

pip install numpy

2.导入

import numpy as np

3.使用

```python
import numpy as np
# 验证一下是否成功
print(np.__version__)
```

4.效果

![1775787487446](D:\class\2603\随堂笔记\第三周\AI大模型开发—14数据分析Numpy和Pandas.assets\1775787487446.png)

## 1.2 Numpy核心

1.创建

一维数组

二维数组

array(列表)：创建数组，一维或二维

arange(起始值,结束值,步长) 创建等差数组

full(形状,填充值) 创建对应的数组，设置填充值，一维或二维

ones(形状) 创建对应数组，填充值为1

zeros(形状) 创建对应的数组，填充值为0

eye(行,列) 创建单位矩阵（二维数组，主对角线都为1，其余为0）

示例代码：

```python
# 创建一维或二维数组对象
import numpy as np
# array函数 创建对应的数组 ，也叫 转换 把对应的列表转换为Numpy的数组
# 创建一维数组-向量
arr1=np.array([1,2,3,4,5])
print(arr1)
# 创建二维数组-矩阵 3*3
arr2=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr2)
# 遍历元素
for i in arr1:
    print("遍历：",i)
for i in arr2:
    for j in i:
        print("二维遍历：",j,end=" ")
    print()
# arange函数 创建等差一维数组
arr3=np.arange(1,10,2)
print(arr3)
# full 函数 设置数组的填充值
arr4=np.full((3,3),5)
print(arr4)
# ones 创建数组，填充值为1
arr5=np.ones((3,3))
print(arr5)
# zeros 创建数组，填充值为0
arr6=np.zeros((3,3))
print(arr6)
# eye 创建二维数组 ，单位矩阵
arr7=np.eye(3,3)
print(arr7)
```

2.属性

ndim 获取维度 1或2

shape 形状 

size 长度

dtype 元素的数据类型

```python
# 属性
import numpy as np
# 创建数组 矩阵-二维
arr1=np.full((3,3),5)
# 常用属性
print("元素个数，长度：",arr1.size)
print("维度：",arr1.ndim)
print("形状：",arr1.shape)
print("数据类型：",arr1.dtype)
```

3.广播机制和矢量化运算

广播机制：一个数组和一个一维数组并且只有1个元素的进行算术运算，广播机制会自动对一维数组且只有1个元素进行扩展，扩展乘和另一个数组长度一样的数组，再进行算术运算

矢量化运算：一个数组和标量(一个具体的数字)进行算术运算，矢量化运算会把这个标量挨个和数组中的元素进行算术运算

```python
# 广播机制 和 矢量化运算
# 创建数组
import numpy as np

arr1=np.array([1,3,6,10])
# 广播机制 和只有1个元素的向量运算
# 一维数组只有1个元素，和其他数组进行运算，会自动把一维数组只有1个元素会进行扩展，和其他数组长度一样的
# [3]---广播机制 [3,3,3,3]
print(arr1*[3])
arr2=np.array([[2,3,4],[5,6,7]])
# [3]--- 广播机制 [[3,3,3],[3,3,3]]
print(arr2%[3])
# 矢量化运算 和标量运算
print(arr1*4)
print(arr2*4)
```

4.索引和切片

数组可以通过索引访问，索引从0开始

切片：数组名[起始索引:结束索引:步长]

```python
import numpy as np
# 创建数组
arr1=np.arange(1,20,3)
print(arr1)
# 索引
print(arr1[3])
# 切片 [起始索引:结束索引:步长] 结束索引不包含，步长默认为1
print(arr1[1:3])
print(arr1[2:5:2])
# 逆序
print(arr1[::-1])
```

5.常用函数

数组是可以进行算术运算：+ - * / % **

运算相关的函数：abs  exp log sqrt sin cos tan ……

示例代码：

```python
import numpy as np

# 数组
arr1=np.arange(-20,10,4)
print(arr1)
# abs 绝对值
print(np.abs(arr1))
# sqrt 平方根
print(np.sqrt(np.abs(arr1)))
arr2=np.array([1,2,3,4,5])
# exp 指数
print(np.exp(arr2))
arr3=np.array([8,9,16])
# log 对数
print(np.log(arr3))
```

> 周末自主研学：初、高中数学
>
> 平方、立方
>
> 指数
>
> 对数
>
> 三角函数、反三角函数
>
> 极限
>
> 均分分布
>
> 正态分布

变形相关的函数：reshape  transpose np.split

```python
# 变形相关
import numpy as np
# 二维数组 3*4
arr1=np.array([[1,2,3,10],[4,5,6,22],[7,8,9,11]])
print(arr1)
# 二维转其他二维数组，转一维数组
# reshape 函数 变形 2*6 4*3 如果要变为一维数组，那么只写出总数
print(arr1.reshape(2,6))
# 变形 为 一维数组
print(arr1.reshape(12))
arr2=np.arange(1,13)
print(arr2)
# 一维转二维 总数必须匹配
print(arr2.reshape(3,4))
# transpose 转置-矩阵 二维数组
print("转置：",arr1.transpose())
# 数组的拆分
print("--数组拆分--")
print(arr1) # 3*4 按照行 拆 拆成3个 1*4 
# split 拆分数组 参数说明：1.要拆分的数组 2.拆成几份 3.按照行拆还是按照列拆 =0 行，=1列
arr3=np.split(arr1,3,axis=0)
print(arr3)
```

分组统计筛选函数：np.sort np.max np.argmax np.isnan where

```python
# 数组
import numpy as np

arr1=np.array([10,21,3,44,5])
print(arr1)
# 排序
print(np.sort(arr1))
# 二维数组
arr2=np.array([[2,4,3],[10,20,0],[20,12,30]])
# 排序
print(np.sort(arr2,axis=1))
# max 获取最大的元素值，argmax 获取最大值的索引
print(np.max(arr2),np.argmax(arr2))
print(np.min(arr2))
arr3=np.array([1,2,3,4,np.nan,10,22])
# isnan 验证是否为缺失值 一一比对
print(np.isnan(arr3))
arr4=np.array([[1,np.nan,22],[np.nan,2,3],[11,22,np.nan]])
print(np.isnan(arr4))
# where 条件筛选 返回符合要求的元素对应的索引值的元组
print(np.where(arr3>2))
print(np.where(arr3<2))
```



## 1.3 综合练习

1.数组创建
创建一个从 0 到 20（不包含 20）、步长为 2 的一维数组
创建一个 3 行 4 列的全 0 数组
创建一个 2 阶单位矩阵
创建 0~1 之间均匀分布的 5 个随机数

2.数组属性
给定数组 arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
查看数组的维度、形状、总元素数
将数组修改为 1 行 9 列的一维数组

3.索引与切片
给定二维数组：
import numpy as np
arr = np.array([[10,20,30,40],
​             [50,60,70,80],
​             [90,100,110,120]])
取出第 1 行第 2 列的元素
取出前两行、所有列
取出所有行、第 1 列
筛选出数组中大于 50 的所有元素

4.数组运算
定义数组 a = np.array([1,3,5])、b = np.array([2,4,6])，计算逐元素相加、相乘
计算上述数组 a 的均值、标准差、最大值
对二维数组 arr = np.array([[1,2],[3,4]])，按列求和、按行求均值

5.数组变形与拼接
创建数组 arr1 = np.arange(1,5)，将其变形为 2×2 数组
创建数组 arr2 = np.arange(5,9)，变形为 2×2 数组
将两个数组垂直拼接、水平拼接

6.排序与搜索
给定数组 arr = np.array([5,2,9,1,5,6])
对数组进行升序排序
找出数组中大于 3 的元素索引
对数组去重，返回唯一值



# 2.Pandas

## 2.1 Pandas

pandas数据处理(加载、清洗、处理、统计等)，基于numpy，第三方库

提供更为丰富的数据处理的函数

核心：

1.一维数据对象

2.二维数据对象

> 和numpy中数组不一样地方，可以为数据设置标签（自定义索引）
>
> 创建、属性、函数

使用步骤：

1.下载

pip install pandas

2.导入

import pandas as pd

3.验证

```python
# 导入pandas模块
import pandas as pd

# 验证
print(pd.__version__)
```

4.效果

![1775807245868](D:\class\2603\随堂笔记\第三周\AI大模型开发—14数据分析Numpy和Pandas.assets\1775807245868.png)



## 2.2 Pandas核心

1.Series 一维

创建

属性

函数

```python
import numpy as np
import pandas as pd

# 创建一维数据对象
# Series 一维数据对象 参数说明：1.数据（一维数组） 2.index 数据对应的标签（数量一致） 3.dtype 设置值的数据类型（控制占用的大小）
data1=pd.Series(np.arange(1,4),index=['a','b','c'],dtype=np.int8)
print(data1)
# 一维数组 常用属性
# index 属性 获取所有的标签
print(data1.index)
# values 属性 获取所有的值
print(data1.values)
# shape 属性 获取形状
print(data1.shape)
# size 属性 获取元素个数
print(data1.size)
# 一维数组常用的函数
print("--常用函数--")
# 可以通过标签取值
print(data1['a'])
# loc 函数 获取指定标签的值
print(data1.loc['a'])
# iloc 函数 获取指定索引的值
print(data1.iloc[1])
print(data1.sort_values())
# mean函数 平均值
print(data1.mean())
# median
print(data1.median())
# max 函数
print(data1.max())
# sum求和
print(data1.sum())
# 统计值出现迭代次数
print(data1.value_counts())
```

2.DataFrame 二维

创建

属性

基础函数

```python
import numpy as np
import pandas as pd

# 二维数据对象
# DataFrame 二维数据对象 参数说明：1.data 数据 二维数组 2.index 标签，行名 3.columns 标签，列名 4.dtype 值的数据类型
data1=pd.DataFrame([[11,2,22],[10,3,40]],index=['a','b'],
                   columns=['col1','col2','col3'],dtype=np.int8)
print(data1)
# 属性
# index 行的自定义标签
print(data1.index)
# columns 列的自定义标签
print(data1.columns)
# values 值
print(data1.values)
print(data1.shape)
print(data1.size)
print(data1.dtypes)
print("---常用函数--")
# print(data1['a'])
# 通过自定义列标签获取值
print(data1['col1'])
# head 函数 从头往后取指定的行
print(data1.head(1))
# tail 函数 从后往前取指定的行
print(data1.tail(1))
# sample 函数 随机获取指定数量的行
print(data1.sample(1))
# describe 函数 统计结果
print(data1.describe())
# isnull 验证是否为null值 返回二维数据对象
print(data1.isnull())
```

3.数据获取和选择-筛选

```python
# 二维数据对象 数据操作 获取 切片 条件筛选
import pandas as pd

data1=pd.DataFrame({'c1':[1,22,3],'c2':[41,4,6]},index=['r1','r2','r3'])
print(data1)
# 通过列直接获取
print(data1['c1'])
# 通过行获取
print(data1.loc['r1'])
# 行索引
print(data1.iloc[1])
# 切片 返回二维数据对象 [起始行索引:结束行索引:步长] 结束行索引不包含
print(data1.iloc[::-1])
# 条件筛选  二维
print("单条件：",data1[data1['c2']==5])
# c2列 值是偶数 大于5
# & 并且 等同于 and  左右两边都满足 加小括号
print("多条件：",data1[(data1['c2']%2==0) & (data1['c2']>5)])
# | 或者 等同于 or
print("多条件：",data1[(data1['c2']%2==0) | (data1['c2']>5)])
# query函数 实现条件筛选
print(data1.query("c2%2==0 or c2>5"))
```

4.数据文件读写

csv json excel

读取：

pd.read_json

pd.read_csv

pd.read_excel

写出：

to_json

to_csv

to_excel

> excel文件，需要依赖三方库：openpyxl

```python
# 操作文件
# json文件 内容为json格式
# 保存数据到json文件中
import pandas as pd

data1=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],index=['a','b','c'],columns=['x','y','z'])
print(data1)
# 写出到json文件 如果有中文，需要指定force_ascii=False
# to_json 写出内容 格式为json
# data1.to_json("data1.json",force_ascii=False)
# pd.read_json读取对应的文件 获取内容
data2=pd.read_json("data1.json")
print(data2)

# 写出csv文件
data2.to_csv("data2.csv",index=False)
# 读取
print("csv文件：",pd.read_csv("data2.csv"))

# 写出excel文件 需要依赖 openpyxl
data2.to_excel("data2.xlsx",index=False)
print("excel文件：",pd.read_excel("data2.xlsx"))
```

5.数据操作（crud 增删改查）

```python
# 数据操作 修改 和 删除 新增
import numpy as np
import pandas as pd
# 二维数据对象
data1=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['a','b','c'])
print(data1)
# 新增 新的列
data1['d']=[33,44,55]
data1['e']=data1['a']+data1['b']
print(data1)
# 修改
data1.iloc[0,0]=100
data1.loc[1,'b']=200
print(data1)
# 删除
# drop函数 删除 指定列或行 参数说明：1.列名 或行名 2.行还是列 =0行 =1列 3.是否替换，不替换就产生新的数据对象
data1.drop('b',axis=1,inplace=True)
print(data1)
# where 函数 条件筛选平批量处理 inplace参数 True在原对象做替换，False 产生新的
# data1.where(data1.iloc[1]>5,'f',inplace=True)
# print(data1)
```

# 3.综合练习

1. Series 操作
  创建一个 Series：数据为 [5, 10, 15, 20]，索引为 ['一', '二', '三', '四']，数据类型 int8
  打印该 Series 的索引、值、形状、元素个数
  用 loc 取索引为三的值，用 iloc 取第 2 个位置的值
  计算该 Series 的平均值、总和、最大值

2. DataFrame 基础操作
  创建 DataFrame：
  数据：[[8, 2, 5], [3, 9, 1]]，行索引 ['r1', 'r2']，列名 ['c1','c2','c3']，类型 int8
  打印该数据的行索引、列名、形状、数据类型
  查看前 1 行、后 1 行、随机 1 行
  打印数据的描述性统计、空值检测结果

3. 数据筛选
  给定 DataFrame：


  import pandas as pd
  df = pd.DataFrame({'语文': [85, 92, 78, 90], '数学': [90, 88, 76, 95]}, index=['张三', '李四', '王五', '赵六'])

  用 loc 取出李四的所有成绩
  用 iloc 取出第 0 行第 1 列的值
  单条件筛选：数学成绩大于 80 的行
  多条件筛选：语文≥85 且 数学≥90 的行
  用 query 实现：语文 <80 或 数学> 90 的行

4. 数据增删改
  沿用上面的成绩 DataFrame：
  新增列总分，值为 语文+数学
  修改：将王五的语文成绩改为 80
  删除列数学
  删除行索引为张三的行

5. 创建 DataFrame：
  数据：[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]，列名 ['A','B','C']
  新增列D，值为 B列 * 2
  筛选：C 列 大于 5 的所有行
  将筛选后的数据保存为 CSV 文件（不保存索引）
  读取该 CSV 文件，打印前 2 行
  将原数据保存为 Excel 文件（不保存索引）



# 4.总结

numpy 数值计算 

核心：

1.数组

​	一维数组-向量

​	二维数组-矩阵

2.特性

​	广播机制

​	矢量化运算

3.属性

4.函数

> 可以进行算术运算的：+ - * / %



pandas 数据处理，基于Numpy	1 1 12

核心：

1.对象（带标签的数组）

​	一维数据对象

​	二维数据对象

2.一维数据对象

​	创建

​	属性

​	函数

3.二维数据对象

​	创建

​	属性

​	索引与切片

​	函数（特别多）

# 5.作业

Python基础知识 打牢基础

1.使用 NumPy 创建 4 行 3 列的随机整数数组（1~100），将其转换为 Pandas DataFrame，列名设为 语文、数学、英语
查看该 DataFrame 的所有属性（行索引、列名、形状、数据类型）
将 DataFrame 转换回 NumPy 数组，计算数组的总和

2.基于上一题的成绩 DataFrame，使用 np.where 新增一列 等级：
平均分 ≥ 60 → 及格
平均分 ＜ 60 → 不及格
筛选出 语文成绩大于 80 的所有学生数据
使用 NumPy 计算全班每科成绩的平均值

3.用 NumPy 创建数组：[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]，转为 DataFrame，列名 A、B、C
新增列 D：用 Pandas 计算 B列 × 2（NumPy 运算逻辑）
用 np.where 批量修改数据：C 列大于 5 → 改为 99，否则不变
筛选出修改后D 列大于 10的数据，保存为 result.csv
读取 CSV 文件，转 NumPy 数组，打印数组最大值

周末作业：

1.绘制思维导图-手绘

2.查漏补缺

3.作业

4.刷刷力扣

