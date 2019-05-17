import json

teste1 = {
    "name": "Thanakin Skywalker",
    "age": 12,
    "local": "Death Star 2"
}

teste2 = json.dumps(teste1)

print(teste2) 
#{"name": "Thanakin Skywalker", "age": 12, "local": "Death Star 2"}