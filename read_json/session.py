import requests

s = requests.session()
s.auth = ("yzz","123456")
s.get("https://www.baidu.com/")
print(s.headers)