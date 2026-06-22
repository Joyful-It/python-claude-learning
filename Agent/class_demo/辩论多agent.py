from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from sqlalchemy.ext.asyncio import result


# state
class DebateState(TypedDict):
    messages: Annotated[list, add_messages]
    topic: str           # 辩论议题
    pro: str             # 正方观点
    con: str             # 反方观点
    neutral: str         # 中立数据
    consensus: str       # 最终裁决结果


# node
def pro_agent(state: DebateState) -> dict:
    """正方 Agent：给出支持理由"""
    return {"pro": f"支持「{state['topic']}」的理由：\n1. 提升效率\n2. 降低成本\n3. 可扩展性强"}

def con_agent(state: DebateState) -> dict:
    """反方 Agent：给出反对理由"""
    return {"con": f"反对「{state['topic']}」的理由：\n1. 安全风险\n2. 实施复杂\n3. 初期投入高"}

def neutral_agent(state: DebateState) -> dict:
    """中立 Agent：提供客观数据"""
    return {"neutral": f"中立数据：\n1. 行业采用率 +40%\n2. 平均 ROI 18 个月"}


def judge_agent(state: DebateState) -> dict:
    """裁决者：综合正反方观点，输出最终结论"""
    consensus = (f"## 辩论共识：{state['topic']}\n\n"
                 f"### 正方\n{state['pro']}\n\n"
                 f"### 反方\n{state['con']}\n\n"
                 f"### 数据\n{state['neutral']}\n\n"
                 f"**裁决**：建议分阶段推进")
    return {"consensus": consensus}


# graph
graph = StateGraph(DebateState)
graph.add_node("pro_agent", pro_agent)
graph.add_node("con_agent", con_agent)
graph.add_node("neutral_agent", neutral_agent)
graph.add_node("judge_agent", judge_agent)

graph.add_edge(START, "pro_agent")
graph.add_edge(START, "con_agent")
graph.add_edge(START, "neutral_agent")
graph.add_edge("pro_agent", "judge_agent")
graph.add_edge("con_agent", "judge_agent")
graph.add_edge("neutral_agent", "judge_agent")
graph.add_edge("judge_agent", END)

# 编译 运行
app = graph.compile()
result = app.invoke({"topic": "企业引入 AI 自动化"})
print(result["consensus"])