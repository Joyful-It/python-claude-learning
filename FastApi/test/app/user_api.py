import random
import fastapi
from pydantic import BaseModel,field

router = fastapi.APIRouter(prefix="/user",tags=["user"])

@router.get("/luck")
def luck (name:str,age:int):
    if 1<age<100:
        if len(name.split())>0:
            return{"name":name,"age":age,"num":random.randint(1,10)}
        
        