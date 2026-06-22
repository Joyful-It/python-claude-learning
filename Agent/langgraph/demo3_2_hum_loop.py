from langgraph.graph import START,END,StateGraph
from typing import Annotated,TypedDict
from langgraph.types import interrupt,Command
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import AIMessage

# ==================== Step 1: 定义状态 ====================
class message_state(TypedDict):
    """审批信息状态"""
    message:Annotated[list,add_messages]  # 消息列表（自动追加，不覆盖）
    content:str                           # 待审批的内容
    approved:bool                         # 审批结果

# ==================== Step 2: 定义节点 ====================
def gen_message(state:message_state)->dict:
    """生成待审批消息（实战中这里可能是AI写的内容）"""
    return{"content":"AI will generate message"}

def jud_message(state:message_state)->dict:
    """人工审批节点：interrupt()暂停，等人做决定"""
    # interrupt() 把待审内容抛给人类，程序卡在这里
    # 人类通过 Command(resume=...) 把决定传回来，赋值给 review
    review=interrupt({
        "message":"please review this message",
        "content":state.get("content","")
    })
    # review 是人工审批返回的字典，取 approved 字段
    # 默认 False（不是字符串"false"——非空字符串if判断为True，会绕过审批）
    return{"approved":review.get("approved",False)}

def publish_message(state:message_state)->dict:
    """根据审批结果发布/拒绝消息"""
    if state["approved"]:
        return{"message":[AIMessage(content="published")]}
    return{"message":[AIMessage(content="not published")]}

# ==================== Step 3: 构建图 ====================
flow=StateGraph(message_state)

# 注册节点
flow.add_node("gen_message",gen_message)
flow.add_node("jud_message",jud_message)
flow.add_node("publish_message",publish_message)

# 连线：直线 → 直线 → 审批 → 发布 → 结束
flow.add_edge(START,"gen_message")
flow.add_edge("gen_message","jud_message")
flow.add_edge("jud_message","publish_message")
flow.add_edge("publish_message",END)

# ==================== Step 4: 编译与运行 ====================

# MemorySaver 是内存版检查点——interrupt暂停需要它来保存状态
checkpointer = MemorySaver()
app = flow.compile(checkpointer=checkpointer)

# config 区分不同会话（同一个thread_id=同一条对话线）
config = {"configurable": {"thread_id":"111"}}

# 第一次调用：跑到 jud_message 的 interrupt() 会自动暂停
# 返回值里包含 interrupt 抛出的待审内容
print("=" * 40)
app.invoke({"content": "", "approved": False, "messages": []}, config)

# 取当前状态，把待审内容亮出来给管理员看
state = app.get_state(config)
if state.interrupts:
    interrupt_data = state.interrupts[0].value  # 取出 interrupt 携带的数据
    print(f"[待审批内容] {interrupt_data.get('content', '无内容')}")
    print(f"[提示信息] {interrupt_data.get('message', '')}")

# 管理员看到内容后做决定
cmd = input(" 管理员审批 (approve / reject): ")

# Command(resume=...) 把人工决定塞回去，流程从 jud_message 继续往下走
# review 变量收到 resume 里的字典，然后 return {"approved": ...}
result = app.invoke(Command(resume={"approved": cmd == "approve"}), config)

# 最终结果从 state 的 message 列表取最后一条
print(f"最终消息: {result['message'][-1].content}")
