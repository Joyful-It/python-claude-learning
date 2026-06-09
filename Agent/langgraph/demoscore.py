from typing import TypedDict
from langgraph.graph import StateGraph,START

#step 1 定义状态
class Score(TypedDict):
    name:str
    grade:str
    score: int
    

#step 2 定义节点工具
def judge(state : Score) ->dict:
    if state['score'] >= 60:
        return {"grade":"pass"}
    else :
        return{"grade":"fail"}
    
#定义图
#初始化图
flow = StateGraph(Score)
#添加节点
flow.add_node("judge",judge)
#添加边
flow.add_edge(START,"judge")
#运行
app = flow.compile()
result = app.invoke({"name":"san","score":61})
print(result)