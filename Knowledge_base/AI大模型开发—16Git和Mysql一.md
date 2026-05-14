# AI大模型开发—16Git和Mysql

# 0.课程内容

## 0.1 晨考

https://ks.wjx.com/vm/rzgUP6z.aspx# 

## 0.2 课程回顾

数据分析的三剑客：数据计算--数据处理--数据可视化--机器学习

数据计算：numpy 一维（向量）和二维数组（矩阵） 广播机制和矢量化运算 常用属性 核心函数

数据处理：pandas 一维和二维数据对象 常用属性 核心函数（二维数据对象）

数据可视化：matplotlib和seaborn 绘制各种图表（折线图、柱状图、饼图、散点图等等）



一阶段：

Python语言掌握

数据分析库

全栈开发（工程化）



# 1.Git

## 1.1 git

git：版本控制软件

分布式

> 开发中为什么需要版本控制软件：
>
> 1.团队开发，源码共享的问题、源码管理
>
> 2.日常需求变更，每一版本的源码管理
>
> 3.上线部署的源码隔离，分支管理
>
> ……
>
> 哪怕团队只有1个人，也需要使用版本控制软件

版本控制软件：

1.svn（服务端和客户端）

2.git（没有服务端）

目前主流都是使用的git

git:分布式版本控制系统

git的安装：

**1.下载git**

https://git-scm.com/

![1776131388448](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776131388448.png)

**2.双击安装**

双击安装包，一路下一步，即可安装成功

**3.验证安装是否成功**

打开cmd 输入以下命令：

git --version

![1776131448812](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776131448812.png)

**4.完成初始化**

> 第一次安装git需要进行初始化配置
>
> 配置用户名和邮箱

按照要求输入以下命令：

```bash
# 设置你的名字和邮箱（每次提交都会记录）
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"
# 设置默认分支名为main（新标准）
git config --global init.defaultBranch main
# 查看配置
git config --list
```

> 请替换为自己的名字（英文）、替换为自己的邮箱

![1776131662204](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776131662204.png)

**5.实现远程仓库初始化配置**

> 远程仓库的目的：多人协作开发，在远程备份源代码
>
> Git主流的远程仓库：
>
> 1.Github-全球化的开源项目的集合
>
> 2.Gitee-国产远程仓库
>
> 3.GitLab-企业私服，搭建在企业自有的服务器上，供公司内部使用
>
> 4.GitCode-国产远程仓库，Github克隆

选择gitee为例：把gitee作为git的远程仓库

a.注册账号 gitee

https://gitee.com/

![1776132156796](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776132156796.png)

b.本机生成ssh秘钥

在cmd中执行下面的命令：

ssh-keygen -t ed25519 -C "xingfei_work@163.com"

> 注意：要把邮箱换成你自己的

注意如果在cmd执行报：命令不存在，就在下面输入

桌面右键-![1776135578655](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776135578655.png)

然后在执行上面的命令即可生成SSH公钥

![1776135619921](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776135619921.png)

![1776132268122](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776132268122.png)

c.远程仓库配置SSH秘钥

登录gitee，账号设置，SSH公钥

把上一步生成的公钥（id_xxx.pub）新增到gitee

![1776132390470](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776132390470.png)

![1776132418643](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776132418643.png)

## 1.2 git操作流程

**1.git的基本操作**

> 新建一个Python项目，通过git的基本操作，管理源代码

git init 初始化git管理，生成隐藏文件夹.git

git status 查看git的状态 未加入git管理的：红色，已加入但是未提交的：绿色

git add 文件名 把变化的文件加入到git的管理（暂存区）

git commit -m '提交日志信息'

git log 查看提交日志

> 各个命令怎么使用，有什么作用

![1776133272266](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776133272266.png)

git diff 查看对比，有没有修改

.gitignore文件 设置哪些内容不被git管理

> 一般 .xx文件夹，私有内容 都会被排除
>
> 创建项目之后就先创建对应的忽略文件配置 
>
> 参考的排除内容：.gitignore文件
>
> ```
> # .gitignore
> # Python相关
> __pycache__/
> *.py[cod]
> *.egg-info/
> dist/
> build/
> *.egg
> # 虚拟环境
> venv/
> .venv/
> env/
> # IDE相关
> .vscode/
> .idea/
> *.swp
> *.swo
> # 环境变量（重要！不要把密码提交到Git）
> .env
> .env.local
> # 操作系统文件
> .DS_Store
> Thumbs.db
> # 数据库文件
> *.db
> *.sqlite3
> # 日志文件
> *.log
> logs/
> ```

git reset --hard '提交id'  回滚源码到指定的提交

> 源码就回到原来的版本上
>
> 通过git log 查看提交的日志（包含提交id）

**2.IDE中操作git**

写项目，本地创建项目，设置忽略配置文件

和远程仓库建立联系

再把其他人拉到仓库中

这样其他人就可以共享仓库（源码）

提交

拉取

推送

切换-分支

合并-(分支|他人代码）

第一步：

创建项目

第二步：

IDE--vcs--创建git仓库

![1776138380623](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776138380623.png)

第三步：

创建 .gitignore文件

弹出一个窗口：询问是否 把文件添加到仓库，记得勾选左下角：不再询问

> 后续就不需要执行 git add 命令，会自动添加

第四步：

提交操作

![1776138698840](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776138698840.png)

记得填写 提交日志，没问题 就点击 提交

第五步：

推送代码到远程仓库

![1776138853257](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776138853257.png)

先定义远程，在对应的远程仓库，新建仓库（名字和项目名一致）

访问gitee-新建仓库-填写仓库信息

![1776138941017](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776138941017.png)

![1776138972406](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776138972406.png)

有了远程仓库的地址：https://gitee.com/coderferi/aistudy1601.git

再回到IDE填写远程仓库的地址

![1776139031801](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776139031801.png)

![1776139056230](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776139056230.png)

![1776139087216](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776139087216.png)

![1776139131738](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776139131738.png)

第六步：

远程仓库添加项目成员

![1776139260295](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776139260295.png)

仓库链接：https://gitee.com/coderferi/aistudy1601/invite_link?invite=3a8933c75d32ec429c583cb9853c5b3f4d2a0aa41ce72bd2a51e94016c61e1f7408a02ed317f32915f318cd36bbddc3a

> 加入成功，每个成员都可以在自己的gitee上看到项目

第七步：

克隆项目

> 项目组其他成员需要克隆项目获取源码
>
> 可以安装gitee插件

![1776139480371](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776139480371.png)

PyCharm设置--插件--搜索gitee--点击安装

再点击文件--来自版本控制--选择gitee--点击gitee授权登录

然后就可以看到所有的项目选择即可点击 克隆

等待导入即可



第八步：

日常开发

提交

拉取

推送

切换

合并

3.**分支**

分支：隔离，每个分支都是独立的，分支之间隔离的

> 实际开发中，多分支，处理不同的场景
>
> 公司的分支：上线、开发、bug、测试、新特性
>
> 个人的分支：日常开发、开发、测试……

Git中分支管理：

0.查看分支：git branch 

1.新建分支 ：git branch 分支名

2.切换分支：git checkout 分支名

3.合并分支：git merge 分支名1 分支名2   把分支名2合并到分支名1上面

> 合并出现了冲突，对同一个文件本地的操作和另外分支的也操作，出现冲突，同一个文件都出现了改变，合并的时候不知道用谁的，一般需要手动解决（要么选择当前分支文件的内容，要么选择另外分支的文件内容，要么手动更改冲突内容）

4.删除分支：谨慎操作

默认的主分支：main/master

> 命令操作也行，也可以之间选择在PyCharm中点击完成操作-推荐

010 62332452

开发中都是采用多分支进行开发

0-1的项目的分支：

main 主分支-受保护--打版本号

develop 开发分支--研发团队正常版本迭代的分支

个人分支：

姓名拼音-develop 个人日常开发分支

姓名拼音-test 个人日常开发分支

每天工作流程：

晨会

拉取代码

日常开发

推送代码

日报

> 务必在推拉之前先提交代码
>
> 开发一定是并行的
>
> Git一定要玩废几个仓库

# 2.Mysql

数据库：存储数据的仓库

专门用来存储数据的

分类：

1.关系型数据库

数据之间有关联关系

典型代表：Sqlite、Mysql、Oracle、Sql Server、Db2、H2、达梦、人大金仓、TiDB

2.非关系型数据库

典型代表：

nosql-Not Only SQL ，典型代表：Redis MongoDB Neo4j 

向量数据库

文件存储数据的问题：

Excel、csv、json

效率 数据量 



## 2.1 Mysql

Mysql数据库，开源免费，目前使用最为广泛

Mysql的版本：5.7 8.x 9.x

Mysql数据库：存储数据到磁盘上



## 2.2 Mysql安装

Mysql数据库的安装

1.下载

2.双击安装

> 常见问题：
>
> 1.3306端口被占用（检查是否安装过mysql）
>
> 2.路径有特殊字符（包含中文）
>
> 3.电脑的用户名有中文或特殊字符
>
> 4.权限的问题

3.校验是否安装成功

![1776154102507](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776154102507.png)



Mysql可视化工具的安装

1.下载

2.双击安装

3.打开软件

> 数据库的可视化工具有很多种，不限制使用哪一种：
>
> 1.Mysql WorkBeanch 
>
> 2.Navicat
>
> 3.sqlyoung

![1776154337169](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776154337169.png)

> 数据库：本机
>
> ip：127.0.0.1
>
> 端口号：3306
>
> 账号：root
>
> 密码：   安装的时候自己设置的密码

如果要连接别人或服务器数据库

ip地址需要换成别人的或服务器ip地址

同时 root账号的Host字段值得是 % ，默认是localhost



127.0.0.1 或 localhost 都是表示 本机

## 2.3 SQL

Mysql是数据库，存储数据的

使用SQL语言操作数据库，实现数据的管理：新增、修改、删除、查询

SQL:结构化查询语言，专门操作关系型数据库

Mysql数据库内部对数据的管理：

1.数据库-database

2.表-table

3.字段

4.数据



使用Mysql:

1.先创建数据库

语法格式：

```sql
create database 数据库名 char set 'utf8mb4';
use 数据库名;
```

2.再创建表

语法格式：

```sql
create table 表名(字段名 数据类型 约束条件,……)
```

> Mysql数据库支持的数据类型：
>
> 整型：int
>
> 浮点型：float
>
> 字符串：varchar(长度)、text
>
> 日期：datetime
>
> Mysql数据库支持的约束条件：
>
> 主键约束：每个表都需要有主键，并且主键唯一 非null,建议使用int类型作为主键 语法：primary key
>
> 默认值约束：给字段设置默认值，语法：default 默认值
>
> 唯一约束：字段的值唯一，不可重复 语法：unique
>
> 非空约束：字段的值必须写，不能为null 语法： not null
>
> 外键约束：某表的主键作为当前表的字段，一般需要外键约束 语法：foreign key
>
> 自增约束：只能用在主键上(整型)，就不需要给其赋值，自动赋值。语法：auto_increment

3.操作数据

> 数据的：新增、修改、删除、查询

新增数据的语法格式：

```sql
insert into 表名(字段名,……) values(值,……),……;
```

修改数据的语法格式：

```sql
update 表名 set 字段名=值,…… where 条件
```

删除数据的语法格式：

```sql
delete from 表名 where 条件
```

查询数据的语法格式：

```sql
select 字段名,…… from 表名 where 条件
```

> 其中可以用* 表示所有的字段名，如果写的是*那么就查询这个表所有字段的值

常用的条件：

```
=
<
>
>=
<=
!=
between xxx and xx   
like xx
in (xx,xx,……)
```

where id between 1 and 3 ==> id的值在1和3之间 [1,3]

where name like '王%'  ===>查询name的值 王开头的所有数据

where age in (18,33,40) ===>age的值属于 这些值：18,33,40

基础操作示例代码：

```sql
# 创建数据库
# 创建数据库 语法格式 
create database db_study char set 'utf8mb4' ;
# 使用数据库 
use db_study;
# 创建表 语法格式
create table t_user(id int ,username varchar(50),password varchar(500));
# 新增数据
insert into t_user(id,username,password) values(1,'admin','123456');
# 查询数据
select * from t_user;
# 新增数据 新增多条数据
insert into t_user(id,username,password) values
(2,'admin2','2123456'),(3,'admin3','3123456'),(4,'admin4','4123456');

# 创建表
create table t_student(id int primary key,name varchar(20) not null,sex int);

```

Mysql Workbeanch默认开启安全模式

![1776157804062](D:\class\2603\随堂笔记\第四周\AI大模型开发—16Git和Mysql一.assets\1776157804062.png)

常用的基础操作的实例代码：

```sql
-- 数据库
-- 创建数据库
create database db_test char set 'utf8mb4';
-- 切换数据库 选中对应的数据库
use db_test;

-- 创建表
create table t_person(id int primary key auto_increment,name varchar(20) not null,sex varchar(2),edu varchar(20));

-- 新增数据
-- 新增一条
insert into t_person(name,sex,edu) values('张三','男','专科');
-- 新增多条数据
insert into t_person(name,sex,edu) values  
('李四','女','专科'),('貂蝉','男','高中'),('唯一','男','本科'),('码字','男','专科');

-- 查询数据
select id,name,sex,edu from t_person;
select * from t_person;
-- 查询数据 带条件
select * from t_person where sex='女';
-- 多个条件 同时满足就用 and ，只需满足一个 就用 or
select * from t_person where id between 2 and 5 and sex='男';
-- 查询姓李
select * from t_person where name like '李%';
-- 查询姓名中有一的人
select * from t_person where name like '%一%';
-- 修改数据
update t_person set sex='女' where name='貂蝉';
-- 删除数据
delete from t_person where name='码字';

-- 表不想要了
drop table t_person;
-- 数据库不想要了
drop database db_test;

```



## 2.4 综合练习

创建学生表（字段自己决定，需要涵盖下面的练习内容），完成一下的练习：

1. 查询所有学生的全部信息
2. 查询所有学生的姓名、年龄、分数
3. 查询姓名叫 张三 的学生所有信息
4. 查询性别为 女 的学生姓名和分数
5. 查询分数 不等于 80 分 的学生信息
6. 查询年龄 等于 18 岁 的学生
7. 第 3 部分：比较查询 > < >= <=
8. 查询分数 大于 80 分 的学生
9. 查询年龄 小于 18 岁 的学生
10. 查询分数 大于等于 90 分 的学生
11. 查询年龄 大于 19 岁 的学生姓名和性别
12. 查询分数在 70 ~ 90 分之间 的学生
13. 查询年龄在 18 ~ 20 岁之间 的学生
14. 查询姓名是 张三、李四、王五 的学生
15. 查询分数是 88.5、92.0、95.0 的学生
16. 查询姓名以 “张” 开头的学生
17. 查询姓名以 “六” 结尾的学生
18. 查询姓名中 包含 “七” 的学生
19. 查询手机号以 138 开头的学生
20. 查询 性别为女 且 分数大于 80 的学生
21. 查询 年龄大于 18 且 性别为男 的学生
22. 查询 分数小于 60 或 分数大于 90 的学生
23. 查询 18 岁 或者 20 岁 的学生
24. 查询 性别男 且 年龄 18 岁 且 分数大于 85 的学生
25. 删除姓名为 周八 的学生
26. 修改 张三 的分数为 90.0
27. 修改所有 性别为女 的学生年龄加 1
28. 删除分数 小于 60 分 的学生

刷题：https://www.nowcoder.com/exam/oj?page=1&tab=SQL%E7%AF%87&topicId=199

# 3.综合练习

自己设计并创建书籍表，然后完成以下的操作：

查询所有图书的名称、价格、作者、上架时间
查询价格大于 50 元的图书全部信息
查询库存等于 10 且 分类为计算机 的图书
查询价格在 30~80 元之间 的图书
查询作者是鲁迅、张三 的图书（in 查询）
查询图书名称包含编程 的图书（like 查询）
查询价格小于 20 或 库存小于 5 的图书
查询图书编码以BK开头 的图书
将Java编程这本书的价格修改为 69.9
将所有文学类图书的库存加 5
删除价格小于 20 元的图书
删除作者为未知的图书



# 4.总结

1.git 版本控制软件

管理源代码，团队协作开发

git操作

git的分支

 提交改变--commit

拉取代码--pull

推送代码--push

切换分支--checkout

合并分支--merge

可以基于Git+远程仓库 实现团队项目开发（拉取和推送和合并）

远程仓库：选择 gitee(码云)

2.mysql

mysql 关系型数据库，持久化存储数据的，数据存储到磁盘上

mysql安装

mysql的操作：sql 结构化查询语言，专门操作关系型数据库

mysql的数据类型：整型 浮点型 字符串 日期

mysql常用的约束条件：6种（主键、非空、默认值、唯一、外键、自增）

sql的语法格式：

创建数据库：create database xxx

使用数据库：use xxx

创建数据库表：create table xxx

新增数据：insert into xxx

删除数据：delete from xxx

修改数据：update xxx

查询数据：select * from xxx

常用的基础条件：= 、> 、< 、!= 、and 、or 、in 、like 、between and 

# 5.作业

## 1.全程使用 Git 命令行 / IDEA 图形化 操作均可

必须完成分支、提交、拉取、推送、合并全流程，提交到自己的 Gitee 仓库。
注册 Gitee 账号，新建一个远程仓库（命名：git-homework）
将远程仓库克隆到本地
在本地创建一个新分支 dev，并切换到该分支
在分支中创建一个 test.txt 文件，写入任意内容，执行提交 (commit)
将 dev 分支的代码 ** 推送 (push)** 到 Gitee 远程仓库
切换回主分支 main/master，将 dev 分支 ** 合并 (merge)** 到主分支
将主分支的代码 ** 推送 (push)** 到 Gitee，完成团队协作流程

## 2.MySQL 编程作业

创建数据库、创建表（必须用到你学的：6 大约束 + 4 种数据类型）
插入测试数据
完成所有增删改查编程题
所有题目必须编写完整的 SQL 语句
步骤 1：基础建库建表（必做）
编写 SQL，创建员工管理库和员工表，严格使用你学的约束和数据类型：
库名：company
表名：employee
字段要求：
员工编号 (id)：整型，主键、自增
姓名 (name)：字符串，非空
年龄 (age)：整型
性别 (gender)：字符串，默认值：男
手机号 (phone)：字符串，唯一
工资 (salary)：浮点型
入职时间 (entry_time)：日期类型
步骤 2：SQL 编程题目（编写语句即可）
向employee表中插入 5 条员工测试数据（自定义内容）
查询所有员工的全部信息
查询所有员工的姓名、工资、入职时间
查询姓名为张三的员工所有信息
查询工资大于 5000的员工姓名和工资
查询年龄不等于 25的员工
四、范围查询（between and）
查询工资在 3000~8000 之间的员工
查询年龄在 20~30 之间的员工
查询姓名是张三、李四、王五的员工
查询工资是4500、6000、8000的员工
查询姓名以张开头的员工
查询手机号以138开头的员工
查询性别为女 且 工资大于 6000的员工
查询年龄大于 30 或 工资小于 4000的员工
将张三的工资修改为7000
将所有男性员工的年龄加 1
删除姓名为赵六的员工
删除工资小于 3000 的员工

