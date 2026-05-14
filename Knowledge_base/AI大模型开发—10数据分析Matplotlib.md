# AI大模型开发—10数据分析Matplotlib

> 芯源-邢朋辉

# 0.课程内容

## 0.1 晨考

viewonly

xy1688



## 0.2 课程回顾

Python数据分析

数据计算-数据处理-可视化-科学计算-机器学习

Numpy：实现数值的存储和计算

核心：一维数组（向量）和二维数组（矩阵）

特性：广播机制、矢量化运算

标量：独立的值 值

向量：每个元素都是数字[值,]

矩阵：每个元素都是向量（向量内部的元素都是数字）[[值,],]

数组对象常用的属性

常用的操作数组的函数

> 线性代数计算相关函数
>
> 行列式
>
> 向量的内积
>
> 矩阵的乘积
>
> 可逆矩阵



# 1.Pandas

## 1.1 Pandas是什么

Pandas基于Numpy开发，核心作用：处理结构化数据（Excel、Csv、json文件等等）和分析

核心的数据对象：

一维数据对象：Series (带标签的一维数组)

二维数据对象：DataFrame（带标签的二维数组）

Pandas使用步骤：

1.下载

pip install pandas

2.导入并使用

```python
import pandas as pd
print(pd.__version__)
```

3.运行

![1775185959355](D:\class\2603\随堂笔记\第二周\AI大模型开发—10数据分析Matplotlib.assets\1775185959355.png)

## 1.2 Pandas常用操作

### 1.2.1 一维数据对象

1.创建一维数据对象

pd.Series(数据,标签)

2.一维数据对象的属性

size 获取元素个数，长度

ndim 获取维数

shape 获取形状

index 获取对应的标签 一维数组的形式

values 获取对应的值

访问或修改一维数据对象的元素：对象名[标签名]

```python
# 导入
import numpy as np
import pandas as pd

# 一维数据对象
s1=pd.Series([1,2,3,4,5,6],dtype="int8")
print(s1)
# 创建一维数据对象 带标签
s2=pd.Series([1,2,3,4,5,6],dtype="int8",index=['a','b','c','d','e','f'])
print(s2)
# 获取元素
print(s2['a'])
# 元素的个数，长度
print(s2.size)
# 获取维
print(s2.ndim)
# 形状
print(s2.shape)
# 获取 所有的标签 一维数组
print(s2.index)
# 获取所有的值
print(s2.values)

s2["d"]=119
print(s2)
# iloc函数 通过索引获取值
print(s2.iloc[1])
```

3.运算

运算支持矢量化运算、广播机制

```python
import pandas as pd
import numpy as np

# 创建一维数据对象
s1=pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])
# 运算 针对数据  矢量化运算 每个数据都进行操作
print(s1+3)
print(s1*3)
s2=pd.Series([3,3,5,76,8,0],index=['a','b','c','d','e','f'])
# 2个一维数据对象的操作 根据标签对应进行操作
print(s1+s2)
# 和一个一维数组的数据进行运算，会自动广播扩展 
print(s1+np.array([10]))
# [10,10,10,10,10,10]
```

4.常用函数

| **方法名称**                 | **功能描述**                                           |
| ---------------------------- | ------------------------------------------------------ |
| `index`                      | 获取 Series 的索引                                     |
| `values`                     | 获取 Series 的数据部分（返回 NumPy 数组）              |
| `head(n)`                    | 返回 Series 的前 n 行（默认为 5）                      |
| `tail(n)`                    | 返回 Series 的后 n 行（默认为 5）                      |
| `dtype`                      | 返回 Series 中数据的类型                               |
| `shape`                      | 返回 Series 的形状（行数）                             |
| `describe()`                 | 返回 Series 的统计描述（如均值、标准差、最小值等）     |
| `isnull()`                   | 返回一个布尔 Series，表示每个元素是否为 NaN            |
| `notnull()`                  | 返回一个布尔 Series，表示每个元素是否不是 NaN          |
| `unique()`                   | 返回 Series 中的唯一值（去重）                         |
| `value_counts()`             | 返回 Series 中每个唯一值的出现次数                     |
| `map(func)`                  | 将指定函数应用于 Series 中的每个元素                   |
| `apply(func)`                | 将指定函数应用于 Series 中的每个元素，常用于自定义操作 |
| `astype(dtype)`              | 将 Series 转换为指定的类型                             |
| `sort_values()`              | 对 Series 中的元素进行排序（按值排序）                 |
| `sort_index()`               | 对 Series 的索引进行排序                               |
| `dropna()`                   | 删除 Series 中的缺失值（NaN）                          |
| `fillna(value)`              | 填充 Series 中的缺失值（NaN）                          |
| `replace(to_replace, value)` | 替换 Series 中指定的值                                 |
| `cumsum()`                   | 返回 Series 的累计求和                                 |
| `cumprod()`                  | 返回 Series 的累计乘积                                 |
| `shift(periods)`             | 将 Series 中的元素按指定的步数进行位移                 |
| `rank()`                     | 返回 Series 中元素的排名                               |
| `corr(other)`                | 计算 Series 与另一个 Series 的相关性（皮尔逊相关系数） |
| `cov(other)`                 | 计算 Series 与另一个 Series 的协方差                   |
| `to_list()`                  | 将 Series 转换为 Python 列表                           |
| `to_frame()`                 | 将 Series 转换为 DataFrame                             |
| `iloc[]`                     | 通过位置索引来选择数据                                 |
| `loc[]`                      | 通过标签索引来选择数据                                 |

```python
import numpy as np
import pandas as pd

# 创建 一维数据对象
# s1=pd.Series(np.arange(1,100,3))
s1=pd.Series(np.random.default_rng().integers(90,100,30))
print(s1)
# head 获取前n行的数据 如果n不传，就默认5
print(s1.head())
# tail 获取后n行的数据
print(s1.tail(10))
# value_counts 统计每个数值出现的次数
print("统计各个值的出现的次数：",s1.value_counts())
s2=pd.Series([1,22,22,33,33])
# unique 去重
print("出现的值：",s2.unique())
# cumsum 累计求和 第一位+第二位 成为第一个值  其余以此类推
print("累计求和：",s2.cumsum())
```

### 1.2.2 二维数据对象

二维数据对象是Pandas特别重要的对象

DataFrame

1.创建

```python
import numpy as np
import pandas as pd
# 二维数据对象
# DataFrame的参数：data参数：数据(字典-标题行的列名、二维数组) index:设置数据对应的标签 columns:设置标题行
# 第一种创建方式：字典 转换为二维数据对象
df1=pd.DataFrame({'names':["张三","李四","王麻子"],'sexs':["男","女","男"],'ages':[19,20,18]},index=[1,2,3])
print(df1)
# 第二种创建方式：二维数组
df2=pd.DataFrame(np.array([[11,22,33],[20,30,40]]),index=["a","b"],columns=["d","e","f"])
print(df2)
# 常用属性
print(df2.shape)
print(df2.size)
print(df2.ndim)
```

2.获取和操作数据

```python
import pandas as pd
import numpy as np

# 二维数据对象
df1=pd.DataFrame({'a':[1,2,3],'b':[10,20,30],'c':[11,22,33]})
print(df1)
# 二维数据对象 获取内容的方式
# 1.获取列数据  通过列名 Columns
print(df1["a"][2])
print(df1["b"])
# 2 loc 通过标签 获取一行的数据
print(df1.loc[1])
# 获取 具体的值 loc 参数：1.标签 对应行 2.列 对应的列
print(df1.loc[1,"b"])

# 新增
df1['d']=[70,80,90]
print(df1)
# 修改
df1.loc[2,"c"]=66
print(df1)
# 删除
df1.drop(0,axis=0,inplace=True)
print(df1)
```

3.文件操作

读取和保存

> 文件的类型：csv、excel、json

写出内容到文件：

```python
import pandas as pd

# 准备数据
df1=pd.DataFrame({"id":[1,2,3,4,5,6],"name":["爱编程","第三道","带我的","第三道","e3e3","ew"],
                  "age":[11,20,18,19,17,16]})
# 数据保存到json文件中
df1.to_json("test1.json",index=False,force_ascii=False)
# 数据保存到csv文件
df1.to_csv("test1.csv",index=False)
# 数据保存到excel文件 需要依赖库：openpyxl
df1.to_excel("test1.xlsx",index=False,sheet_name="3月份数据")
```

读取文件内容到二维数据对象

```python
import pandas as pd

# 读取文件 的前提 先有文件
# read_csv 读取csv文件，把文件内容转换为我二维数据对象
df1=pd.read_csv("test1.csv")
print(df1)
# read_excel 读取excel文件
df2=pd.read_excel("test1.xlsx")
print(df2)
# read_json 读取json文件
df3=pd.read_json("test1.json")
print(df3)
```

## 1.3 综合练习

1.Series **基础操作**
导入 pandas 和 numpy，创建带自定义标签（a~f）的 Series，数据为[85,92,78,90,88,95]
要求：① 查看前 3 个数据 ② 统计每个数值出现次数 ③ 计算累计求和 ④ 修改标签d对应的值为 100
2.**DataFrame** 创建与属性
用字典创建学生信息 DataFrame，包含列：姓名、学号、成绩，3 行数据
要求：① 查看形状、元素个数 ② 输出所有列名和值
3.**数据查询**（loc/iloc）
基于上一题的 DataFrame，用loc通过标签获取第二行数据，用iloc通过索引获取第一列第三个值
4.**数据增删改**
为学生表新增性别列，修改第一个学生的成绩，删除第三行数据
5.**矢量化运算**
创建两个等长 Series，实现相加、相乘运算，验证广播机制

# 2.总结



# 3.作业

## 作业 1：员工信息数据处理

导入库，创建 DataFrame：
列：员工编号、姓名、部门、薪资
数据：[101,"张三","技术",8000]、[102,"李四","产品",9500]、[103,"王五","运营",6500]、[104,"赵六","技术",9000]
基础操作：新增绩效列（数据：[90,85,95,88]），修改李四的薪资为 10000
函数应用：查看后 2 行数据，统计部门出现次数，获取唯一部门名称
输出所有结果



## 作业 2：成绩数据 Series 综合计算

创建 Series：索引为语文、数学、英语、物理、化学，值为随机整数（70~100）
计算所有成绩 + 10 分（广播运算）
判断成绩是否大于 85（返回布尔值）
查看成绩最大值、数据类型、元素个数
输出最终结果



## 作业 3：DataFrame 文件写入

构建商品销售 DataFrame：商品名、价格、销量（5 行数据）
将数据分别保存为：sales.csv、sales.xlsx、sales.json
要求：csv/excel 不保存索引，json 正常显示中文



## 作业 4：文件读取与数据修改

读取作业 3 生成的sales.csv文件
新增总销售额列（总销售额 = 价格 × 销量）
删除价格低于 10 的行
输出修改后的 DataFrame



## 作业 5：二维数组创建 DataFrame

用 numpy 二维数组[[1,2,3],[4,5,6],[7,8,9]]创建 DataFrame
自定义行索引和列名
通过loc和iloc两种方式获取第二行第二列的值
对所有数据 ×2，输出结果


## 作业 6：班级成绩综合分析系统

创建 DataFrame，包含：学号、姓名、语文、数学、英语（6 名学生数据）
数据处理：
新增总分列（三科成绩之和）
新增平均分列（保留 2 位小数）
筛选操作：找出总分大于 250 的学生
函数应用：统计各科成绩的唯一值，查看成绩描述信息
最终将完整数据保存为class_score.xlsx



## 作业 7：销售数据阶梯处理

读取自定义的商品销售 csv 文件（无文件可手动创建）
计算总销售额，新增列
分级判断（嵌套逻辑）：
总销售额≥5000：高端商品
2000≤总销售额 < 5000：中端商品
<2000：普通商品
统计各级别商品数量
删除销量为 0 的商品行，保存最终数据
作业 8：Series+DataFrame 混合实战
创建 5 个学科的成绩 Series，计算总成绩
将 Series 转换为 DataFrame
新增等级列：≥90 优秀，80-89 良好，<80 及格
对 DataFrame 按成绩降序排序
保存为 json 文件并重新读取验证

