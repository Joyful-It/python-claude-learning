from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from sqlalchemy.ext.asyncio import result


# ---------- 第①步：定义状态 ----------
class Chengji(TypedDict):
    """学生成绩状态：包含姓名、分数、等级、评语"""
    name: str          # 学生姓名（初始传入，后续不修改）
    score: float       # 考试分数（初始传入，后续不修改）
    grade: str         # 等级（judge 节点更新）
    report: str        # 评语（gen_report 节点更新）


# ---------- 第②步：定义节点 ----------
def judge(state: Chengji):
    """根据分数计算等级，只更新 grade 字段"""
    score = state["score"]
    if score >= 90:
        grade = "优秀"
    elif score >= 80:
        grade = "良好"
    elif score >= 70:
        grade = "中等"
    elif score >= 60:
        grade = "及格"
    else:
        grade = "不及格"
    return {"grade": grade}  # 只返回 grade，name 和 score 不变

def gen_report(state: Chengji):
    """根据等级写评语，只更新 report 字段"""
    print("befor gen_report:", state)
    grade = state["grade"]
    if grade == "优秀":
        report = "成绩优异，继续保持！"
    elif grade == "良好":
        report = "表现不错，还有提升空间！"
    elif grade == "中等":
        report = "成绩中等，需加倍努力！"
    elif grade == "及格":
        report = "刚好及格，要加油了！"
    else:
        report = "不及格，需要认真复习！"
    return {"report": report}  # 只返回 report，其他字段不变

# 构建图
flow = StateGraph(Chengji)
flow.add_node("judge",judge)
flow.add_node("gen_report",gen_report)

flow.add_edge(START,"judge")
flow.add_edge("judge","gen_report")

# 编译和运行
app = flow.compile()

result = app.invoke({"name": "张三", "score": 85, "grade": "", "report": ""})

print(result)