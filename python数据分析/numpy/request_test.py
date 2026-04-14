import requests

def get_api(url):
    response=requests.get(url)
    print(response.status_code)
    return response.json()
result = get_api("https://api.github.com")
print(result)

def get_url(url):
    response1=requests.get(url)

    if response1.status_code == 200:
        data=response1.json()
        text=response1.text
        print("ok")
        return data
    else:
        return None

a=get_url("https://api.github.com")
print(a)