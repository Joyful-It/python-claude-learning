from model import llm
from langchain_core.tools import tool
from langgraph.prebuilt import tool_node
from langgraph.graph import MessagesState,StateGraph,START
from langchain_core.messages import HumanMessage

#step 1 定义节点
@tool
def ask_weather(query:str)->str:
    pass