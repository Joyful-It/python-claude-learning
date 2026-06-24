from langgraph.graph import START,END,StateGraph
from langchain_core.tools import tool
from typing import TypedDict


#定义状态
class weather_state(TypedDict):
    city:str
    weather:str
@tool
def weather(city:str)->str:
    """查询天气"""
    return f"{city} is good"
def get_weather(state:weather):
    result=weather.invoke(
        city=state["city"]
    )
flow=StateGraph(weather_state)
flow.add_node("weather",get_weather)
flow.add_edge(START,"weather")
flow.add_edge("weather",END)
app=flow.compile()
result=app.invoke({"city":"beijing"})
print(result)

