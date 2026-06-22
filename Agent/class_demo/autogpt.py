from model import llm
from typing import TypedDict
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END


# step 1
class AutoGPTState(TypedDict):
    objective: str    # 总目标
    tasks: list       # 当前任务列表（每次 think 都可能变）
    result: str       # 上一步执行结果


# step 2 定义节点和 条件边
def think(AutoGPTState):

    if AutoGPTState['result']:
        remaining  = "、".join(AutoGPTState["tasks"])
        prompt = f"""
        目标任务是：{AutoGPTState['objective']}
        已完成：{AutoGPTState['result']}
        剩余任务是：{remaining}
        请安排剩余任务。除非上一步结果提示有必要调整，否则原样输出。每行一个。
        
        """

    else:

        prompt = f""" 
        我目标是：{AutoGPTState['objective']}
        请拆分目标任务，按顿号拆分子项任务，每个子项任务作为一个任务，不要再拆分，每行一个，不要添加序号
          """
    tasks_ = llm.invoke([HumanMessage(content=prompt)])
    tasks_list = [t.strip() for t in tasks_.content.strip().split("\n") if t.strip()]
    return {"tasks":tasks_list}




def act(AutoGPTState):
    result  = AutoGPTState["tasks"][0]
    print("完成了:",result)
    remaining_task = AutoGPTState["tasks"][1:]
    print("还剩余任务：",remaining_task)
    return {"result":result, "tasks":remaining_task}




def router(AutoGPTState):
    if AutoGPTState['tasks']:
        print(f"[观察决策] 还剩 {len(AutoGPTState['tasks'])} 个任务，继续...\n")
        return "think"
    else:
        return END


# step 3
flow = StateGraph(AutoGPTState)
flow.add_node("think",think)
flow.add_node("act",act)
flow.add_edge(START,"think")
flow.add_edge("think", "act")
flow.add_conditional_edges("act",router)


# step 4 编译和运行
app = flow.compile()
result = app.invoke({ "objective": "帮小明完成周末作业：做完数学卷子、背 20 个英语单词、写一篇 300 字日记","result":""})

print(result)
