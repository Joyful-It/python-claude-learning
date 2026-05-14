# AI大模型开发—18FastApi

# 0.课程内容

## 0.1 晨考

晨考链接：https://ks.wjx.com/vm/m70nBsf.aspx# 

## 0.2 课程回顾

Git 版本控制软件

实现源代码的管理和团队协作开发

核心：

提交

拉取

推送

切换

合并

配合远程仓库，实现团队协作开发

数据库：Mysql数据库，关系型数据库

SQL语句

创建数据库

创建表

新增数据

修改数据

删除数据

查询数据

多表联查：内连接和左外连接

SQLAlchemy ORM

ORM：对象关系映射

表---类

字段--属性

行---对象

核心：

1.连接数据库

2.创建会话

3.操作数据（CRUD）

4.模型类（继承Base）



FastAPI 实现Api

页面

服务器

AI-DD

# 1.FastApi

## 1.1 FastApi

FastAPI 是Python web（后端）开发的核心库

FastApi=fast(快)+Api(接口)

用来开发api接口

特点：高效、简洁、支持同步和异步、适合用在AI领域

配置环境：

1.下载库

pip install fastapi uvicorn

2.导入使用





Pycharm可以直接创建fastapi项目

![1776304733901](D:\class\2603\随堂笔记\第四周\AI大模型开发—18FastApi.assets\1776304733901.png)

## 1.2 FastApi初体验

1.创建项目

2.下载库

3.在main.py中实现如下的代码

```python
# 导入模块
import random
import fastapi

# 创建应用实例
app=fastapi.FastAPI(title="项目接口文档")

# 定义接口
# get请求 
@app.get("/")
def index(): # 定义函数 
    return {"Hello": "World"}

@app.get("/nums")
def nums(size:int):
    arr=[]
    for i in range(size):
        arr.append(random.randint(1,100))
    return arr
```

4.在终端中输入如下的命令：

uvicorn main:app --reload   

> uvicorn 服务器
>
> main 对应的模块名
>
> :app 固定
>
> --reload 热更新 ，接口发生了改变就自动加载，不需要重启服务器

![1776305853156](D:\class\2603\随堂笔记\第四周\AI大模型开发—18FastApi.assets\1776305853156.png)

5.在浏览器访问接口文档

http://127.0.0.1:8000/docs

![1776305925431](D:\class\2603\随堂笔记\第四周\AI大模型开发—18FastApi.assets\1776305925431.png)

6.测试接口

![1776305986041](D:\class\2603\随堂笔记\第四周\AI大模型开发—18FastApi.assets\1776305986041.png)

## 1.3 FastApi核心

### 1.请求方式

Api的接口请求方式一般都是get或post

@app.get("路径")

@app.post("路径")

@app.put("路径")

@app.delete("路径")

> restful规范的Api接口
>
> 采用相同的路径名，通过不同的请求方式用以区分对应的操作
>
> 新增：post请求
>
> 修改：put请求
>
> 删除：delete请求
>
> 查询：get请求

参考示例：

```python
# get请求方式---查询操作
@app.get("/test",tags=["测试接口"],name="自定义测试接口",description="这个接口啥也不干！")
def test_num(id:int):
    return {"id":id}
def test():
    return {"id":1,"num":random.randint(1,100)}
# post请求方式---新增操作
# 参数说明：tags 设置对应标签（相同就是一组）name 设置接口的名称 description 接口说明信息
@app.post("/random/num",tags=["测试接口"],name="获取幸运数字",description='很专业的获取你的幸运数字')
def random_num(name:str):
    return {"name":name,"lucknum":random.randint(1,100)}
#put请求方式---修改操作
@app.put("/update")
def update_num(id:int,name:str,lucknum:int):
    return {"id":id,"name":name,"lucknum":lucknum}
# delete请求方式---删除操作
@app.delete("/delete")
def delete_num(id:int):
    return {"id":id}
```

![1776309397720](D:\class\2603\随堂笔记\第四周\AI大模型开发—18FastApi.assets\1776309397720.png)

### 2.参数方式

1.键值对方式-查询参数

> 默认是键值对的方式进行传递
>
> 传递格式：参数名=值&……



2.json格式-请求体

> 需要自定义类，实现json数据的封装
>
> 一般用于post请求
>
> 为了实现参数的自动校验，所以自定义类需要继承BaseModel类



3.路径传参-路径携带对应的参数的值

> 直接在路径上{参数名}
>
> 在对应的函数上定义对应的参数（参数名需要和上面一样）
>
> 注意：不要传递复杂的参数

示例代码：

```python
import random
import fastapi
from app import paramapi

# 创建应用实例
app=fastapi.FastAPI(title="项目接口文档")

# 定义接口
@app.get("/")
def index():
    return {"Hello": "World"}

@app.get("/nums")
def nums(size:int):
    arr=[]
    for i in range(size):
        arr.append(random.randint(1,100))
    return arr
# get请求方式---查询操作
@app.get("/test",tags=["测试接口"],name="自定义测试接口",description="这个接口啥也不干！")
def test_num(id:int):
    return {"id":id}
def test():
    return {"id":1,"num":random.randint(1,100)}
# post请求方式---新增操作
# 参数说明：tags 设置对应标签（相同就是一组）name 设置接口的名称 description 接口说明信息
@app.post("/random/num",tags=["测试接口"],name="获取幸运数字",description='很专业的获取你的幸运数字')
def random_num(name:str):
    return {"name":name,"lucknum":random.randint(1,100)}
#put请求方式---修改操作
@app.put("/update")
def update_num(id:int,name:str,lucknum:int):
    return {"id":id,"name":name,"lucknum":lucknum}
# delete请求方式---删除操作
@app.delete("/delete")
def delete_num(id:int):
    return {"id":id}

# 主模块 注册路由（新增定义的路由）
app.include_router(paramapi.router)
```

![1776310738238](D:\class\2603\随堂笔记\第四周\AI大模型开发—18FastApi.assets\1776310738238.png)

### 3.返回数据格式

返回的数据类型为json格式

统一返回结果

参考示例代码：



![1776311315169](D:\class\2603\随堂笔记\第四周\AI大模型开发—18FastApi.assets\1776311315169.png)

### 4.路由模式

分模块实现对应api



## 1.4 综合练习

实现学生的crud操作

创建创建阶段：

1.创建项目

2.依赖库

pip install fastapi uvicorn pymysql sqlalchemy cryptography

3.创建.gitingore文件并设置忽略

4.提交并推送远程仓库

https://gitee.com/coderferi/aistudy181

数据库设计阶段：

```
create database db_company char set 'utf8mb4';
use db_company;
-- 学生表
create table t_stu(
id int primary key auto_increment,
name varchar(20),
sex varchar(2),
gid int,
create_time datetime
);
```

5项目的基础代码的配置：

数据库相关：

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 1.创建连接
engine=create_engine('mysql+pymysql://root:xing%401688@localhost:3306/db_company')
# 2.创建会话
sessionFactory=sessionmaker(bind=engine)
session=sessionFactory()
# 3.封装crud操作
class DbUtil:
    # 新增数据
    def add(self,obj):
        try:
            session.add(obj)
            session.commit()
        except Exception as e:
            print(e)
            return False
        else:
            return True
    # 修改
    def update(self):
        session.commit()
        return True
    # 删除
    def delete(self,obj):
        session.delete(obj)
        session.commit()
        return True
    # 查询 全部
    def all(self,type):
        return session.query(type).all()
    # 查询 带条件
    def find(self,type,**filter):
        return session.query(type).filter_by(**filter).all()
```

6.实现学员模块相关类定义

数据库操作对应的模型类：必须继承Base

```python
import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
# 数据库的 模型类
# 父类
Base=declarative_base()
# 子类  表 对应的类
class Stu(Base):
    __tablename__ = "t_stu"
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String)
    sex=Column(String)
    gid = Column(Integer)
    create_time = Column(DateTime,default=datetime.datetime.now)
```



实现学员Api接口操作

实现Fastapi操作的类的定义，必须继承BaseModel

```python
import datetime
from typing import Optional, Any

from pydantic import BaseModel

class R(BaseModel):
    code: int
    msg: str
    data:Optional[Any] = None
class StuAdd(BaseModel):
    name:str
    gid:int
    sex:str
class StuData(BaseModel):
    id:int
    name:str
    gid:int
    sex:str
    create_time:datetime.datetime
    model_config = {"from_attributes": True}
```

基于FastApi实现crud接口

```python
from fastapi import APIRouter

from api.apimodel import StuAdd, R, StuData
from database.dbutil import DbUtil
from models.Models import Stu

# 路由
router=APIRouter(prefix="/stu",tags=["学生模块"])

db=DbUtil()
# 学生模块的crud 接口
# 新增
@router.post("/add",name="新增学生")
def add(obj:StuAdd):
    stu=Stu(name=obj.name,gid=obj.gid,sex=obj.sex)
    if db.add(stu):
        # 成功
        return R(code=0,msg='',data={"id":stu.id})
    else:
        # 失败
        return R(code=1, msg='新增失败')
# 修改
@router.post("/update",name="修改学生")
def update(obj:StuAdd):
    # 先查询
    stu=db.find(name=obj.name)
    stu.name=obj.name
    stu.gid=obj.gid
    stu.sex=obj.sex
    db.update()
    return R(code=0,msg='')
# 删除
@router.get("/del/{id}",name="删除学生")
def delele_id(id:int):
    s=db.find(Stu,id=id)
    if len(s)>0:
        db.delete(s[0])
        return R(code=0,msg='')
    else:
        return R(code=1,msg='')
# 查询 create_time
@router.get("/list",name="查询全部")
def list():
    s=db.all(Stu)
    arr=[StuData.model_validate(s1) for s1 in s]
    return R(code=0,msg='',data=arr)
```

最后在main.py实现路由注册

```python
import fastapi
import uvicorn
from api import StuApi
app=fastapi.FastAPI()

@app.get("/")
def index():
    return {"Hello": "欢迎你访问"}
# 实现路由的注册
app.include_router(StuApi.router)


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # 启动项目
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

7.运行测试

![1776345917009](D:\class\2603\随堂笔记\第四周\AI大模型开发—18FastApi.assets\1776345917009.png)

# 2.综合实战

## 2.1 需求

实现 注册登录业务接口，包含数据库设计

## 2.2 设计



## 2.3 编码



## 2.4 测试



# 3.综合练习

3.1 实现喜欢的汽车的收藏的小功能

用户可以实现对喜欢的汽车进行：新增、修改、删除、查询、分页查询等操作



3.2 实现最爱歌曲的操作

实现歌曲的：新增、修改、删除、查询



3.3 实现用户喜欢吃什么的小系统

涉及用户表、食物表的crud操作



# 4.总结





# 5.作业

5.1 请实现一个选课系统的Api

具体涉及的数据库表，请自行设计



