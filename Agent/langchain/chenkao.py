from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.agents.middleware import SummarizationMiddleware, PIIMiddleware

@tool
def ask_airport(start_point: str, end_point: str, date: str, time: str) -> str:
    """帮助出差员工查询机票，根据员工提供的出发地、目的地、日期、时间推荐航班。
    态度亲切，提醒员工乘飞机相关信息，比如值机。日期格式如2026-06-04，时间格式如14:30"""
    return (
        f" 已查到 {date} {time} 从【{start_point}】到【{end_point}】的航班：\n"
        f"  - CA1234 经济舱  ¥1680  余票12张\n"
        f"  - MU5678 商务舱  ¥3200  余票3张\n"
        f" 建议提前2小时到达机场值机哦！"
    )

@tool
def book_hotel(city: str, date: str, people: int, budget: str) -> str:
    """帮助出差员工预定酒店，根据城市、入住日期、人数和预算推荐酒店。
    会查询酒店评价，主动询问员工是否有窗户、含早餐等需求。"""
    return (
        f" 已查到【{city}】{date}入住、{people}人、预算{budget}的酒店：\n"
        f"  - 汉庭酒店  大床房  ¥298/晚  评分4.5  含早餐\n"
        f"  - 如家精选  双床房  ¥358/晚  评分4.7  有窗\n"
        f"💡 请选择心仪的酒店，需要了解周边交通或其他需求请告诉我！"
    )


model = init_chat_model(
    model="deepseek-v4-flash",      
    model_provider="deepseek",
    api_key="sk-20200342f04849fd955dc4cfb0e9ae6b"
)

middleware = [
    SummarizationMiddleware(model=model),
    PIIMiddleware(pii_type="email"),        
    PIIMiddleware(pii_type="credit_card"),   
]

from langgraph.checkpoint.memory import InMemorySaver
memory = InMemorySaver()
agent = create_agent(
    model=model,
    tools=[ask_airport, book_hotel],
    system_prompt="你是智能差旅助手，帮助员工查询机票和预定酒店。态度亲切专业，主动提醒出差注意事项。",
    middleware=middleware,
    checkpointer=memory,
)

print(" 智能差旅助手已就绪，输入 'quit' 退出\n")
while True:
    user_input = input(" 你：")
    if user_input.lower() == "quit":
        break
    print("助手：", end="", flush=True)
    for chunk in agent.stream(
        {"messages": [{"role": "user", "content": user_input}]},
        config={"configurable": {"thread_id": "travel-agent-session"}},
    ):
        # 只输出模型的文字回复，藏掉中间件/工具日志
        for key in chunk:
            if key == "model":
                for msg in chunk[key].get("messages", []):
                    if hasattr(msg, "content") and msg.content:
                        print(msg.content, end="", flush=True)
    print("\n")