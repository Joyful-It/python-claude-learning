from fastapi import FastAPI

app = FastAPI()  # 创建应用 app约定俗称

@app.get("/")           # 查
def read_root():
    return {"message": "Hello"}

@app.post("/items/")    # 创建
def create_item():
    return {"message": "创建成功"}

@app.put("/items/1/")   # 更新
def update_item():
    return {"message": "更新成功"}

@app.delete("/items/1/") # 删除
def delete_item():
    return {"message": "删除成功"}
"""
.get 可以换成什么？

方法      作用      何时用
.get      获取数据  查东西
.post     创建数据  注册/新增
.put      更新数据  改东西
.delete   删除数据  删除
"""