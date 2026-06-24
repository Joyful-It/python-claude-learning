from model import llm
from langgraph.graph import START,END,StateGraph
from langchain_core.messages import HumanMessage
from typing import TypedDict

#state
class Babyagi_satae(TypedDict):
    result:str
    tasks:list
    objective:str

#node
def decompose(state:Babyagi_satae)->dict:
    tasks=[
        "做数学作业",         # 今晚要交，最急
        "复习英语单词",       # 明天听写
        "写作文",             # 后天交
        "整理笔记",           # 不着急
        "预习明天课程",       # 有空再做
    ]
    print(f"decome {len(tasks)}")
    for t in tasks:
        print(f"-{t}")
    return{"tasks":tasks}

def execute_next(state:Babyagi_satae)->dict:
    task = state["tasks"][0]
    result=f"finshed it {task}"
    print("doing")
    print("done")
    return{"tasks":state["tasks"][1:],"result":result}
def reprioritize(state:Babyagi_satae):
    if not state["tasks"]:
        return{"tasks":[]}
    remaining = "\n".join(state["tasks"])
    prompt = f"目标：{state['objective']}\n刚完成：{state['result']}\n剩余任务：\n{remaining}\n重新排序，最重要的在前。只输出任务名，每行一个，不要序号。"
    
    response = llm.invoke([HumanMessage(content=prompt)])
    new_tasks = [line.strip() for line in response.content.strip().split("\n") if line.strip()]
    
    print(f"\n[LLM 重排] 根据「{state['result']}」重新思考任务顺序：")
    for i, t in enumerate(new_tasks, 1):
        print(f"  {i}. {t}")
    
    return {"tasks": new_tasks}
def route(state: Babyagi_satae):
    """条件边：有任务就循环（回到 execute_next），没任务就结束"""
    if state["tasks"]:
        print("[路由] 还有任务 → 继续循环\n")
        return "execute_next"
    print("[路由] 任务全部完成 → 结束\n")
    return "__end__"

builder = StateGraph(Babyagi_satae)
builder.add_node("decompose", decompose)
builder.add_node("execute_next", execute_next)
builder.add_node("reprioritize", reprioritize)
builder.add_edge(START, "decompose")
builder.add_edge("decompose", "execute_next")
builder.add_edge("execute_next", "reprioritize")   # 执行完 → 先重排
builder.add_conditional_edges("reprioritize", route) 