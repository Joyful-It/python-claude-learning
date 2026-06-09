from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, AIMessage


# 定义普通 list  state
class StateA(TypedDict):
    messages:list


class StateB(TypedDict):
    messages:Annotated[list,add_messages]


# 定义节点
# 图a的节点
def node1(state: StateA):
    return {"messages": [AIMessage("第一条回复")]}

def node2(state: StateA):
    return {"messages": [AIMessage("第二条回复")]}

# 图b的节点
def node3(state: StateB):
    return {"messages": [AIMessage("第一条回复")]}

def node4(state: StateB):
    return {"messages": [AIMessage("第二条回复")]}

# 定意图a
flow_a = StateGraph(StateA)
flow_a.add_node("node1",node1)
flow_a.add_node("node2",node2)
flow_a.add_edge(START,"node1")
flow_a.add_edge("node1","node2")



# 编译和运行
app_a = flow_a.compile()
result_a = app_a.invoke({"messages":[HumanMessage("开始！")]})

print("a:",result_a['messages'])

# 定意图b
flow_b = StateGraph(StateB)
flow_b.add_node("node3",node3)
flow_b.add_node("node4",node4)
flow_b.add_edge(START,"node3")
flow_b.add_edge("node3","node4")


# 编译 运行
app_b = flow_b.compile()
result_b = app_b.invoke({"messages":[HumanMessage("开始！")]})
print("b:",result_b['messages'])