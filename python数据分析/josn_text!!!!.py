import json 
import pydantic
data = {"name":"zhang","age":20}

json_str = json.dumps(data)
print(json_str)

result=json.loads(json_str)
print(result["name"])

data={"name":"a","age":18}
json_data=json.dumps(data)
print(json_data)
print(data)
# 这两个字典完全一样！
# data1 = {"name": "a"}   # 你写的双引号
# data2 = {'name': 'a'}   # 单引号

# print(data1 == data2)   # True
# Python 不区分单双引号，打印字典时默认用单引号显示。

recived='{"name":"wer","age":23}'
# 那个单引号是 Python 的"包装纸"
# Copy code to clipboard
# # 这是一个 Python 字符串
# received = '{"city": "北京", "temp": 25}'
# #          ↑ 这里的单引号告诉 Python：里面是字符串内容

# # 如果不写单引号
# received = {"city": "北京", "temp": 25}  # Python 会认为这是字典！
# ￼
# 分层理解
# Copy code to clipboard
# '{"city": "北京", "temp": 25}'
#  ↑                              ↑  外层：Python 字符串的边界
#   ↑                          ↑    内层：JSON 格式的内容（双引号）
# 层
# 符号
# 属于谁
# 外层
# 单引号 '
# Python（表示这是字符串）
# 内层
# 双引号 "
# JSON（标准格式）
a=json.loads(recived)
print("encodeing :",a)