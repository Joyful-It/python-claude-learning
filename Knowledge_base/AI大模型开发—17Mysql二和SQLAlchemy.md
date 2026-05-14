# AI大模型开发—17SQLAlchemy和FastApi

# 0.课程内容

## 0.1 晨考



## 0.2 课程回顾

Git:版本控制

方便进行源码管理和团队协作

Git基础操作：

git init

git add

git commit -m 

git status

git log

 git diff

git pull

git push

git clone

Git的分支：

git branch

git checkout

git merge

Git的日常操作：

项目的创建人：

创建项目

完成开发约定

完成Git仓库

创建对应分支

![1776217855736](D:\class\2603\随堂笔记\第四周\AI大模型开发—17Mysql二和SQLAlchemy.assets\1776217855736.png)

实现远程仓库和本地联系

把项目成员拉入项目组

正常开发（提交、切换、合并、推送、拉取）

项目组成员：

先克隆项目

然后创建分支

进行正常开发（提交、切换、合并、推送、拉取）



Mysql：关系型数据库，存储数据到磁盘

SQL：结构化查询语言，操作关系型数据库的

数据类型：

约束条件：

核心语句：

创建数据库：create database

删除数据库：drop database

创建数据库表：create table 

新增数据：insert into 表名

修改数据：update 表名 set

删除数据：delete from 表名

查询数据：select 字段 from 表名

SQL语言分类：

1.DDL 数据定义语言

创建、删除相关：create 、drop、alter

2.DML 数据操作语言

实现数据的修改：新增、修改、删除：insert update delete

3.DQL 数据查询语言

实现数据的查询：select

4.TPL 事务管理语言

实现事务操作



# 1.SQL进阶

## 1.1 常用各种查询

查询条件：连接条件有2个关键字：and(左右条件都满足)  or(左右条件满足一个)

```
=
>
<
!=
like
in
between   and  
order by 排序
group by 分组
having 分组后条件筛选（聚合函数）
count 计数
sum 求和
max 最大值
min 最小值
avg 平均值
```

```sql
-- 
create database db_company char set 'utf8mb4';
use db_company;
create table t_emp(
id int primary key auto_increment,
name varchar(50) not null,
sex varchar(2),
edu varchar(10),
job_date date,
job varchar(20),
create_time datetime
) comment '1.员工表';
-- 数据
insert t_emp (name,sex,edu,job,job_date,create_time) values
('王怡然','女','博士','科研员','2025-07-01',now()),
('王二龙','男','硕士','研发工程师','2024-07-01',now()),
('张铁','女','本科','研发工程师','2025-09-01',now()),
('赵沼','女','专科','科研员','2025-10-01',now()),
('单封','男','专科','行政','2025-09-08',now());

-- 查询条件
-- asc 升序 desc 降序
select * from t_emp order by job_date desc;
-- count 聚合函数 group by 分组 
select sex,count(*) as nums from t_emp 
group by sex;
-- 查询对应学历人数超过1人的学历是什么
-- having 对分组后的数据做筛选，可以跟聚合函数
select edu,count(*) as persons from t_emp group by edu having count(*)>1;
-- 聚合函数
select max(id),min(id),sum(id),avg(id) from t_emp;

```



## 1.2 多表联查

子查询：一个查询语句可以作为查询条件来使用

示例代码：

```sql
-- 查询职位人数超过1的员工信息
select * from t_emp where job in 
(select job from t_emp group by job having count(*)>1);
```

关系型数据库，表之间的数据是可以存在对应关系的

一对一：A表和B表，A中数据和B中数据存在一对一的关系  1 1

用户表和学生表 一对一

一对多和多对一：A表和B表，A中数据在B中一个对应多个，反过来就是多对一 1 n

班级表和学生表：一个班级有多个学生

多对多：A表和B表，A中的数据在B中一个对应多个，反过来也是一个对应多个 n m

课程表和学生表：一个课程有多个学生，一个学生多个课程

> 多对多需要中间表，新增一个表：学生选课表

E-R图：实体关系映射图 描述表与表之间的关系

准备建表的SQL语句：

```sql
use db_company;
-- 学生表
create table t_stu(
id int primary key auto_increment,
name varchar(20),
sex varchar(2),
gid int,
create_time datetime
);
-- 用户表
create table t_user(
id int primary key auto_increment,
username varchar(50),
password varchar(100),
sid int,
create_time datetime
);
-- 班级表
create table t_grade(
id int primary key auto_increment,
name varchar(20),
address varchar(50),
create_time datetime
);
-- 课程表
create table t_course(
id int primary key auto_increment,
name varchar(20),
teacher varchar(20),
create_time datetime
);
-- 选课表
create table t_stu_course(
id int primary key auto_increment,
sid int,
cid int,
create_time datetime
);

-- 初始化数据
insert into t_stu(name,sex,gid,create_time) values
('abc','男',1,now()),
('ww','女',1,now()),
('eee','女',2,now()),
('ttt','男',2,now()),
('uuu','男',2,now());
insert into t_user(username,password,sid,create_time) values
('qiut','123456',1,now()),
('oppo','123456',2,now()),
('word','admin',3,now()),
('tead','654321',4,now()),
('admin','123456',5,now());
insert into t_grade(name,address,create_time) values
('软件工程1班','10楼3教室',now()),
('计算机科学与技术2班','12楼3教室',now());
insert into t_course(name,teacher,create_time) values
('人工智能导论','李教授',now()),
('数据库','钱副教授',now()),
('高等数学','王讲师',now()),
('Python语言','赵讲师',now());
insert into t_stu_course(sid,cid,create_time) values
(1,1,now()),(1,2,now()),(1,3,now()),(2,1,now()),
(3,1,now()),(4,2,now()),(4,3,now()),(5,2,now()),
(5,3,now()),(5,4,now()),(3,4,now());
```

查询多表的数据，sql语句实现多表查询有以下几种方式：

1.左外连接查询 left join 

以左表为主表，右表有匹配数据就查询，没有匹配的显示为null

2.右外连接查询 right join

以右表为主表，左表有匹配数据就查询，没有匹配的显示为null

3.内连接查询 inner join

左右两表数据都需要匹配

示例代码：

```sql
-- 联表查询  内连接
select * from t_stu as s inner join t_user as u
 on s.id=u.sid ;
insert into t_stu(name,sex,gid,create_time) values
('李同学','男',1,now());
-- 左外
select * from t_stu as s left join t_user as u
 on s.id=u.sid ;
 -- 右外
select * from t_stu as s right join t_user as u
 on s.id=u.sid ;
 -- 查询 每个课程选择的人数
 select * from t_course;
 select cid,count(*) from t_stu_course group by cid;
 -- 联合查询
 select c.id,c.name,c.teacher,
 ifnull(sc.stus,0) as stus from t_course as c 
 left join
 (select cid,count(*) as stus from t_stu_course group by cid) as sc
 on c.id=sc.cid;
 insert into t_course(name,teacher,create_time) values
('前端开发','邢教授',now());
```



## 1.3 索引

索引：提高查询效率

> 命中才能提高，查询的需要使用上索引，索引生效

主键字段默认就是索引，主键索引 

分析查询语句是否使用索引：explain

新增索引：create index 索引名 on 表名(字段名)

示例代码：

```sql
 -- 查看主键索引
 -- explain 分析查询语句 查看索引是否是否使用 type字段 all未使用,const\range\ref
 explain select * from t_stu where name ='abc';
 -- 创建索引
create index i_stuname on t_stu(name); 
```

## 1.4 综合练习

要求：基于t_emp员工表完成
查询所有女员工的姓名、学历、职位
查询入职时间（job_date）在2025-09-01及之后的员工信息，按入职时间升序排序
统计每种职位的员工人数，别名字段为job_count
统计每种学历的员工人数，只保留人数 = 1 的学历
查询员工表中最高的 ID、最低的 ID、所有 ID 的平均值
查询职位人数大于 1的所有员工完整信息
查询学历为专科的员工，所在的职位有哪些（去重）
多表联查（内连接 / 左连接）
内连接查询：学生姓名、性别、对应的用户名（t_stu + t_user）
左连接查询：所有学生的姓名、班级名称（t_stu + t_grade，无用户的学生也显示）
查询所有课程名称、授课老师，以及对应的选课人数（无选课的课程显示 0）
查询每个班级的班级名称、班级地址、班级学生人数	
查询选了数据库这门课的所有学生姓名、性别、班级名称
统计男学生选择每门课程的人数
查询李教授教授的课程，有多少学生选课
给t_emp表的job字段创建普通索引，索引名i_emp_job
使用explain分析语句：select * from t_emp where job = '研发工程师'，判断是否命中索引

# 2.SQLAlchemy

## 2.1 SQLAlchemy

ORM:对象关系映射

采用面向对象的思维操作数据库（关系型数据库）

数据库：

表---类

字段--属性

行--对象

ORM库可以不用写sql语句，直接操作数据库

操作数据库的库：SqlAIchemy ORM

在Python语言中操作数据库特别简单方便

使用步骤：

1.下载

pip install pymysql sqlalchemy cryptography

> pymysql Mysql数据库的驱动库
>
> SqlAlchemy 操作数据库的库
>
> cryptography 密码库

2.导入使用

```python
import sqlalchemy

print(sqlalchemy.__version__)
```

3.验证



## 2.2 核心操作

> 先有数据库

基础的实例代码：

```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, DeclarativeBase,declarative_base

# 1.连接数据库 创建会话对象
# engine 数据库连接对象
# @ 写出 %40
# 简写的数据库连接字符串：语法格式：mysql+pymysql://账号:密码@ip地址:端口号/数据库名
engine=create_engine(
    "mysql+pymysql://root:xing%401688@127.0.0.1:3306/db_company",
    echo=True
)
# connect_url=URL(
#     drivername="pymysql",
#     host="127.0.0.1",
#     port=3306,
#     username="root",
#     password="xing@1688",
#     database="db_company"
# )
# engine = create_engine(connect_url, echo=True)
# 实例化会话工厂对象
sessionFactory = sessionmaker(bind=engine)
# 实例化 会话对象
session=sessionFactory()
# session=sessionmaker(bind=engine)
# session=session()

# 定义 模型类
# 定义 ORM 类的父类
# class Base(DeclarativeBase):
#     pass
# 定义 ORM 类的父类
Base=declarative_base()
# 表对应的类
# t_stu
class Student(Base):
    # 设置对应的表名
    __tablename__ = 't_stu'
    # 定义属性 -- 表中字段
    # primary_key 是否为主键  autoincrement 是否自增
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(50))
    sex = Column(String(2))
    gid=Column(Integer)
    create_time = Column(DateTime)

# 3.基于会话实现数据库的操作 crud
# 查询数据
# query 查询
students=session.query(Student).all()
# 遍历
for s in students:
    print(f"学员信息：{s.id},{s.name},{s.gid},{s.sex},{s.create_time}")
```

连接数据库

​	1.engine

> 数据库：ip地址 端口号 账号 密码 数据库名

创建会话

​	2.session

模型类

​	1.父类 Base

​	2.定义对应的类

> 每个表都有自己对应的类

数据新增，修改，删除

session.add

session.add_all

修改：先查询再修改对象的值

删除：先查询对象再执行session.delete()

示例代码：

```python
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker,declarative_base

# 基于SqlAlchemy实现数据的crud
# 1.数据库连接对象
engin=create_engine("mysql+pymysql://root:xing%401688@127.0.0.1:3306/db_company",echo=True)
# 2.创建会话对象
sessionFactory=sessionmaker(bind=engin)
session=sessionFactory()

# 3.根据表 写出对应的模型类
Base=declarative_base()
# 课程表 对应的类
class Course(Base):
    # 表名
    __tablename__="t_course"
    # 属性 设置对应字段信息
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(20))
    teacher=Column(String(20))
    create_time=Column(DateTime)

# 4.实现表的数据的操作 crud
def all():
    # query 查询
    courses = session.query(Course).all()
    # print(type(courses))
    for c in courses:
        # print(type(c))
        print(f'查询课程：{c.name},{c.teacher},{c.create_time}')
print("原来的数据：")
all()
# 新增
# 创建对象
c1=Course(name='Java',teacher='邱老师',create_time=datetime.now())
# 添加数据
# session.add(c1)
# 提交（新增、修改、删除） 才会真正的改变
# session.commit()
print("新增之后再查询")
all()
# 修改 先查询再修改
# 查询到对应的对象
results=session.query(Course).filter(Course.id==3).first()
print(type(results))
# 直接对修改的属性进行赋值 就是修改
results.teacher='鲍佳佳'
session.commit()
print("修改之后再查询")
all()
# 删除 先查询到再删除
session.delete(session.query(Course).filter(Course.id==6).first())
session.commit()
print("删除之后再查询")
all()
```

数据查询

session.query(要的字段)

带条件查询：

where(条件语句)

filter(单条件)

排序：order_by

分组：group_by

示例代码：

```python
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy.sql.operators import like_op

# 基于SqlAlchemy实现数据的crud
# 1.数据库连接对象
engin=create_engine("mysql+pymysql://root:xing%401688@127.0.0.1:3306/db_company",echo=True)
# 2.创建会话对象
sessionFactory=sessionmaker(bind=engin)
session=sessionFactory()

# 3.根据表 写出对应的模型类
Base=declarative_base()

class Course(Base):
    # 表名
    __tablename__="t_course"
    # 属性 设置对应字段信息
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(20))
    teacher=Column(String(20))
    create_time=Column(DateTime)
# 各种查询
r1=session.query(Course).filter(Course.name.like("%a%")).all()
for r in r1:
    print(f'{r.id},{r.name},{r.teacher},{r.create_time}')
r2=session.query(Course).filter(Course.id.between(
    1,4
)).all()
for r in r2:
    print(f'{r.id},{r.name},{r.teacher},{r.create_time}')

r3=(session.query(Course).
    filter(Course.id>3).
    filter(Course.teacher.like("%老%")).
    all())
for r in r3:
    print(f'{r.id},{r.name},{r.teacher},{r.create_time}')
# 查询指定的字段
r4=session.query(Course.id,Course.name).order_by(Course.id.desc()).limit(1,10).all()
for r in r4:
    print(f'{r.id},{r.name}')
# 获取 数量
r5=session.query(Course).count()
print(r5)
```

多表联合查询

内连接：join() 

左外连接：outerjoin()

原生SQL语句

session.execute(text(sql语句))

对于查询的结果：Query

all()

first()

one()

limit(10,20)

示例代码：

```python
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, text
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy.sql.operators import like_op

# 基于SqlAlchemy实现数据的crud
# 1.数据库连接对象
engin=create_engine("mysql+pymysql://root:xing%401688@127.0.0.1:3306/db_company",echo=True)
# 2.创建会话对象
sessionFactory=sessionmaker(bind=engin)
session=sessionFactory()

# 3.根据表 写出对应的模型类
Base=declarative_base()

class Course(Base):
    # 表名
    __tablename__="t_course"
    # 属性 设置对应字段信息
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(20))
    teacher=Column(String(20))
    create_time=Column(DateTime)

class StuCourse(Base):
    __tablename__="t_stu_course"
    id=Column(Integer,primary_key=True,autoincrement=True)
    sid=Column(Integer)
    cid=Column(Integer)
    create_time = Column(DateTime)
# 多表联合查询
# 内连接 join
# 外连接查询 outerjoin 左外
r1=(session.query(StuCourse.id.label("scid"),Course.id,Course.name,Course.teacher,StuCourse.sid).
    outerjoin(StuCourse,Course.id==StuCourse.cid).all())
for r in r1:
    print(f'{r.scid},{r.id},{r.name},{r.teacher},{r.sid}')

# 不想ORM想写SQL语句
# 执行原生sql语句
r2=session.execute(text("select * from t_course")).all()

for r in r2:
    print(r.name)
r3=session.execute(text("select * from t_course as c left join t_stu_course as sc on c.id=sc.cid")).all()
for r in r3:
    print(f'{r}---{r.id}')


# 会话关闭
session.close()
```

## 2.3 综合练习

1.场景：设计一个图书(Book)表，完成所有单表核心操作
连接 Mysql数据库，定义Book模型，字段要求：
主键id（自增）、书名title（非空）、作者author、价格price、出版社publisher、出版年份year；
创建数据库表；
新增 5 本图书数据（自定义内容）；
查询操作：
查询所有图书；
查询价格 > 50 元的图书；
查询 2020 年之后出版的图书；
修改操作：将第一本图书的价格修改为 69.9 元；
删除操作：删除价格 < 30 元的图书；
提交所有事务。



# 3.综合练习

1.场景：设计作者(Author) + 图书(Book) 一对多关系（一个作者写多本书）
定义模型：
作者表：id、name（姓名）、country（国家）；
图书表：id、title、price、author_id（外键关联作者）；
建立relationship关联关系；
新增 2 个作者，每个作者对应 2 本图书；
多表查询：
查询「中国」作者的所有图书；
查询某本图书对应的作者信息；
统计每个作者的图书数量；
联合条件查询：查询美国作者、价格 > 40 元的图书名称和作者姓名。

2.场景：简易电商商品管理系统，涉及三张表：分类(Category)、商品(Product)、库存(Stock)（一对多 + 一对一）
模型设计：
分类表（Category）：id、c_name（分类名，如：电子产品、服装）；
商品表（Product）：id、p_name（商品名）、price、cate_id（外键→分类）；
库存表（Stock）：id、num（库存数量）、product_id（外键→商品，一对一）；
核心要求：
建立表关系：分类 ←一对多→ 商品 ←一对一→ 库存；
新增数据：2 个分类，每个分类 3 个商品，每个商品对应 1 条库存；
复杂查询：
查询「电子产品」分类下所有商品的名称、价格、库存数量；
查询库存数量 < 10 的所有商品及所属分类；
数据维护：
将所有商品价格涨价 10%；
删除库存为 0 的商品。



# 4.总结

sql 各种查询，联合查询，索引

Sqlalchemy python语言中操作数据库的库 ORM的一种

engine 数据库连接对象

session 会话对象（操作数据的对象）

Base 模型类的父类

表---类--

数据的操作：crud

新增

修改

删除

查询（各种条件查询，联合查询，排序和分组或分页）



# 5.作业

SQLAlchemy 综合实战（教务管理系统）
业务场景
设计一个学校教务管理系统，包含 教师表、课程表、学生表、成绩表 四张表，表关系：
一对多：1 个教师可以教多门课程，1 门课程只属于 1 个教师
多对多：1 个学生可以选多门课程，1 门课程可以被多个学生选（通过成绩表关联）
题目要求
使用 SQLAlchemy 连接Mysql数据库（文件名为school.db）；
初始化引擎、基类、数据库会话。

严格按照以下字段和关系定义 4 个模型类，必须配置外键和relationship 关联：
教师表 (teacher)
id：主键，自增
name：教师姓名，非空
subject：授课科目（如：数学、英语）
age：教师年龄
课程表 (course)
id：主键，自增
course_name：课程名称（如：高等数学、大学英语），非空
credit：学分（整数）
teacher_id：外键 → 教师表 id（一对多关联）
学生表 (student)
id：主键，自增
name：学生姓名，非空
age：学生年龄
gender：性别
成绩表 (score)（学生 & 课程的中间表，多对多关联）
id：主键，自增
student_id：外键 → 学生表 id
course_id：外键 → 课程表 id
score：考试成绩（浮点数）
约束：同一个学生不能重复选同一门课程

执行代码，自动创建所有 4 张表；
批量新增数据（必须提交事务）：
新增 2 名教师；
为每个教师新增 2 门课程；
新增 4 名学生；
为每个学生选择 2 门课程，添加对应的成绩。

单表查询：查询所有年龄大于 30 岁的教师；
一对多查询：查询「数学」科目教师所教的所有课程；
多对多联合查询：查询学生「张三」所选的所有课程名称、学分、对应教师姓名；
条件联合查询：查询成绩大于 80 分的所有学生姓名、课程名、成绩；
统计查询：统计每一门课程的平均分，并按平均分降序排列；
分组查询：统计每个教师教授的课程数量。

