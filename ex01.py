import json

teste1 = '{ "name":"Thanakin", "age":12, "local":"Death Star" }'

teste2 = json.loads(teste1)

print(teste2["age"])
#12