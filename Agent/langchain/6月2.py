from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool

@tool
def teacher_math(subject):
    """数学题很难，一步一步指导，安心鼓励"""
    return f'{subject} is hard.no worry i can help you'
@tool
def teacher_english(subject):
    '''英语题需要每个单词和孩子翻译，尽量用他们看过的英语动画片比如汪汪队，海绵宝宝剧情解释'''
    return f'{subject} 不难，如果把主角当成海绵宝宝呢'
@tool
def teacher_chinese(subject):
    '''语文要详细教一下拼音顺便把常用成语也教一下'''
    return f'{subject}'

model=init_chat_model(
    model="deepseek-v4-flash",
    model_provider='deepseek',
    api_key='sk-20200342f04849fd955dc4cfb0e9ae6b'
    
)

agent=create_agent(
    model=model,
    tools=[teacher_chinese,teacher_english,teacher_math],
    system_prompt="你是小学老师"

)
for chunk in agent.stream(
    {'messages': [{'role': 'user', 'content': '数学题:6*7+3*9'}]}
):
    print(chunk)

