from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ========== Pydantic 模型 ==========
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

# ========== Path 参数 ==========
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

# ========== Query 参数 ==========
@app.get("/items/")
def list_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# ========== Body 参数 ==========
@app.post("/items/")
def create_item(item: Item):
    return item
