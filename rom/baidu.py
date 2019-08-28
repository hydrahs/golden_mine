import requests
w = "http://www.baidu.com"
response = requests.get(w)
response.encoding="utf-8"
print(response.text)