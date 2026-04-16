from fastapi import FastAPI

app = FastAPI(title="学习路径参数")

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
