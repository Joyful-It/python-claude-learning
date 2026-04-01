import json
import requests

response=requests.get("https://wttr.in/Beijing?format=j1")
if response.status_code == 200 :
    new_response=response.json()
    print(json.dumps(new_response,indent=4,ensure_ascii=False))
    #第一个参数是对象，第二个是缩进，第三个转换为中文