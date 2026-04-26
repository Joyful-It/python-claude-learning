from fastapi import FastAPI

app = FastAPI(title="学习路径参数")

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
# @app.get("/路径")
#      ↓
# app 是 FastAPI 创建的应用实例
# .get 是 HTTP 请求方法
# /路径 是访问的网址
"""
.get 可以换成什么？

方法      作用      何时用
.get      获取数据  查东西
.post     创建数据  注册/新增
.put      更新数据  改东西
.delete   删除数据  删除
"""