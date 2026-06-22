import random
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# step 1 定义state
class Chengji(TypedDict):
    """学生成绩状态：姓名、分数、等级、考试次数"""
    name: str         # 学生姓名
    score: int        # 考试成绩
    grade: str        # 毕业状态
    exam_count: int   # 考试次数（用于循环计数）


# step 2 定义节点
def take_exam(state:Chengji):
    score = random.randrange(10, 100,10)
    exam_count  = state.get("exam_count",0)  + 1
    print(f"第{exam_count}次考试，得分{score}")
    return {"score":score, "exam_count":exam_count}


def pass_exam(state:Chengji):
    return {"grade":"毕业"}

# 条件边
def router(state:Chengji):
    if state["score"] >= 60:
        return "pass_exam"
    return "take_exam"

# step3 定义图
flow = StateGraph(Chengji)
flow.add_node("take_exam", take_exam)
flow.add_node("pass_exam", pass_exam)
flow.add_edge(START, "take_exam")
flow.add_conditional_edges("take_exam",router)
flow.add_edge("pass_exam", END)

# step4 编译和运行
app = flow.compile()
result = app.invoke({"name":"小王"})

print(result)