# AI大模型开发—08数据分析Numpy

> 芯源-邢朋辉

# 0.课程内容

## 0.1 晨考

https://ks.wjx.com/vm/YwEDg7s.aspx# 

## 0.2 课程回顾

面向对象：类和对象

类：模板 属性和函数的封装

语法格式：

```python
class 类名:
	# 构造函数
	def __init__(self,参数,……):
		# 定义属性 并 赋值
		self.属性名=值
		……
	# 函数
	def 函数名(self,参数……):
		实现功能的代码块
	……
```

对象：实例 根据类创建的

语法格式：

```
# 创建对象 对象名=变量名 这种数据类型 自定义类
对象名=类名(参数的值,……)
# 使用属性
# 获取属性
对象名.属性名
# 修改属性的值
对象名.属性名=值
# 调用函数
对象名.函数名(参数的值,……)

```

封装：属性的封装，属性私有，提供共有的get和set函数进行操作属性

```
self._属性名 受保护的属性 本类和子类可操作
self.__属性名 私有的属性 本类

def _函数名(xxx) 受保护的函数
def __函数名(xxx) 私有的函数
```

继承：子承父业，子类继承父类，拥有父类的非私有的属性和函数

```python
class 类名(父类的类名):
	def __init__(self,参数,……):
		父类的类名.__init__(self,参数,……)
		//super().__init__(参数,……)
		self.属性名=值
		……
	# 函数
```

多态：具有多种形态 得有继承

1.对象转型 子类对象可以转为父类对象-向上转型-自动

2.函数的重写 子类中可以对父类的函数进行重写 函数名和对应的参数不变

默认函数：

```
__init__ 构造函数，创建对象并完成属性的初始化
__str__  打印对象会自动调用，默认返回对象的内存地址
```

异常处理

try 可以捕获内部的异常，内部出现异常后续代码不在执行，出现异常跳出

expect 匹配异常，匹配到就执行对应的代码 （要写所有可能出现的异常，有时为了省事：Exception）

else try模块没有异常就会执行

finally 无论是否有异常，都会执行的

raise 抛出异常，单独使用



# 1.模块和包

## 1.1 模块

模块：以.py结尾的文件就叫模块

模块内部可以包含：类、函数、变量、语句（分支、循环）

实现模块1：内部实现类和函数的定义

实现模块2：内部定义函数

实现模块3：把模块1全部导入，模块2按需导入进行使用

示例代码如下所示：模块1

```python
# demo1.py 文件就叫模块
# 自定义类
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name} is {self.age} years old'
# 函数
def check_num(num):
    return True if num %2==0 else False
```

示例代码如下所示：模块2

```python
# utils.py
def check_year(year):
    return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False
def check_str(s):
    return True if len(s.strip())>0 else False
```

示例代码：模块3

```python
# demo2.py
# 导入其他模块(.py文件)
# 导入模块 demo1.py 所有的
import demo1 as d
# 导入模块 utils.py中的check_year
from utils import check_year as cy
# 创建对象
s1=d.Student("张三",12)
print(s1)
print(d.check_num(12))
print("是否为闰年：",cy(2001))
```

> 1.导入的方式 
>
> ​	1.按需导入
>
> ​	语法格式：from 模块名 import 导入的类|函数|变量 as 别名
>
> ​	2.导入整个模块
>
> ​	语法格式：import 模块名 as 别名
>
> 2.别名 一些框架都是有固定的别名



## 1.2 包

包（命名空间包）：文件夹\目录，在老版本中，一个目录想做为包，那么内部必须有一个文件，名字固定

`__init__.py`,文件内容为空，标识当前的目录就是包

在新版本之后就不需要init文件作为标识，默认目录都是包，但是开发中还是要求包的话必须有init文件

写项目的时候，会结合业务需要，对模块进行分包，不同包做不同事情

在导入包中某个模块的内容的时候，需要加上包名

示例：创建models包，并在内部创建对应的模块

![1775010105363](D:\class\2603\随堂笔记\第二周\AI大模型开发—08数据分析Numpy.assets\1775010105363.png)

示例：创建apis包，并在内部创建对应的模块

![1775010149935](D:\class\2603\随堂笔记\第二周\AI大模型开发—08数据分析Numpy.assets\1775010149935.png)

示例：导入包中的模块

```python
# 导入其他包中的模块
import models.cardata as cd
from apis.weatherapi import get_weather as gw
# 创建对象
c1=cd.Car("小米汽车","su7",2024)
cd.list1.append(c1)
for x in cd.list1:
    print(x.make)
    print(x.model)
    print(x.year)

print("函数调用：",gw("郑州"))
```



## 1.3 库

Python提供了一些标准库，可以直接导入使用

标准库：

1.random

2.math

3.datetime

使用的示例代码：

```python
# 导入对应的模块（库）
# 标准库 系统自带 随机数
import random
# 算术库 math
import math
# 日期时间
import datetime

# 获取随机数 random() [0,1)
print("随机数",random.random())
# 随机1-10的数字
print("你的幸运数字：%d"%(random.random()*10+1))
# floor 向下取整
print(math.floor(1.2))
print(math.floor(random.random()*10+1))
# ceil 向上取整
print(math.ceil(1.2))
# log10
print(math.log10(3))
# 获取当前时间
print(datetime.datetime.now())
print(datetime.datetime.today())
d=datetime.datetime.now()
print(d.year,d.month,d.day,d.hour,d.minute,d.second)
```

4.json

> json一种特殊的字符串，目前主流的数据交互的数据格式
>
> 语法格式：
>
> 对象：{ "属性名":值,…… }
>
> 数组：[  元素,…… ]
>
> 对象中的值可以是：整型、浮点型、字符串、布尔类型、对象、数组
>
> 数组中的元素可以是：整型、浮点型、字符串、布尔类型、对象、数组
>
> 下面的json格式：
>
> {"id":1,"name":'zhangsan'}对
>
> {"age":12,11,33} 不对
>
> [11,33,44]对
>
> ["id":11,{"name":"zz"}] 不对
>
> 编程中对json格式的数据的操作就2种：
>
> 1.生成json格式的内容
>
> 2.解析json格式的内容
>
> 可以合理的使用json格式化网站进行json格式的数据分析
>
> 比如：https://tool.juhe.cn/

开发中对json的操作：

1.解析json内容为对象或列表

> {}开始，那就解析为对象
>
> []开始，那就解析为列表

json.loads(带解析的字符串)

2.生成json内容

> 把对象或列表转换为json格式的字符串

json.dumps(要转换的对象或列表,ensure_ascii=False)

> ensure_ascii=False 解决中文编码的问题

示例代码：

```python
# 系统自带的json模块
import json
# 解析json
# json格式的字符串
s1='{"id":101,"name":"lisi","age":12}'
print(type(s1))
# 解析json数据 转换 对象
# loads 函数 解析json字符串 参数：带解析的字符串 返回 字典类型
# json对象 解析 转换字典
obj1=json.loads(s1)
print(type(obj1))
print(obj1["id"])
# json数组
s2='[11,22,33,44]'
print(type(s2))
# json数组 解析之后  列表list
list1=json.loads(s2)
print(type(list1))
print(list1[0])

# 生成 json格式的内容
l2=['abc','def','ghi']
print(type(l2))
# dumps 把对象或列表转换为json格式的字符串 json数组 []
s3=json.dumps(l2)
print(type(s3))
print(s3)

stu1= {"id":1,"name":"lisi","ages":[12,18,22,30]}
print(type(stu1))
# dumps 把对象或列表转换为json格式的字符串 json对象 {}
s4=json.dumps(stu1)
print(type(s4))
print(s4)
```

第三方库：需要先下载，再导入，后使用

> pip 设置国内镜像代码，下载速度会一点

1.pydantic

数据校验处理

> 使用步骤：
>
> 1.下载
>
> pip install pydantic
>
> ![1775015477468](D:\class\2603\随堂笔记\第二周\AI大模型开发—08数据分析Numpy.assets\1775015477468.png)
>
> 2.导入并使用
>
> ```python
> # 导入三方库
> from pydantic import BaseModel
> # 定义类 必须继承 BaseModel
> class Student(BaseModel):
>     id:int
>     name:str
>     age:int
> # 待解析的json字符串 
> json1='{"id":1,"name":"admin","age":"12"}'
> # parse_raw 解析json字符串
> s=Student.parse_raw(json1)
> print(type(s))
> print(s.id,s.name,s.age)
> ```

2.requests

想要请求Api接口，那么就需要http请求，需要用到三方库：requests

作用：请求接口

> 接口平台：聚合数据、快递100、钉钉、企微……
>
> 最火大模型：接口

Api接口主要的请求方式：

1.get请求

2.post请求

> get和post区别

接口地址：https://v1.hitokoto.cn/?c=f&encode=text

使用步骤：

1.下载

pip install requests

2.导入并使用

> 基于requests请求接口

参考代码：

```python
# requests 三方库 请求接口
import requests
# 实现接口请求
def get_json(url,data=''):
    # 发起get请求
    response=requests.get(url,params=data)
    #验证是否成功
    if response.status_code == 200:
        return response.text
    else:
        return ''
# post请求
def post_ai(url,headers,data):
    response=requests.post(url,headers=headers,data=data)
    if response.status_code == 200:
        return response.json()
    else:
        return ''

# 发起get请求
r1=get_json("https://v1.hitokoto.cn/?c=f&encode=text")
print(r1)
city=input("请输入城市的名称：")
p2={
    "cityname":city,
    "key":"819bd521a100686c112ed92bd696635c"
}
r2=get_json("http://v.juhe.cn/weather/index",p2)
print(r2)
# post请求
print(post_ai("http://v.juhe.cn/toutiao/index",
              {
                  "Content-Type":"application/x-www-form-urlencoded"
              },data={"key":"7f14068bf84db1f93377e4a98c8c8404"}))
```



通过requests调用大模型的Api步骤如下所示：

1.选择对应的大模型 智谱、Kimi、MiniMax、通义千问、DeepSeek等

2.注册大模型开放平台的账号，并新增key

智谱AI开放平台：https://bigmodel.cn/

3.查阅开发文档，找到http Api接口交互

![1775035495410](D:\class\2603\随堂笔记\第二周\AI大模型开发—08数据分析Numpy.assets\1775035495410.png)

4.通过requests实现大模型的Api的调用

> 调用有2种方式：
>
> 第一种：普通调用 缺点：等待时间特别长，需要完全结束才可以获取结果
>
> 第二种：流式调用 优点：大模型回答着响应着，体验比较好

普通调用 示例如下：

```python
# 大模型 Api 普通调用
import requests


# post请求
def post_ai(url,headers,data):
    response=requests.post(url,headers=headers,data=data)
    if response.status_code == 200:
        return response.json()
    else:
        return ''
# 请求大模型的接口 实现问答
q3=input("请输入你的问题：")
# 需要的请求消息头
h3={
    "Content-Type": "application/json", # 返回的数据为json格式
    "Authorization": "Bearer 21a11a1acd5ee6eb4565aab225ad5fd1.6JPhTKgnliseuJnc" # 设置对应的key
}
# 需要的请求参数
d3='{"model":"glm-5","messages":[{"role":"user","content":"'+q3+'"}]}'
r3=post_ai("https://open.bigmodel.cn/api/paas/v4/chat/completions",h3,d3)
print(r3)
```

大模型Api流式调用

```python
# requests 流式请求 去 和大模型进行交互
import requests


def post_stream(url,headers,data):
    # 发起流式请求
    response = requests.post(url, headers=headers, data=data,stream=True)
    # 获取流式数据 iter_lines data:返回值  data:{}
    # 监听流式数据返回
    for data in response.iter_lines():
        if data:
            s=data.decode("utf-8")
            print(s)


# 流式请求大模型
# 1.请求消息头
q=input("请输入你的问题：")
# 需要的请求消息头
h={
    "Content-Type": "application/json", # 返回的数据为json格式
    "Authorization": "Bearer 21a11a1acd5ee6eb4565aab225ad5fd1.6JPhTKgnliseuJnc" # 设置对应的key
}
# 准备发送的数据
d='{"model":"glm-5","messages":[{"role":"user","content":"'+q+'"}],"stream":true}'
post_stream("https://open.bigmodel.cn/api/paas/v4/chat/completions",h,d)
```

> 思考：怎么把流式返回的数据，只要内容，并且不会出现异常？

DeepSeek开放平台

Kimi开放平台

千问开放平台

miniMax开发平台



# 2.综合练习

1.基于requests调用5个不同的api并把结果显示同时存储到txt文件中

2.基于requests调用至少一个大模型的Api接口，实现2种+形式的调用，比如普通调用、流式调用、思考推理模式等，并把每一次交互的：问题+响应的结果保存到文件中





# 4.总结



# 5.作业

小作业：

1.自学一下：矩阵、向量分别是什么，怎么进行运算的？



