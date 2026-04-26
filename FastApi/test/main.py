import fastapi #fastapu框架
import uvicorn# 服务器软件 （运行fastapi）
from app import userapi empapi

app= fastapi.FastAPI()

app.include_router(userapi.router)
app. include_router(empapi.router)

if __name__ == "main":                                 
    uvicorn.run(app,host="0.0.0.0",post=8000)
    
"""
# 第4步：启动服务器
if __name__ == "__main__":           # 只有直接运行这个文件时才执行
    uvicorn.run(app, host="127.0.0.1", port=8000)
    #                  ↑            ↑    ↑
    #              本机地址        端口号

app.include_router(userapi.router)  # 注册用户的路由
app.include_router(empapi.router)   # 注册员工的路由

aistudy19/
├── demo1.py      # 主入口，创建 FastAPI 应用并注册路由
├── main.py       # 数据库连接配置（SQLAlchemy）
├── app/
│   ├── userapi.py   # 用户 API（两个接口）
│   └── empapi.py    # 员工 API（增、查）
└── schemas/
    ├── datamodel.py # 员工表映射（类 → 表）
    └── dbutil.py    # 数据库连接工具


"""