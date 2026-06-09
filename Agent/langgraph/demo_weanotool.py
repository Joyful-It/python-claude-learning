from langgraph.graph import START,StateGraph,END
#from model import llm
from typing import TypedDict

#定义状态
class weather_state(TypedDict):
    city:str
    temputer:float
#定义点
def get_weather(state:weather_state) ->dict:
    city=state['city']
    
    return {"temputer":30}
#定义图
flow=StateGraph(weather_state)
#tian jia dian
flow.add_node("huodetianqi",get_weather)
#tian jia bian
flow.add_edge(START,"huodetianqi")
flow.add_edge("huodetianqi",END)
#运行
app=flow.compile()
result=app.invoke({"city":"beijing"})
print(result)

