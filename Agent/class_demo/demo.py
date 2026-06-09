from typing import  TypedDict
from langgraph.graph import StateGraph,START


# step1 定义state
class Chengji(TypedDict):
    name:str
    score:int
    grade:str



# step 2 定义节点: 传入 state，返回dict
def judge(Chengji):
    if Chengji['score'] >= 60:
        return  {"grade":"及格"}
    else:
        return {"grade":"不及格"}



# step3 定义图
# (1)  初始化图
flow = StateGraph(Chengji)
# # (2) 添加节点
flow.add_node("judge", judge)  # (name:str, func)
#(3) 添加边
flow.add_edge(START, "judge")  #(启动节点名, 目标节点名）

# step 4 编译 和 运行
app  =  flow.compile()

result = app.invoke({"name":"张三","score":80})  # 传入字典

print(result)