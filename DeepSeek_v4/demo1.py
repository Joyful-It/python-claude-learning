from openai import OpenAI # 导入OpenAI类，用于创建OpenAI API客户端

client = OpenAI(
    api_key="sk-a18b770419fb4bed87d887c2013ef32e",
    base_url="https://api.deepseek.com"
)

response=client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[{"role":'user',"content":"deepseek-v4 什么时候发布的"}],
    stream=True,
    temperature=1.0

)
# print(response.choices[0].message.content)
for chunk in response:
    if chunk.choices[0].delta.content:
        # 检查是否有新内容,delta.content是新内容的字符串 
        # chunk是响应的每个部分 choices[0]是第一个选择，返回选择列表
        # chunk.choices[0]是第一个选择的delta对象
        print(chunk.choices[0].delta.content, end="")