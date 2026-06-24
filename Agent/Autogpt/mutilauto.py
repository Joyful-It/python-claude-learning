from langgraph.graph import StateGraph,END,START
from langgraph.graph.message import add_messages
from typing import TypedDict,Annotated

#1
class muilauto(TypedDict):
    pass

#2
def super(state:muilauto):
    messages=Annotated[list,add_messages]
    task: str                       # 初始任务描述
    market_analysis: str            # 市场专家分析结果
    tech_feasibility: str           # 技术专家评估结果
    financial_projection: str       # 财务专家预测结果
    final_plan: str 

def market_agent(state:muilauto):
    return{
        "market_analysis":"50b"
    }
def tech_agent(state:muilauto):
    return{"tech_feasibility":"6 montshs"}
def financial