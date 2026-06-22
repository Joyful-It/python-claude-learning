from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from sqlalchemy.ext.asyncio import result


# step 1 定义状态
class BusinessPlanState(TypedDict):
    messages: Annotated[list, add_messages]
    task: str                       # 初始任务描述
    market_analysis: str            # 市场专家分析结果
    tech_feasibility: str           # 技术专家评估结果
    financial_projection: str       # 财务专家预测结果
    final_plan: str                 # 主管汇总的最终计划书


# step 2 定义节点

# 主管节点
def supervisor_agent(state: BusinessPlanState) -> BusinessPlanState:
    """主管 Agent：接收任务"""
    print(" 主管 Agent: 分解任务完成")
    return {"task": state["task"]}


def supervisor_final(state: BusinessPlanState) -> BusinessPlanState:
    """主管 Agent：汇总各专家结果生成最终计划书"""
    plan = f'''## 商业计划书
### 市场分析
{state.get('market_analysis', '')}
### 技术可行性
{state.get('tech_feasibility', '')}
### 财务预测
{state.get('financial_projection', '')}'''
    print(" 主管 Agent: 汇总完成")
    return {"final_plan": plan}


# 专家节点
def market_agent(state: BusinessPlanState) -> BusinessPlanState:
    """市场专家：分析市场情况"""
    print(" Market Agent: 分析市场...")
    return {"market_analysis": "市场规模预计500亿，目标用户25-35岁。"}

# 专家节点
def tech_agent(state: BusinessPlanState) -> BusinessPlanState:
    """技术专家：评估技术可行性"""
    print(" Tech Agent: 评估技术...")
    return {"tech_feasibility": "技术方案可行，需要6个月开发。"}

# 专家节点
def financial_agent(state: BusinessPlanState) -> BusinessPlanState:
    """财务专家：预测财务状况"""
    print(" Financial Agent: 预测财务...")
    return {"financial_projection": "初期投入200万，预计18个月回本。"}


# step3 定义图
graph = StateGraph(BusinessPlanState)
graph.add_node("supervisor_agent", supervisor_agent)
graph.add_node("market_agent", market_agent)
graph.add_node("tech_agent", tech_agent)
graph.add_node("financial_agent", financial_agent)
graph.add_node("supervisor_final", supervisor_final)

graph.add_edge(START, "supervisor_agent")
graph.add_edge("supervisor_agent", "market_agent")
graph.add_edge("market_agent", "tech_agent")
graph.add_edge("tech_agent", "financial_agent")
graph.add_edge("financial_agent", "supervisor_final")
# step4 编译和运行
app = graph.compile()
result = app.invoke({"task": "估开发AI客服的商业可行性"})

print("result:",result['final_plan'])


