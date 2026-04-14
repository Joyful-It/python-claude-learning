import json
import requests


response=requests.post(
    url = "http://47.108.60.237:3300/api",
    headers = {
    "Authorization": "Bearer cr_35202ed0073f8a6c357f01b7f56c67a3784b586a633a88b730d2bd695ba271ff",
    "Content-Type": "application/json"
    },
    json = {
    "model": "glm-5",
    "messages": [
        {"role": "user", "content": "现在几点"}
        ]
    }

)
result = response.json()
print(result)
