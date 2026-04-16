# 学习会话记录 - 2026-04-16

## 会话概览
- 日期：2026-04-16
- 形式：一对一教学
- 核心主题：FastAPI 基础 + 前后端架构理解

## 学员提出的问题/需求
1. 想学 FastAPI
2. 不理解 @app.get / @app.post 的意思
3. 不理解装饰器 @ 是什么
4. 不理解为什么 Pydantic 用 class 定义模型
5. 不理解普通类 vs Pydantic 类的区别
6. 问前后端分离架构是什么

## 讲解的概念与教学过程

### 1. Git/Gitee SSH 连接
学员配置了 SSH 公钥连接 Gitee：
- 生成了 SSH key: `ssh-keygen -t ed25519`
- 添加公钥到 Gitee
- 测试连接成功：`Hi 王琪萌! You've successfully authenticated`

遇到的问题：
- 仓库地址更换，需要 `git remote set-url` 更新
- 权限不足（Auth error），因为队友仓库被删重建

### 2. uvicorn 端口占用问题
学员遇到"Error loading ASGI app"和"Port 8000 already in use"：
- 用 `netstat -ano | findstr :8000` 查进程
- 用 `taskkill /PID xxx /F` 杀进程
- 学会切换运行 `uvicorn new:app --reload`

### 3. HTTP 方法讲解
GET = 获取数据（问服务器要东西）
POST = 发送/创建数据（给服务器发东西）
PUT = 更新数据
DELETE = 删除数据

### 4. 装饰器 @ 解释
```
@app.get("/")
def root():
    return {"message": "Hello"}
```
- @ 是 Python 装饰器
- 给函数"戴帽子"，改变它的行为
- 告诉 FastAPI：这个函数可以被网址访问

### 5. 三种参数类型

| 类型 | 位置 | 示例 |
|-----|------|------|
| Path | URL 路径 | `/user/{user_id}` |
| Query | URL 问号后 | `?size=5` |
| Body | 请求体 JSON | POST 请求里的 JSON |

### 6. Pydantic BaseModel 解释
- 普通类需要自己写 `__init__` 和属性
- Pydantic 类只需写属性，自动处理初始化和验证
- 数据格式不对会自动报错

### 7. 前后端分离架构
```
用户 → 前端（界面） → 后端（逻辑） → 数据库（存储）
```
- 前端 = 网页/App（显示界面）
- 后端 = FastAPI/Django/Flask（处理请求）
- 数据库 = MySQL/SQLite（存数据）

比喻：
- 前端 = 服务员（接收顾客请求）
- 后端 = 厨师（真正做菜）
- 数据库 = 冰箱（存食材）

## 学员问题记录
- "@app.get 什么意思？" → 解释了装饰器和 HTTP 方法
- "Pydantic 为什么用 class？" → 对比普通类解释
- "普通类和 Pydantic 类区别？" → 普通类要写 __init__，Pydantic 自动处理
- "那一大段代码实现什么？" → 解释是商品管理 API

## 识别的知识漏洞
- Python 装饰器概念较陌生
- 类和实例的理解需要巩固

## 完成的练习
1. 写第一个 FastAPI 应用
2. 实现 Path 参数：`/items/{item_id}`
3. 实现 Query 参数：`/items/?skip=0&limit=10`
4. 实现 POST Body 参数：用 Pydantic 模型验证
5. 用 `/docs` Swagger 页面测试 API

## 作业状态
学员表示 BERT 情感分析作业已完成。

## 今日代码文件
```
FastApi/
├── main.py    # 第一个 FastAPI 应用
├── new.py     # Path 参数练习
├── all.py     # 完整示例（Path + Query + Body）
└── note.py    # 注释练习
```

## 学习效果评估
- FastAPI 基础：理解 HTTP 方法、装饰器、三种参数
- 前后端架构：完全理解
- 学员状态：积极，主动要求练习

## 明日计划
1. Matplotlib / Seaborn（图表可视化）
2. 报告第二章（同学已提供草稿）
3. FastAPI + SQLAlchemy（数据库集成）
