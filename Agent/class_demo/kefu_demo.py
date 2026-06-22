from model import llm
from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage



# step 1 定义state
class State(TypedDict):
    messages: Annotated[list, add_messages]
    enough: str  # 信息是否足够："yes" / "no"
    category: str  # 商品类别：手机/家电/服装


# step 2 定义节点
def ask(State):
    """向用户提问，收集需求信息"""
    msg = input("输入需求：")
    return {"messages": [HumanMessage(content=msg)]}

# 判断节点
def judge(State):
    convestion = ",".join(m.content  for m in State['messages'])
    prompt = f"对话内容：{convestion}\n\n请判断是否能确定客户想要的商品类别（手机/家电/服装）？只需回答 yes 或 no。"
    res = llm.invoke([HumanMessage(content=prompt)])
    print("res:",res.content)
    return {"enough": "yes" if "yes" in res.content else "no"}


def category(State):
    chat = " ".join(m.content for m in State["messages"])
    prompt = (
        "你是一个商品分类器。\n"
        "请根据对话内容，只回答一个客户想要买的商品类型，不要解释。\n"
        "可选类别：手机 / 家电 / 服装\n\n"
        f"对话内容：{chat}"
    )
    res = llm.invoke([HumanMessage(content=prompt)])
    return {"category": res.content}


def phone(State):
    print("手机AI助手已接入")
    return {"result": "手机AI助手已接入"}

def appliance(State):
    return {"result": "家电AI助手已接入"}

def clothing(State):
    return {"result": "服装AI助手已接入"}


def router( State):
    if State["enough"] == "yes":
        return "category"

    else:
        return "ask"


def router2( State):
    if State["category"] == "手机":
        return "phone"

    elif State["category"] == "家电":
        return "appliance"

    elif State["category"] == "服装":
        return "clothing"


# step 3 定义图
flow = StateGraph(State)
flow.add_node("ask", ask)
flow.add_node("judge", judge)
flow.add_node("category", category)
flow.add_node("phone", phone)
flow.add_node("appliance", appliance)
flow.add_node("clothing", clothing)

flow.add_edge(START, "ask")
flow.add_edge("ask", "judge")
flow.add_conditional_edges("judge",router)  # (出发节点名，条件函数本身）)

flow.add_conditional_edges("category",router2)


app = flow.compile()
result = app.invoke({"messages": [], "enough": "", "category": ""})
print(result["category"])