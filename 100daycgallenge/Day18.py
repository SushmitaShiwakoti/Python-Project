import json
from re import X
x = '{"name":"susmita shiwakoti","age":34, "city": "kathmandu"}'
y=json.loads(x)
print(y)
print(y['name'])

A= {
    "name":'susmita shiwakoti',
    "age":34,
    "city":'Kathmandu',
    "marrid":True,
    "divorced":False,
    "child":("ariya","aryan"),
    "pets":None, 
}
B=json.dumps(A)
print(B)
print(json.dumps(["apple","orange","banana"]))
# print(json.dumps({"susmita shiwakoti","yasoda shiwakoti","sarita shiwakoti"}))
print(json.dumps(("dhurba shiwakoti","sabin shiwakoti")))
print(json.dumps(A))