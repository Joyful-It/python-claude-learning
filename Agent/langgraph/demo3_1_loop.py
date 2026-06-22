from langgraph.graph import START,END,StateGraph
import random
from typing import TypedDict

#step 1 定义状态
class student_state(TypedDict):
    name:str
    score:float
    grade:str
    loop_count:int

# step 2 node
def get_score(state:student_state):
    score = random.randrange(10,90,10)
    cnt = state.get("loop_count",0)+1
    print(f"第{cnt}次考试->{score}分")
    return{"score":score,"loop_count":cnt}
    

def judge_score(state:student_state):
    return{"grade":"pass"}

#定义路由函数
def route(state:student_state)->str:#返回下一站去哪 所以是str
    if state['score']>=60:
        print("pass,end")
        return "judge_score"
    print("fail")
    return "get_score"
    


#step 3 图
flow=StateGraph(student_state)
flow.add_node("get_score",get_score)
flow.add_node("judge_score",judge_score)

flow.add_edge(START,"get_score")
flow.add_conditional_edges("get_score",route)

flow.add_edge("judge_score",END)

# step 4 run
app=flow.compile()
result=app.invoke({"name":"ming","score":0,"grade":"","loop_count":0})
print(result)

