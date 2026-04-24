# 学习会话记录 - 2026-04-21

## 会话概览
- 日期：2026-04-21
- 形式：一对一教学
- 核心主题：前端三件套（HTML/CSS/JS）+ FastAPI项目代码复习

## 学员提出的问题/需求
1. 想看 aistudy19 仓库的代码（FastAPI 项目），从零开始学习
2. 不理解文件结构和整体设计
3. 不理解 prefix 和路由的关系
4. 想了解数据库部分
5. 依赖注入是什么意思
6. 为什么不能直接粘贴图片给 Claude

## 讲解的概念与教学过程

### 1. 项目结构讲解
用"餐厅比喻"帮助理解：
- FastAPI = 接待员（接收请求）
- SQLAlchemy = 仓库管理员（操作数据库）
- 路由 = 分拣员（决定请求交给谁处理）

项目文件结构：
```
aistudy19/
├── demo1.py      # 主入口（实际只是随机数练习）
├── main.py       # 真正的入口：创建app、注册路由、启动服务
├── app/
│   ├── userapi.py   # 用户接口（/user/luck, /user/luck2）
│   └── empapi.py    # 员工接口（/emp/add, /emp/all）
└── schemas/
    ├── datamodel.py # 表结构定义（Emp 类 → t_emp 表）
    └── dbutil.py    # 数据库连接（engine, sessionLocal）
```

### 2. FastAPI 路由机制
- prefix = "部门名称"，所有接口以它开头
- 文件名和 prefix 可以不同
- 用户访问路径 = host + prefix + 接口路径

示例：
- empapi.py 的 prefix="/emp"
- 所以 `/emp/add` 和 `/emp/all` 是这个文件的接口

### 3. SQLAlchemy 数据库
- engine = 数据库连接工具（create_engine）
- sessionLocal = 会话工厂（sessionmaker(bind=engine)）
- 每次调用 sessionLocal() = 生产一个新的 db 会话
- dbutil.py：连接数据库 `mysql+pymysql://root:xing%401688@127.0.0.1:3306/db_company`

### 4. datamodel.py 表结构
```python
Base = declarative_base()  # ORM 基类
class Emp(Base):
    __tablename__ = "t_emp"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    age = Column(Integer)
    job = Column(String(20))
    create_time = Column(DateTime, default=datetime.datetime.now)
Base.metadata.create_all(engine)  # 如果表不存在就创建
```

### 5. 依赖注入（Depends）
```python
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
```
- 不用每次自己打开/关闭数据库
- FastAPI 自动调用 get_db() 并把结果传进来

### 6. empapi.py 增删改查
**新增（/emp/add）：**
```python
emp = Emp(name=obj.name, age=obj.age, job=obj.job)
db.add(emp)      # 准备新增
db.commit()      # 确认保存
```

**查询（/emp/all）：**
```python
emps = db.query(Emp).all()  # SELECT * FROM t_emp
for emp in emps:
    arr.append(EmpData(...))
```

### 7. Pydantic 模型
```python
class EmpAdd(BaseModel):  # 请求参数模板
    name: str = Field(min_length=2, max_length=20)
    age: int = Field(ge=12, le=20)
    job: str = Field(min_length=2, max_length=20)

class EmpData(BaseModel):  # 返回数据模板
    id: int
    name: str
    age: int
    job: str
    create_time: datetime.datetime
```
- Field 用于参数校验（长度、范围等）

### 8. 前端三件套讲解
应学员要求，总结了前端知识（已更新到 CLAUDE.md）：
- HTML = 内容结构
- CSS = 样式外观
- JavaScript = 交互行为

### 9. 雪了一段前端代码
学员贴了一段 JS 代码（var/let/const、数据类型），代码无报错。

## 识别的知识漏洞
- prefix 和文件名的关系（已讲解清楚）
- 依赖注入的概念（已讲解）
- ORM 的理解（已初步理解）

## 完成的练习
1. 理解 FastAPI 项目整体结构
2. 理解 prefix 和路由的关系
3. 理解 SQLAlchemy ORM 的作用
4. 理解依赖注入 Depends
5. 学习前端三件套 HTML/CSS/JS

## 今日代码文件
```
/tmp/aistudy19/   # 克隆的 aistudy19 仓库
```

## 明日计划
1. 继续学习前端（如果有需要）
2. 继续 FastAPI 项目学习
3. 复习 OOP 部分（继承、重写、super()、封装、多态）

## 学习效果评估
- 项目结构理解：明显提升
- SQLAlchemy 理解：基本掌握 ORM 概念
- 前端知识：初步了解 HTML/CSS/JS 作用
- 整体状态：学习积极性高

---

## 下次继续
```
继续学习，请读取：
1. progress/python-tracker.md
2. sessions/2026-04-21/session-notes.md

上次学完发现：
- 前端三件套初步了解
- FastAPI 项目结构初步理解
- SQLAlchemy ORM 初步理解
- 依赖注入初步理解
```
