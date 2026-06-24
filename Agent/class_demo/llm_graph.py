from model import llm
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
from langgraph.graph import MessagesState,StateGraph,START,END
from langchain_core.messages import HumanMessage
@tool
def search(query: str) -> str:
    '''查询天气的工具函数'''
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "温度是 60 华氏度，天气阴霾。"

    return "温度是 90 华氏度，天气晴朗。"

# 把工具打包成节点：search函数 → tools列表 → ToolNode节点
tools = [search]                       # 工具列表
model = llm.bind_tools(tools)          # 把工具绑定给LLM，告诉LLM可以调用它
# step1 定义state
# MessagesState

# step 2 定义工具
tooL_node = ToolNode(tools) # 定义工具节点

# 定义LLM节点
def call_model(MessagesState):
    res = model.invoke(MessagesState['messages'])
    return  {"messages":[res]}   # list
# step 2 继续 定义条件边:传入 state ,返回节点名称
def should_contine(MessagesState):
    last_message = MessagesState['messages'][-1]
    if last_message.tool_calls:
        print("---调用工具---")
        return  "tool_node"
    else:
        print("----结束----")
        return "__end__"
# step 3 定意图
# (1) 初始化
flow = StateGraph(MessagesState)
# (2) 添加节点
flow.add_node("tool_node",tooL_node)  # （name:str, func)
flow.add_node("agent",call_model)
#(3) 添加边
flow.add_edge(START,"agent" )
flow.add_conditional_edges("agent", should_contine,
                           {"tool_node":"tool_node","__end__":END})  # (出发节点名，条件函数本身）
flow.add_edge("tool_node","agent")

# step4 编译和运行
app = flow.compile()

result = app.invoke(  {"messages": [HumanMessage(content="旧金山的天气如何")]  }  )

print(result['messages'][-1].content)


print(app.get_graph().draw_ascii())