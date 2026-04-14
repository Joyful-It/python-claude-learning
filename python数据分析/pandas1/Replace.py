import pandas as pd

data = pd.DataFrame({
    'name': ['张三', '李四', '王五'],
    'birthday': ['2000-10-01', '2000 09 01', '2001 09 01']
})

print("原始数据：")
print(data)

print("\n--- 把空格替换成横杠 ---")
data['birthday'] = data['birthday'].str.replace(' ', '-')
print(data)