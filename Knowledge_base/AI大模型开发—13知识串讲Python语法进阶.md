# AI大模型开发—13知识串讲Python语法进阶

# 0.课程内容

## 0.1 晨考

https://ks.wjx.com/vm/Qs1a8C8.aspx# 

## 0.2 课程回顾

循环结构

​	for语句

​	while语句

​	循环可以嵌套使用

​	循环控制关键字：continue break

函数

​	定义函数 调用函数

​	函数的参数，函数的返回值 return

​	函数的几种形式：递归函数、Lambda函数

容器数据类型：存储多个值

​	元组 (值)  有序 可重复，不可更改

​	列表 [值] 有序 可重复 可更改

​	集合 {值} 无序，不可重复，可更改

​	字典 {键:值} 有序、每个元素师键值对，键不可重复，值可以，可更改

字符串：str

​	索引、切片

​	函数：len split replace ……





# 1.文件操作

Python操作文件，可以实现写出和读取

语法格式：

```
with open("操作的文件路和文件名","操作模式",endcoding="utf-8") as f:
	f.操作文件的函数
```

写出文件：

```python
# 写出文件
l1=[11,22,33,44,55,'我爱大模型']
with open("data2.txt","a",encoding="utf-8") as f:
    for i in l1:
        # 每个内容单独占用一行
        f.write(str(i)+"\n")

print("写出内容成功！")
```

读取文件：

```python
# 读取文件内容
l1=[]
with open("data1.txt","r",encoding='utf-8') as f:
    # print(f.readlines())
    # print(f.readline())
    # 读取全部内容 字符串
    s1=f.read()
    # 按照格式进行切割
    l1=s1.split("\n")
print("读取完成")
print("结果：",l1)
```



# 2.面向对象

## 2.1 面向对象

面向对象是一种开发的思想，在日常开发中，可以封装类（公共的属性和函数），通过对象使用

核心目的：简化代码，提高代码复用率

面向对象的核心：类和对象

> 面向对象会不会取决于：你能不能熟练的定义类和使用对象

面向对象的三大特征：

​	1.封装 隐藏内部的细节

​	2.继承 复用父类的属性或函数

​	3.多态 一个东西有多种形态 

## 2.2 类和对象

定义类的语法格式：

```python
class 类名:
	属性:数据类型
	……
	def __init__(self,参数,……):
		self.属性名=值
		……
	
	def 函数名(self,参数,……):
		实现功能的代码块
		return 返回值
	……
```

对象创建的格式：

```
对象名=类名(值,……)
对象名.属性名
对象名.属性名=值
对象名.函数名(值,……)

```

示例：

```python
# 面向对象
# 类：模板，封装公共的属性和函数 对象：实例，具体的
class Person:
    # 属性
    id:int
    name:str
    age:int
    # 函数  构造函数 创建对象
    def __init__(self,id:int,name:str,age:int):
        self.id=id
        self.name=name
        self.age=age
    # 函数
    def show(self):
        print(self.id,self.name,self.age)

# 对象
# 创建对象
person1=Person(11,'李四',19)
print(person1.name)
person1.age+=20
person1.show()

# 类的定义 简化版本
class Dog:
    def __init__(self,id:int,name:str,age:int):
        self.id=id
        self.name=name
        self.age=age
    def show(self):
        print(self.id,self.name,self.age)
# 对象
dog1=Dog(11,'旺财',5)
print(dog1.id)
dog1.show()
```



## 2.3 核心内容

1.访问控制

​	默认类中的属性，在哪里都可访问，默认为公有的

​	self._属性名 受保护的 只能在本类或子类中

​	self.__属性名 私有的 只能在本类中

```python
# 面向对象的 访问控制 和三大特征
class Car:
    def __init__(self,brand,model,year):
        # 公有 访问不受限
        self.brand=brand
        # 受保护的 访问受限 本类或子类
        self._model=model
        # 私有的 访问受限 本类
        self.__year=year
    # 函数
    def sale(self):
        print("车辆已卖：",self.brand,self._model,self.__year)
    # 私有函数 只能 本类 
    def __buy(self):
        print("私有函数")

# 对象
c1=Car("比亚迪","唐L",2024)
print(c1.brand)
c1.sale()
```

2.特征一 封装

​	属性私有，通过公有的get和set函数进行操作属性

​	好处：隐藏内部细节

3.特征二 继承

​	一个类可以继承其他的类

​	父类： 公共的属性和函数

​	子类：继承父类，拥有父类非私有的属性和函数

​	好处：简化重复代码，类之间有关系

4.特征三 多态

​	一个函数有多种形态（重写）

​	一个对象有多种形态（对象转型 子类对象可以转换为父类对象）

示例：

```python
# 面向对象三大特征
# 封装
class Phone:
    def __init__(self,model:str):
        # 私有属性
        self.__model=model
    # 公有的get函数 获取私有属性的值
    def get_model(self):
        return self.__model
    # 公有的set函数 设置私有属性的值
    def set_model(self,model:str):
        self.__model=model
p1=Phone("苹果18")
print(p1.get_model())
p1.set_model("华为Meta8")
print(p1.get_model())
# 继承 2个类
# 父类
class Animal:
    def __init__(self,type:str,name:str):
        self.type=type
        self.name=name
    def eat(self,food:str):
        print(f'{self.name}喜欢吃{food}')
# 子类 继承父类
class Cat(Animal):
    def __init__(self,type:str,name:str,age:int):
        # super().__init__(type,name)
        Animal.__init__(self,type,name)
        self.age=age
    def show(self):
        print(self.name,self.age)

# 创建对象
c1=Cat("猫",'喵喵',3)
c1.eat("猫粮")
c1.show()

# 多态
# 重写 在子类中，对父类中定义的函数进行重写
class Dog(Animal):
    def __init__(self,type:str,name:str):
        Animal.__init__(self,type,name)
    # 对父类中定义的函数进行重写
    def eat(self,food:str):
        if len(food.strip())==0:
            print(f"亲，你的 {self.name} 吃什么呢！")
        else:
            super().eat(food)
#
d1=Dog("狗","花花")
d1.eat('   ')
d1.eat("狗粮")
c1.eat("小鱼")
# 对象转型 子类对象 自动转换为父类对象
def like(obj:Animal):
    print(obj.name,obj.type,type(obj))

like(c1)
like(d1)
```

5.内置函数

构造函数：`__init__` 创建对象自动调用

str函数：`__str__`  打印对象 自动调用，默认是对象的地址，可以重写

6.内置属性

dict属性:`__dict__`



## 2.4 综合练习

1. 学生信息管理系统
  要求：
- 基于面向对象思想，开发一个简单的学生信息管理系统，包含以下功能：
  - 定义 StudentManager 类，封装学生信息的增、删、改、查、保存、读取功能。
  - 属性：student_list（存储所有学生对象的列表）、file_path（保存学生信息的 JSON 文件路径，如“students.json”）。
  - 方法：
    1. add_student(self, student)：接收一个 Student 对象，添加到 student_list，确保学号不重复（若重复，提示“学号已存在，添加失败”）。
    2. delete_student(self, student_id)：根据学号删除学生，删除成功提示“删除成功”，学号不存在提示“未找到该学生”。
    3. update_student(self, student_id, new_info)：根据学号修改学生信息（new_info 为字典，如 {"age":21, "major":"软件工程"}），修改成功提示“修改成功”。
    4. query_student(self, student_id=None)：若传入学号，查询单个学生信息并打印；若不传入，查询所有学生信息并打印。
    5. save_to_file(self)：将 student_list 中的所有学生对象，转为字典列表，通过 json 模块保存到 file_path 指定的文件中。
    6. read_from_file(self)：读取 file_path 中的 JSON 文件，将字典列表转为 Student 对象列表，赋值给 student_list（程序启动时调用，实现数据持久化）。
- 编写主程序，创建 StudentManager 对象，调用 read_from_file 读取数据，提供简单的命令行交互（如输入“1”添加学生、“2”删除学生、“3”修改学生、“4”查询学生、“5”保存并退出），模拟实际使用场景。



# 3.模块和包

## 3.1 模块

在Python语言中，每一个py文件就是一个模块，内部可以定义变量、类、函数

模块之间可以相互导入使用其他模块内部的内容

导入模块的2种形式：

1.全导入 import 模块名 as 别名

2.部分导入 from 模块名 import 变量|类|函数等等

定义模块：demo6.py

```python
# py文件就叫模块
VERSION=1.1
class Student:
    def __init__(self,no:str,name:str,sex:str,age:int):
        self.no=no
        self.name=name
        self.sex=sex
        self.age=age
    def __str__(self):
        return f"学号：{self.no},姓名：{self.name},性别：{self.sex},年龄：{self.age}"
def add(num1:int,num2:int):
    return num1+num2
```

导入模块并使用：demo7.py

```python
# 导入模块
# 全部导入
import demo6 as d

print(d.VERSION)
s1=d.Student("xy1001","李四","男",18)
print(s1)
print("函数：",d.add(1,1))
```

## 3.2 包

包：命名空间包

一种特殊的文件夹（目录），内部包含：`__init__.py`

好处：分类模块，把多个模块（py文件）按照功能或者对应的场景分为多个包

包的创建有2种形式：

1.直接创建Python软件包

​	自动创建对应的init文件

2.创建文件夹，在手动创建py文件，文件名必须为：`__init__.py`



![1775706672383](D:\class\2603\随堂笔记\第三周\AI大模型开发—13知识串讲Python语法进阶.assets\1775706672383.png)



## 3.3 内置函数和标准库

Python提供了一些内置函数，可以直接使用

max(xx,……) 最大值

min(xx,……) 最小值

sum(xx,……) 求和

abs(xx) 绝对值

round(xx,xx) 四舍五入

int(xx) 转换为整型

str(xx) 转换为字符串类型

bool(xx) 转换为布尔类型

float(xx) 转换为浮点型

open(xx) 打开文件，进行文件的读写



Python提供了一些标准库

要使用的时候，需要先导入后使用

random 随机数

datetime 日期时间

json 操作json

```python
import random
import datetime

# 内置函数
print(max(11,33))
print(min(10,9))
# 四舍五入 同时指定小数位
print(round(13.55,1))
# 次幂
print(pow(2,3))

# 标准库random() [0,1)
print("随机数",random.random())
# 日期
print("当前时间：",datetime.datetime.now())
d=datetime.datetime.now()
print(d.year,d.month,d.day,d.hour,d.minute,d.second)
print("星期：",d.weekday())
```

## 3.4 json

系统数据交互的格式：

1.xml

2.json(最为主流)

json数据：符合json格式的数据，一种特殊字符串

> 数据格式：跨平台 跨编程语言 跨设备 都可以通用

json的语法格式：

json的数据分为2种：

1.json对象

语法格式：`{"属性名":值,……}`

> 属性名为字符串，必须使用引号
>
> 属性必须有值，值可以为任意类型：整型、浮点型、布尔类型，字符串类型，对象（类）、数组

2.json数组

语法格式：`[值,……]`

> 数组存储的值，值可以为任意类型

举例下述就是常见的json

```
{"name":"张三"}
[11,22]
[{"name":"李四"},{"name":"赵武"}]
{"id":1,"shop":"二七万达店","sales":[102,99,887]}

["id":1] {11,22} 这样的都是不对的
```

怎么把json数据转换为对象(列表) --解析json

> json.loads(带解析的json数据-字符串)

怎么把对象(列表)转换为json数据--生成json

> json.dumps(对象或列表,ensure_ascii=False)
>
> 如果有中文，需要设置ensure_ascii参数为False, 不使用ASCII编码

Python语言使用标准库 json 实现json数据的操作

json实现json数据处理：

1.导入json模块

2.生成json数据-dumps

3.解析json数据-loads

```python
# 操作json数据
import json

# 生成 json数据
obj1={"id":101,"name":"小花","sex":"女","age":18}
print(obj1,type(obj1))

# 把对象 转换为 json
# dumps 函数 把对象或列表 转换为 json字符串
json1=json.dumps(obj1,ensure_ascii=False)
print(json1,type(json1))
print(json1,type(json1))

obj2=["abc","wwe","eer","123"]
print(obj2,type(obj2))
json2=json.dumps(obj2)
print(json2,type(json2))

# 解析
print("--解析--")
print(json1,type(json1))
# loads 解析json数据（字符串） json 字符串->字典类型或列表类型
obj3=json.loads(json1)
print(obj3,type(obj3))
obj4=json.loads(json2)
print(obj4,type(obj4))
```



## 3.5 三方库

三方库：第三方公司或个人开发和维护的Python库

三方库使用步骤：

1.下载

pip install xxx

2.导入

import xxx as xx

3.使用

> 建议查询官方手册

比如requests三方库的使用

requests三方库：请求Api接口 实现网络数据交互

> 调用大模型的Api
>
> api接口地址：https://api.apiopen.top/docs

基于requests库实现接口的调用

接口路径：https://api.apiopen.top/api/json

第一步：下载库

![1775717629045](D:\class\2603\随堂笔记\第三周\AI大模型开发—13知识串讲Python语法进阶.assets\1775717629045.png)

第二步：导入并使用

```python
# requests库 实现接口的调用
import requests
# 发起get请求 获取响应的结果
def get_json(url,params):
    response = requests.get(url,params)
    if response.status_code == 200:
        # json() 响应的结果解析json数据 字典或列表
        return response.json()
        # 获取响应内容 字符串
        # return response.text
    else:
        return '接口有误！'

# 请求接口
json1=get_json('https://api.apiopen.top/api/json','')
print(type(json1))
print("get请求：",json1)
# 遍历 字典
for k,v in json1.items():
    print(k,v)
# 遍历 列表
for i in json1["data"]:
    print(i)
```

post请求

```python
# post请求
def post_json(url,headers,data):
    # post 发起post请求 参数说明：1.接口地址 2.传递数据 3.设置的请求消息头
    response = requests.post(url,data,headers=headers)
    if response.status_code == 200:
        return response.json()
    if response.status_code == 200:
        return response.json()
    else:
        print(response.text)
        return "接口有误！"

# 调用post接口
json3=post_json("https://api.apiopen.top/api/auth/register",'','')
print(json3)
```

> Python 主流第三方库大全
>
> 一、数据处理与分析（数据岗 / 办公必备）
> Python 最核心的优势领域，处理表格、数值、大数据的基石
> NumPy：数值计算基础库，高效处理数组 / 矩阵运算，所有科学计算库的底层依赖
> Pandas：数据处理王者，像操作 Excel 一样处理 CSV/Excel/SQL 数据，数据分析必学
> SciPy：基于 NumPy，专业科学计算（积分、线性代数、信号处理、优化）
> Polars：新一代高性能数据处理库，速度远超 Pandas，适合大数据量
> 二、Web 开发（后端 / 接口开发）
> Flask：轻量灵活，小型项目、API 接口首选，入门简单
> Django：全栈重量级框架，自带后台、认证、数据库 ORM，适合大型企业项目
> FastAPI：现代高性能 API 框架，异步支持、自动生成接口文档，AI 接口 / 微服务主流
> Requests：HTTP 请求库，写接口测试、简单网络请求必用
> 三、机器学习 / 深度学习 / AI（最热门方向）
> Scikit-learn：传统机器学习入门首选，分类、回归、聚类、降维一站式
> PyTorch：深度学习主流框架（Facebook），易用性强，科研 / 工业界双料冠军
> TensorFlow/Keras：谷歌深度学习框架，适合生产部署
> Transformers：Hugging Face 出品，大模型调用（LLM、CV、NLP）必备
> OpenCV-Python：计算机视觉，图像处理、人脸识别、视频分析
> XGBoost/LightGBM：梯度提升树算法，数据竞赛神器
> 四、数据可视化（图表 / 大屏）
> Matplotlib：基础绘图库，静态图表（折线图、柱状图、散点图）
> Seaborn：基于 Matplotlib，统计可视化更美观
> Plotly：交互式可视化，支持网页端缩放、筛选
> Pyecharts：百度 ECharts 封装，快速做数据大屏、炫酷图表
> 五、网络爬虫（数据采集）
> Requests：发送 HTTP 请求，爬虫基础
> BeautifulSoup4：解析 HTML/XML 网页数据
> Scrapy：专业爬虫框架，高并发、分布式爬取大型网站
> Selenium/Playwright：浏览器自动化，模拟人工操作，爬取动态网页
> 六、办公自动化（解放双手）
> openpyxl：读写 Excel 文件
> python-docx：操作 Word 文档
> PyPDF2：合并、拆分、提取 PDF 内容
> python-pptx：生成 / 修改 PPT
> 七、GUI 桌面应用
> Streamlit：零前端知识，快速做数据科学 Web 应用（最推荐）
> PyQt6/PySide6：专业桌面应用开发，功能强大
> Tkinter：Python 自带轻量 GUI，简单小工具首选
> 八、数据库操作
> SQLAlchemy：ORM 框架，优雅操作关系型数据库
> pymysql：MySQL 直连库
> pymongo：MongoDB 非关系型数据库操作
> 九、测试与工具
> pytest：Python 最流行的单元测试框架
> Black：代码自动格式化工具
> Psutil：系统监控（CPU、内存、磁盘、进程）

## 3.6 综合练习

1.JSON 与 requests ：简单接口请求与数据处理

要求：

- 使用 requests 库发送 GET 请求，访问公开测试接口：`https://api.apiopen.top/xx?page=1&count=2`（笑话接口，无需密钥）。
- 获取响应结果，将响应内容（JSON 格式）解析为 Python 字典，提取出所有笑话的“content”字段，打印每一条笑话内容。
- 将解析后的 Python 字典，通过 json 模块保存到本地文件 `jokes.json` 中，确保文件可正常读取。

2.模块与包
要求：

- 创建一个名为 data_tools 的包，包含以下结构：
    ​    data_tools/
    ├── __init__.py
    ├── json_tool.py
    └── file_tool.py
- 在 json_tool.py 中定义2个函数：
  - json_to_dict(json_str)：接收一个 JSON 字符串，解析为 Python 字典，若解析失败，返回空字典并提示错误。
  - dict_to_json(dict_data, file_path)：接收一个字典和文件路径，将字典转为 JSON 格式并保存到指定文件，确保缩进为4。
- 在 file_tool.py 中定义1个函数：read_file(file_path)：读取指定路径的文件（支持 .txt、.json 格式），返回文件内容（JSON 文件返回解析后的字典，txt 文件返回字符串）。
- 在 __init__.py 中导入上述3个函数，使得外部可以通过 from data_tools import json_to_dict, dict_to_json, read_file 直接导入使用。
- 创建测试文件，导入 data_tools 包中的函数，完成：① 将一个学生信息字典保存为 JSON 文件；② 读取该 JSON 文件并打印；③ 读取一个 txt 文件（自行创建）并打印内容。



# 4.正则表达式

## 4.1 正则表达式

正则表达式：一种处理字符串的语法，可以快速实现字符串内容的校验，查找，分组，替换

> 正则表达式 不区分编程语言

正则表达式需要掌握：

1.元字符

一些用在正则表达式上有特殊函数的符号

| 序号 | 元字符            | 作用                  |
| ---- | ----------------- | --------------------- |
| 1    | \d                | 数字                  |
| 2    | \D                | 非数字                |
| 3    | \w                | 字母、数字、下划线    |
| 4    | \W                | 非 字母、数字、下划线 |
| 5    | `[a-z][A-Z]`      | 大小写英文字母        |
| 6    | `[0-9][a-z][A-Z]` | 大小写字母和数字      |
| 7    | ^                 | 开头                  |
| 8    | $                 | 结尾                  |

2.量词

| 序号 | 量词  | 作用         |
| ---- | ----- | ------------ |
| 1    | {n}   | n次          |
| 2    | {n,m} | n-m次        |
| 3    | *     | 0或1次或多次 |
| 4    | +     | 至少1次      |
| 5    | ?     | 最多1次      |

Python对于正则表达式有个标准库 re

re库提供了一些常用的正则表达式的函数

> 正则表达式（字符串）都需要r"正则表达式字符串"

match 从头开始匹配

search 查询第一次出现

sub 替换

findall 查询全部

> 最常用的是match函数

示例代码：

```python
# 正则表达式
import re

phone=input("请输入手机号：")
print("用户输入：",phone)
# 校验是否为手机号 11位 第一个数字：1 第二个数字：3-9之间 第三个到第十一个：纯数字 0-9

r=True
if len(phone)!=11:
    r=False
else:
    for i in range(len(phone)):
        # 验证是否为数字
        if phone[i].isdigit():
            # 第一位
            if i == 0:
                if phone[i] == '1':
                    pass
                else:
                    r = False
                    break
            # 第二位
            elif i == 1:
                n = int(phone[i])
                # if n >= 3 and n <= 9:
                if 2<n<10:
                    pass
                else:
                    r = False
                    break
            else:  # 第3位到第11位
                pass
        else:  # 不是数字
            r = False
            break

print(f"{phone} 是不是手机号：",True if r else False)

# 使用正则表达式 匹配是否为手机号
# ^1[3-9][\d]{9}$
# 如果match返回的不是None 说明匹配成功
print(f"{phone} 是不是手机号：", re.match(r"^1[3-9][\d]{9}$", phone))
```

## 4.2 综合练习

1.基于正则表达式实现邮箱合法性校验

2.密码强度校验：只有字母或数字或下划线一种 弱 有2种 强 有3种非常强

3.身份证号码的正则表达式校验



# 5.GUI-了解

## 5.1 GUI-Tkinter

GUI:图形开发界面,桌面程序开发

Python语言有几种GUI库，可以进行桌面程序开发

1.**Tkinter**

2.**wxPython**

3.**Jython**

推荐使用tk



## 5.2 基本操作

tk的基本使用：

1.导入

2.使用

```python
# 导入tk库
import tkinter

# 使用 创建窗口
tk1=tkinter.Tk()
# 加一个按钮
bt1=tkinter.Button()
# 把按钮加到主窗口中
bt1.pack()
# 单行输入框
en1=tkinter.Entry()
en1.pack()
# 列表
l1=tkinter.Listbox()
for i in (11,22,33,44):
    l1.insert(0,i)
l1.pack()
# 显示窗口
tk1.mainloop()
```

设置大小

设置内容

设置事件

示例代码：

```python
#
import tkinter as ttk

# 创建窗口 -根窗口
root=ttk.Tk()
# 设置窗口的标题
root.title("自定义窗口")
# 设置窗口大小
root.geometry("400x400")
# 组件
# 文本组件
label1=ttk.Label(text="欢迎你的到来")
# 加到根窗口，采用 Pack
label1.pack()
# 输入框组件
entry1=ttk.Entry(show="*")
entry1.pack()
# 按钮组件
def get_msg():
    # print(entry1.get())
    # get 获取输入框的内容
    return entry1.get()
# 按钮 text属性 按钮显示的文本内容 command 对应事件 点击
button1=ttk.Button(text="点击获取输入内容",command=get_msg())
button1.pack()
#
root.mainloop()
```

## 5.3 综合练习

1.实现一个简单的计算器



# 6.总结

文件的读写的操作 with open read write

面向对象：类 对象

​	三大特征

​	内置的函数、属性

模块

包

json数据格式的操作：1.解析 2.生成

三方库：requests 和Api接口进行交互

标准库：random datetime json re tk

正则表达式：语法 操作-匹配

GUI-Tkinter Python做桌面程序



# 7.作业

## 7.1 网络接口数据采集与清洗系统

题目要求
整合requests+JSON + 正则 + 文件操作，实现 AI 开发必备的接口数据处理工具：
使用requests发送 GET 请求，调用公开接口：
https://api.apiopen.top/api/xxx?page=1&size=10
核心功能：
请求接口，解析 JSON 响应数据
正则表达式清洗数据：提取纯文本、去除特殊符号、空值过滤
数据统计：统计总条数、字符长度最长的句子
本地持久化：清洗后的数据保存为clean_data.json和clean_data.txt
异常处理：网络错误、接口失败、数据解析失败全部捕获

## 7.2 采用面向对象调用大模型API接口交互

定义 APILog 类，包含属性：请求时间、接口地址、请求参数、响应状态、耗时
定义 APILogManager 管理类，实现功能：
调用大模型（任意大模型都可以）测试接口，自动生成调用日志
日志正则校验：过滤无效接口、非法参数、异常响应
日志存储：将所有调用记录保存为 api_logs.json，支持追加写入
日志查询：按时间 / 状态筛选日志，统计成功 / 失败调用次数
日志导出：将 JSON 日志转换为格式化文本文件 api_logs.txt
完整异常处理：网络异常、文件读写异常、JSON 解析异常全部捕获
命令行交互菜单，支持循环操作