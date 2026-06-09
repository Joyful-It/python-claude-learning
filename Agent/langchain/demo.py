import langchain
import random
import os
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

# print(f"版本号：{langchain.__version__}")

# 定义函数 工具调用
def get_weather(city):
    "ask weather"
    return f"{city} weather is warm"
def get_num ():
    "get lucky number"
    return random.randint(1,100)

model=init_chat_model(
    model="deepseek-v4-flash",
    model_provider="deepseek",
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

agent=create_agent(
    model=model,
    tools=[get_weather,get_num],
    system_prompt="你是天气预报员"
)

res=agent.invoke(
    {'messages':[{"role":'user','content':'睢县天气'}]}
)
print(res)