# AI大模型开发—19FastApi进阶和前端Html

# 0.课程内容

## 0.1 晨考



## 0.2 课程回顾

Mysql 关系型数据库

SQL 结构化查询语言，操作关系型数据库

核心：

1.数据类型-对应数据库

整型、浮点型、字符串、日期

2.约束条件

主键、外键、自增、默认、非空、唯一

3.创建数据库

create database 数据库名 char set 'utf8mb4'

drop database 数据库名

4.创建表

create table 表名 (字段名 数据类型 约束条件,……)

5.删除表

drop table 表名

6.新增数据

insert into 表名(字段名,……)  values(值,……)

7.修改数据

update 表名 set 字段名=值 where 条件

8.删除数据

delete from 表名 where 条件

9.查询数据

select * from 表名 where 条件

> and or
>
> like
>
> between and
>
> in
>
> 聚合函数
>
> order by
>
> group by
>
> having

内连接：inner join

左外连接:left join

子查询

索引 explain



SqlAlchemy ORM 操作数据库

表--类

字段--属性

行--对象

连接数据库

创建会话

模型类--Base

数据操作：crud



FastApi 开发后端Api接口的库，性能卓越



应用 @app

路由 @router



支持多种请求方式：get post put delete

参数形式有3种：query查询参数-键值对、路径传参-{参数名}、请求体-json

> json数据交互，必须继承BaseModel



# 1.fastApi进阶

## 1.1 Pydantic数据验证

Pydantic是主流的Python语言的数据格式验证库，fastapi内置

核心作用：

1. **自动解析**：前端传的 JSON / 表单 / 路径参数 → 自动转为 Python 对象
2. **强制验证**：类型错误、格式错误、数值越界 → 直接返回标准化错误
3. **智能序列化**：数据库对象 / 复杂数据 → 自动转为安全的 JSON 响应
4. **自动文档**：基于模型生成 OpenAPI 文档，无需手写注释

> Field

示例代码：

```python
# 路由
import random
import fastapi
from pydantic import BaseModel, Field

# 创建路由对象
router = fastapi.APIRouter(prefix="/user",tags=["user"])

# 接口 输入你的姓名和年龄 自己写校验
@router.get("/luck")
def luck(name:str,age:int):
    # 参数校验
    if 1<age<100:
        if len(name.strip())>0:
            # 掐住一算 你的幸运数字
            return {"name":name,"age":age,"num":random.randint(1,10)}
    # 参数异常
    return {'error':'亲，请输入合法的姓名或年龄！'}

# 使用 Pydantic
class UserParam(BaseModel):
    name: str=Field(min_length=1,max_length=10,description='请输入合法的姓名')
    age: int=Field(gt=1,lt=100,description='请输入合法的年龄')
# 定义接口 自动化参数校验
@router.post("/luck2")
def luck2(user:UserParam):
    return {"name":user.name,"age":user.age,"num":random.randint(1,10)}
```

https://gitee.com/coderferi/aistudy19

## 1.2 依赖注入

Depends：实现FastApi中的依赖注入

可以把公共的操作封装成函数，通过Depends实现注入，这样多个Api接口就可以复用

比如数据库的会话

参考示例：

```python
import datetime

from fastapi import APIRouter,Depends
from pydantic import BaseModel,Field
from sqlalchemy.orm import session

from schemas.datamodel import Emp
from schemas.dbutil import sessionLocal

router=APIRouter(prefix="/emp",tags=["emp"])
# 需要依赖注入的函数
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

# 接口层的类  封装参数
class EmpAdd(BaseModel):
    name: str=Field(min_length=2,max_length=20)
    age: int=Field(ge=12,le=20)
    job: str=Field(min_length=2,max_length=20)
class EmpData(EmpAdd):
    id:int
    # name:str
    # age:int
    # job:str
    create_time:datetime.datetime
# 新增
@router.post("/add")
def add(obj:EmpAdd,db:session=Depends(get_db)):
    # 类型转换
    emp=Emp(name=obj.name,age=obj.age,job=obj.job)
    try:
        db.add(emp)
        db.commit()
        return {"code": 0, "msg": "ok"}
    except Exception as e:
        return {"code": 1, "msg": e}
# 查询
@router.get("/all")
def all_emp(db:session=Depends(get_db)):
    emps=db.query(Emp).all()
    # arr=[EmpData.model_validate(e for e in emps)]
    arr=[]
    for emp in emps:
        arr.append((EmpData(id=emp.id,name=emp.name,age=emp.age,job=emp.job,create_time=emp.create_time)))
    return arr
```

> 全部代码请参考gitee仓库

![1776655763100](D:\class\2603\随堂笔记\第四周\AI大模型开发—19前端和AI-DD.assets\1776655763100.png)

## 1.3 异步支持

同步：排队，同一时间只能执行一个，按顺序进行

异步：同时，多个任务可以同时执行，不用相互等待

FastApi支持同步，也支持异步

异步接口的函数采用async修饰

异步函数内部如果想让某个异步函数的调用变为同步函数，那么需要在函数调用前使用await修饰

```python
import datetime

from fastapi import APIRouter

router=APIRouter(prefix="/test",tags=["test"])
# 异步函数 异步接口
# async 修饰函数
@router.get("/test")
async def test():
    return {"now":datetime.datetime.now()}
```

## 1.4 文件上传

FastApi支持文件上传，内置：UploadFile

实现文件上传的步骤：

1.下载

pip install mulitpart

2.定义Api接口实现

```python
from pathlib import Path
import fastapi
from fastapi import UploadFile
from fastapi.params import File

router=fastapi.APIRouter(prefix="/file",tags=["file"])

# 保存内容的路径
DIR_PATH=Path('uploads')
DIR_PATH.mkdir(parents=True,exist_ok=True)

# 文件上传接口
@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    # 读取文件内容
    data=await file.read()
    # 把内容写出到指定路径
    file_path=f'{DIR_PATH}/{file.filename}'
    # 写出到文件中 模式：wb 任意文件类型
    with open(file_path,'wb') as f:
        f.write(data)
    return { "success": True,"file": file_path}
# 上传多个文件
@router.post("/uploads")
async def uploads(files: list[UploadFile] = File(...)):
    for file in files:
        # 读取文件内容
        data = await file.read()
        # 把内容写出到指定路径
        file_path = f'{DIR_PATH}/{file.filename}'
        # 写出到文件中 模式：wb 任意文件类型
        with open(file_path, 'wb') as f:
            f.write(data)
    return {"success": True,"files": len(files)}
```

3.测试

![1776667618702](D:\class\2603\随堂笔记\第四周\AI大模型开发—19前端和AI-DD.assets\1776667618702.png)



# 2.前端

## 2.1 html

 Html:超文本标记语言

主要用来显示内容，可以通过浏览器访问

html的标签是固定的

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
<!--    title 设置网页的标题内容-->
    <title>网页标题</title>
</head>
<body>
<!--    h1-h6 标题标签  加粗加大-->
    <h1>我是标题1</h1>
    <h6>我是标题6</h6>
<!--label文本标签-->
    <label>文本标签</label>
<!--分块标签-->
    <div>
<!--        输入框-->
        <input placeholder="请输入姓名"> <br/>
<!--        单选框-->
        <label>性别：</label><input type="radio" name="sex">男 <input type="radio" name="sex">女<br/>
<!--      type="checkbox"  多选框-->
        <label>爱好：</label><input type="checkbox">电竞 <input type="checkbox">二次元 <br/>
<!--       select 下拉框-->
        <label>家乡：</label>
        <select>
<!--            option 作用在select下拉框 设置选项内容-->
            <option>北京</option>
            <option>东京</option>
            <option>南京</option>
            <option>河南</option>
        </select>
    </div>
    <div>
        密码框：<input type="password">
    </div>
    <div>
        <button>按钮</button>
    </div>
    <div>
<!--        table 标签 表格-->
        <table border="1">
<!--            表头-->
            <thead>
<!--            tr 行-->
                <tr>
<!--                    th 列 内部内容 加粗-->
                    <th>序号</th>
                    <th>姓名</th>
                    <th>性别</th>
                    <th>年龄</th>
                </tr>
            </thead>
            <tbody>
                <tr>
<!--                    td 列 -->
                    <td>1</td>
                    <td>张三</td>
                    <td>男</td>
                    <td>18</td>
                </tr>
             <tr>
                    <td>1</td>
                    <td>张三</td>
                    <td>男</td>
                    <td>18</td>
                </tr> <tr>
                    <td>1</td>
                    <td>张三</td>
                    <td>男</td>
                    <td>18</td>
                </tr>
            </tbody>
        </table>
    </div>
<div>
<!--    img 标签 图片-->
    <img src="imgs/s1.png"/>
</div>
</body>
</html>
```

![1776669998875](D:\class\2603\随堂笔记\第四周\AI大模型开发—19前端和AI-DD.assets\1776669998875.png)

> html页面想要在fastapi项目中使用，需要在app中配置
>
> ```python
> # fastapi 挂载静态页面
> app.mount("/front", StaticFiles(directory="front"), name="front")
> ```
>
> front 不固定，根据你的前端所在目录



# 3.综合练习

基于SqlAIchemy+FastApi实现一个用户喜欢的歌曲小项目

## 3.1 需求

需求：实现一个记录用户喜欢的歌曲

要求：

用户可以注册、登录、个人信息

用户登录之后可以进行喜欢歌曲的：新增、删除、修改、查询



## 3.2 分析

> 分析需求：目的为了明确需求究竟是要干什么

用户模块：新增、查询

歌曲模块：新增、修改、删除、查询



## 3.3 设计

数据库：存储用户信息、歌曲信息

sql脚本：

```sql
create database db_song char set 'utf8mb4';
use db_song;
create table t_user(id integer primary key auto_increment,nickname varchar(50),password varchar(500),create_time datetime);
create table t_song(id integer primary key auto_increment,uid integer,name varchar(50),author varchar(50),score integer,info varchar(50),create_time datetime);
```

> sqlalchemy 操作数据库
>
> t_user--->User
>
> t_song--->Song



Api接口--FastApi

app+router的形式进行开发，分模块，降低耦合性

用户模块 路由中提供Api接口：

注册用户

登录接口

查询用户信息



歌曲模块 路由中提供Api接口：

新增歌曲

修改歌曲

删除歌曲

查询歌曲-全部



## 3.4 编码

1.创建项目

2.下载依赖

pip install pymysql sqlalchemy cryptography fastapi uvicorn

3.完成初始化配置

​	git忽略文件

​	main.py

​	分层的包

4.完成git初始化

​	git仓库初始化

​	git提交

​	git远程仓库分享

![1776672810414](D:\class\2603\随堂笔记\第四周\AI大模型开发—19前端和AI-DD.assets\1776672810414.png)

![1776672859158](D:\class\2603\随堂笔记\第四周\AI大模型开发—19前端和AI-DD.assets\1776672859158.png)

操作成功：https://gitee.com/coderferi/aistudy191

5.配置路由的Api接口

> 采用FastApi的路由模式进行分模块开发
>
> router 路由 
>
> 使用步骤：
>
> 1.在对应模块中，实现如下的代码
>
> ```python
> # APIRouter 创建路由对象
> # 参数说明：1.prefix 接口前缀 2.tags 接口加标签（分组）
> router = APIRouter(prefix="/user", tags=["user"])
> ```
>
> 2.在main.py（入口模块、启动模块）
>
> ```python
> import fastapi
> import uvicorn
> from app import userapi,songapi
> app = fastapi.FastAPI()
> 
> # 配置路由
> app.include_router(userapi.router)
> app.include_router(songapi.router)
> 
> if __name__ == "__main__":
>     uvicorn.run(app, host="127.0.0.1", port=8000,reload=True)
> ```

6.实现数据库操作

​	数据库连接相关模块

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 数据库连接配置
# 连接
engine=create_engine('mysql+pymysql://root:xing%401688@127.0.0.1:3306/db_song',echo=True)
# 会话工厂
sessionLocal=sessionmaker(bind=engine)
```

​	ORM相关的模型类

```Python
import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
# 数据库操作 的模型类的父类
Base = declarative_base()

class User(Base):
    __tablename__ = "t_user"
    id = Column(Integer, primary_key=True,autoincrement=True)
    nickname = Column(String)
    password = Column(String)
    create_time = Column(DateTime,default=datetime.datetime.now)

class Song(Base):
    __tablename__ = "t_song"
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String)
    author = Column(String)
    uid=Column(Integer)
    score=Column(Integer)
    info = Column(String)
    create_time = Column(DateTime,default=datetime.datetime.now)
```

7.基于FastApi实现Api接口

用户模块的实现

示例代码：

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import session
from app.apimodels import R, UserData
from database.dbmodels import User
from database.dbutil import sessionLocal

# APIRouter 创建路由对象
# 参数说明：1.prefix 接口前缀 2.tags 接口加标签（分组）
router = APIRouter(prefix="/user", tags=["user"])

# 封装函数 让FastApi依赖注入
def get_db():
    db=sessionLocal()
    try:
        yield db
    except Exception:
        db.close()
# 注册
@router.get("/register")
async def add(name:str,password:str,db:session=Depends(get_db)):
    # 创建 数据库 模型类对象
    user=User(nickname=name,password=password)
    # 操作数据库 实现新增
    db.add(user)
    db.commit()
    return R(code=0,msg='ok',data='成功')

# 登录
@router.get("/login")
async def login(name:str,password:str,db=Depends(get_db)):
    # 查询数据库
    user=db.query(User).where(User.nickname==name).first()
    print(user)
    if user is not None: # 查询到了用户
        if user.password==password:
            # 登录成功
            return R(code=0,msg='ok',data=user.id)

    return R(code=1,msg='error',data="亲，账号或密码错误！")

# 查询个人信息
@router.get("/info")
async def info(id:int,db=Depends(get_db)):
    user=db.query(User).where(User.id==id).first()
    if user is not None:
        ud=UserData(id=user.id,nickname=user.nickname,password=user.password,create_time=user.create_time)
        return R(code=0,msg='ok',data=ud)
    else:
        return R(code=1,msg="error",data='亲，请检查用户ID')
```



## 3.5 测试

自测

> 一般一个模块结束，就可以进行测试

http://127.0.0.1:8000/docs#/

![1776677014715](D:\class\2603\随堂笔记\第四周\AI大模型开发—19前端和AI-DD.assets\1776677014715.png)

# 4.总结

FastApi：开发Api接口的库

简单好用

基于Pydantic的参数校验

依赖注入Depends

异步接口-asyncs ,await

文件上传：UploadFile

前端-Html 显示内容（通过各种固定的标签）

FastApi和SqlAlchemy的综合练习

> 今日务必 消化并理解 综合练习-用户模块



# 5.作业

## 5.1 完善歌曲模块



## 5.2 实现**书籍收藏管理系统**





