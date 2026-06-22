from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt, Command
from langchain_core.messages import AIMessage
from torch.distributed._shard import checkpoint


# step 1 定义state
class ApprovalState(TypedDict):
    """审批状态：对话历史 + 待审核内容 + 是否通过"""
    messages: Annotated[list, add_messages]  # 对话消息
    content: str                             # 待审核的内容
    approved: bool


# 定义节点

def generate_content(state: ApprovalState):
    return {"content": "AI 生成的草稿内容"}

def human_review(state: ApprovalState):
    print("content：", state["content"])

    review = interrupt({
        "messages": state.get("messages","请审核一下内容"),
        "content": state.get("content", "")
    })
    return {"approved": review.get("approved", False)}


def publish_content(state: ApprovalState):
    if state.get("approved", False):
        return {"messages": [AIMessage(content="内容已发布")]}

    return {"messages": [AIMessage(content="内容未通过审核")] }


# 定意图
flow = StateGraph(ApprovalState)
flow.add_node("generate_content",generate_content)
flow.add_node("human_review",human_review)
flow.add_node("publish_content",publish_content)

flow.add_edge(START,"generate_content")
flow.add_edge("generate_content","human_review")
flow.add_edge("human_review","publish_content")
flow.add_edge("publish_content",END)

# step4
checkpointer = MemorySaver() # MemorySaver()
app = flow.compile(checkpointer=checkpointer)

config = {"configurable":  {"thread_id":"111"} }


app.invoke({"content": "", "approved": False, "messages": []}, config)

cmd = input(" 管理员审批 (approve / reject): ")

result = app.invoke(Command(resume={"approved": cmd == "approve"}), config)

print(f"最终消息: {result['messages'][-1].content}")