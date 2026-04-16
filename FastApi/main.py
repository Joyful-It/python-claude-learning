import fastapi
import random

app =fastapi.FastAPI(title="NB")
@app.get('/')
def UB():
    return("I am best person")
@app.get("/num")
def nums (size:int):
    arr=[]
    for i in range(size):
        arr.append(random.randint(1,100))
    return arr