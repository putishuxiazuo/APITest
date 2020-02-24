import json

with open('./test.json','r')  as  f:
    data = f.read()
data = json.loads(data)
print(data)