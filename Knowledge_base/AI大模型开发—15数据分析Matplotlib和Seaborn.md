# AI大模型开发—15数据分析Matplotlib和Seaborn

# 0.课程内容

## 0.1 晨考



## 0.2 课程回顾

Python语言（数据类型、变量、运算符、注释、输入和输出、字符串、容器数据类型(元组、列表、集合、字典)、函数、面向对象（类、对象、三大特征）、文件操作、正则、异常处理、模块、包-命名空间包、标准库、三方库）

数据分析（让数据产生价值）

数据分析核心的内容：

1.numpy 数值计算 核心：一维数组 和 二维数组 ，核心函数：运算、数据操作、排序等，核心机制：广播机制、矢量化运算

2.pandas数据处理 核心：一维数据对象和二维数据对象，核心函数：运算、数据操作、排序、数据处理（缺失值、非法值、数据格式等）

3.matplotlib\seaborn数据可视化

4.机器学习

AI驱动Python的全栈开发

AI-DD新开发范式



# 1.Pandas

## 1.1 Pandas核心

1.排序

排序相关的函数：

```python
import pandas as pd

# 排序
# 二维数据对象
data1=pd.DataFrame([[23,2,30],[1,22,5],[6,10,2]],columns=['语文成绩','数学成绩','英语成绩'])
print("原始内容：")
print(data1)
# 内部的值进行排序
# sort_values函数 根据列进行值的排序 参数说明：1.列名或行名 2.inplace 是否在原对对象上改变，默认为False 3.ascending 是否升序排列，默认升序
data1.sort_values("数学成绩",inplace=True,ascending=False)
print("排序之后")
print(data1)
# sort_index 根据行名或列名进行排序 参数说明：axis =0 表示行，axis=1 表示列
data1.sort_index(inplace=True,ascending=False,axis=1)
print(data1)
print("rank函数")
# rank函数 获取排名 参数说明：1.method 按照什么进行排名 取值：min max …… 2.ascending 按照升序-True还是降序-False排名
data2=data1.rank(method='min',ascending=True)
print(data2)
print("语文成绩最高的2项：")
# nlargest 获取指定列 的最大的前n项
print(data1.nlargest(2,'语文成绩'))
print("数学成绩最低的2项：")
# nsmallest 获取指定列 的最小的前n项
print(data1.nsmallest(2,'数学成绩'))
```



2.数据处理

一般针对二维数据对象，对现有的数据做处理，主要是合规性或格式化处理

常用的处理：

-  

示例代码：

```python
# 准备数据
import numpy as np
import pandas as pd

data1=pd.DataFrame({
    "id":[1,2,30,40,np.nan,-10],
    "name":["ww",'abc','zhangsan','wqes','123','w'],
    "age":[20,30,30,50,60,0],
    'birthday':['2000-10-01','2000 09 01','2001 09 01','2003年07月01日','2008.05.01','2020-01-01']
                    })
print("原始数据：")
print(data1)
# 把不合理的数据变的合规 就需要 数据处理
print(data1.isna())
print(data1.isnull())
print(data1.isnull().sum())
# print("---删除nan值---")
# # dropna 删除nan，参数说明：axis 按照行或列 how删除形式，不写就只删除对应的nan对应的行，all:只有这一行全部nan
# data1.dropna(axis=0,inplace=True)
# print(data1)
# fillna 把nan替换成指定的值
print("---填充---")
# data1['id'].mean() 获取某一列的平均值
data1.fillna(data1['id'].mean(),inplace=True)
print(data1)

print("---校验重复内容---")
print(data1.duplicated())
# duplicated 进行重复的内容的校验 参数：subset 校验指定列的值
print(data1.duplicated(subset='age',keep=False))
# 删除重复
print("---删除重复内容---")
data1.drop_duplicates(subset='age',keep="first",inplace=True)
print(data1)
# id 目前为浮点型 需要转换为整型
print(data1.dtypes)
# astype函数 把指定列的数据类型转换为指定的类型 返回新的内容（列 新的值）
data1['id']=data1['id'].astype(int)
print(data1)
print(data1.dtypes)
print("----查看数据统计----")
print(data1.describe())
# 年龄这一列的值有问题
# apply函数 可以设置处理数据的lambda函数
data1['age']=data1['age'].apply(lambda x:x if 9<x<101 else data1['age'].mean())
print(data1)
# str.xx 使用字符串相关的函数做处理
data1['birthday']=data1['birthday'].str.replace(' ','-').str.replace('.','-')
print(data1)
```



# 2.Matplotlib

## 2.1 Matplotlib

Matplotlib：数据可视化库，显示图表，发音：麦特普洛特力布

和numpy、pandas配合实现数据分析

支持多种图表：折线图、柱状图、饼图、热力图等等

使用步骤：

1.下载

pip install matplotlib

2.导入

import matplotlib

3.使用

```
# 导入
# 导入整个
import matplotlib as mpl
# 按需导入
# from matplotlib import pyplot as plt
# 查看版本号
print(mpl.__version__)
```

4.效果

![1776062721533](D:\class\2603\随堂笔记\第三周\AI大模型开发—15数据分析Matplotlib和Seaborn.assets\1776062721533.png)



## 2.2 常用操作

核心：绘制各种图表

折线图：

```python
from matplotlib import pyplot as plt
# 设置以下信息，解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号 - 显示为方框的问题
# 绘制折线图
data1=["一月","二月","三月","四月"]
data2=[1009,999,200,788]
# plot 绘制折线图 参数：横坐标的数据 纵坐标的数据
plt.plot(data1,data2,color='red',linewidth=5)
# 如果需要显示以往的数据对比，多折线图 那么plot就多个，一般横坐标不变
plt.plot(data1,[999,800,700,900],color='blue',linewidth=5)
# title 设置标题
plt.title('2025-2025年1-4月销量统计',fontsize=30)
# xlabel 设置x坐标轴的名称
plt.xlabel("月份",fontsize=20)
# ylabel 设置y坐标轴的名称
plt.ylabel("销量",fontsize=20,color='green')
# 展示图表
plt.show()
```

![1776064915195](D:\class\2603\随堂笔记\第三周\AI大模型开发—15数据分析Matplotlib和Seaborn.assets\1776064915195.png)

柱状图：

```python
from matplotlib import pyplot as plt
# 设置以下信息，解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号 - 显示为方框的问题

# 柱状图
data1=['大模型2601','大模型2602','大模型2603','大模型2604']
# bar(垂直)或 barh（水平） 柱状图
plt.bar(data1,[12000,13100,15000,14700])
plt.bar(data1,[11000,9000,8888,6666])
plt.title("班级平均薪资")
plt.xlabel("班级")
plt.ylabel("平均薪资")
# 显示图表
plt.show()
```

![1776064883841](D:\class\2603\随堂笔记\第三周\AI大模型开发—15数据分析Matplotlib和Seaborn.assets\1776064883841.png)

饼图：

```python
from matplotlib import pyplot as plt
# 设置以下信息，解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号 - 显示为方框的问题

# 饼图
data1=['行政部','人事部','市场部','研发部','财务部']
# pie 饼状图 参数说明：数据,labels 每个数据的名称,explode 突出显示(设置每块数据图表的间距),shadow 设置是否有阴影
plt.pie([90000,10000,120000,100000,9999],labels=data1,
        explode=[0.05,0.0,0.0,0.05,0.0],shadow=True)
# 设置标题
plt.title('各部门1月份成本支出')
# 显示图表
plt.show()
```

![1776064786950](D:\class\2603\随堂笔记\第三周\AI大模型开发—15数据分析Matplotlib和Seaborn.assets\1776064786950.png)

散点图：

```python
import matplotlib.pyplot as plt
import numpy as np
# 设置以下信息，解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号 - 显示为方框的问题

# 散点图
np.random.seed(2)
# 随机生成 100个 1-100的数字
# 模拟 学员的学号
data1=np.arange(1,101,1)
print(data1)
# 模拟 学员的乘积
data2=np.random.randint(1,100,100)
print(data2)
# 散点图
# scatter 绘制散点图，参数说明：1.x轴 2.y轴-数据 3.s 设置标记符号的大小 4.marker 标记符号，o表示圆形 s表示方块 ^三角形
plt.scatter(data1,data2,color='red',s=20,marker='^')
# 设置图表的标题
plt.title("学员成绩分布")
# 显示
plt.show()
```

更多图表请参考：https://matplotlib.org/stable/users/explain/quick_start.html



# 3.Seaborn

## 3.1 Seaborn

seaborn:数据可视化的三方库，基于Matplotlib，代码相对较少，图表相对美化

使用步骤：

1.下载

pip install seaborn

2.导入

import seaborn as sns

3.使用

```
import seaborn as sns

print(sns.__version__)
```

4.效果

![1776070024348](D:\class\2603\随堂笔记\第三周\AI大模型开发—15数据分析Matplotlib和Seaborn.assets\1776070024348.png)

## 3.2 常用操作

简单了解，图表常用的函数即可

```python
# 导入数值计算库numpy，用于生成随机数、数组等
import numpy as np
# 导入matplotlib的pyplot模块，简称为plt，用于绘图基础设置和展示图表
from matplotlib import pyplot as plt
# 导入seaborn库，简称为sns，用于绘制更美观的统计图表
import seaborn as sns
# 导入pandas库，简称为pd，用于处理数据、创建数据框
import pandas as pd

# ---------------------- 数据准备 ----------------------
# 创建一个DataFrame数据框（表格数据）
# x轴数据a：生成1到100的连续整数，共100个数据
# y轴数据b：生成100个1~100之间的随机整数
data1 = pd.DataFrame({'a': np.arange(1, 101, 1), 'b': np.random.randint(1, 100, 100)})

# ---------------------- 绘图样式设置 ----------------------
# 设置seaborn图表主题：白色背景+网格（whitegrid）
sns.set_style("whitegrid")
# 设置图表字体、线条大小等模板：talk模式（适合展示、字体偏大）
sns.set_context("talk")

# ---------------------- 绘制各类图表 ----------------------
# 1. 绘制柱状图：展示x和y的数值对应关系
sns.barplot(x='a', y='b', data=data1)
# 为柱状图添加标题
plt.title('bar plot')
# 显示当前绘制的图表
plt.show()

# 2. 绘制箱线图：展示数据分布、中位数、异常值等
sns.boxplot(x='a', y='b', data=data1)
plt.title('box plot')
plt.show()

# 3. 绘制分类散点图：展示分类变量与数值变量的关系
sns.catplot(x='a', y='b', data=data1)
plt.title('cat plot')
plt.show()

# 4. 绘制分布图：展示双变量的分布情况
sns.displot(x='a', y='b', data=data1)
plt.title('displot plot')
plt.show()

# 5. 绘制直方图/双变量直方图：展示数据分布密度
sns.histplot(x='a', y='b', data=data1)
plt.title('hist plot')
plt.show()

# 6. 绘制折线图：展示数据随x轴变化的趋势
sns.lineplot(x='a', y='b', data=data1)
plt.title('line plot')
plt.show()

# 7. 绘制小提琴图：结合箱线图和密度图，展示数据分布形态
sns.violinplot(x='a', y='b', data=data1)
plt.title('violin plot')
plt.show()
```



更为详细的图表操作，请参考：https://seaborn.pydata.org/tutorial/introduction.html

# 4.综合练习

练习 1：Pandas 排序与排名实战
要求：
创建 3 名学生的语文、数学、英语成绩 DataFrame
按英语成绩降序排序
按列名升序排序
计算成绩排名（method='min'）
找出语文成绩最高的 1 名学生

练习 2：Pandas 数据清洗（缺失值 + 重复值 + 异常值）
要求：
给定含缺失值、重复年龄、异常年龄的数据
用平均值填充 id 列缺失值
删除age 列重复值（保留第一个）
过滤异常年龄（10<age<100，否则替换为平均值）
查看数据统计信息

练习 3：Matplotlib 双折线图（解决中文乱码）
要求：
绘制 2024/2025 年 1-4 月销量对比折线图
设置中文标题、坐标轴标签
自定义线条颜色和宽度

练习 4：Matplotlib 饼图（突出显示 + 阴影）
要求：绘制 4 个班级人数占比饼图，突出人数最多的班级，添加阴影。

练习 5：Seaborn 基础可视化
要求：
生成 1-50 的随机数据
设置白色网格主题
绘制折线图 + 柱状图

# 5.总结



# 6.作业

## 作业 1：学生成绩综合分析

题目要求
创建 DataFrame：包含学号、姓名、语文、数学、英语，内置缺失值、重复值、异常成绩（<0 或> 100）
数据清洗：
填充成绩缺失值为列平均值
删除重复学号的数据
过滤异常成绩
可视化：
Matplotlib 绘制三科成绩柱状图
Seaborn 绘制成绩箱线图（查看数据分布）

## 作业 2：销售数据可视化

题目要求
生成 1-12 月的随机销售额数据
Pandas：按销售额降序排序，找出最高 / 最低 3 个月
Matplotlib：绘制销量散点图
Seaborn：绘制小提琴图+直方图

## 作业 3：部门支出分析

题目要求

1. 创建 5 个部门的支出数据（含格式不规范的字符串、重复值）
2. 数据清洗：格式化支出金额、删除重复数据
3. Matplotlib：绘制**支出饼图**
4. Seaborn：绘制**折线图**展示支出趋势



