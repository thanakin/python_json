import json

teste = {
    "name": "Thanakin",
    "age": 12,
    "married": True,
    "divorced": False,
    "children": None,
    "pets": ("Nino", "Layka","Mil-Mi", "Muleke"),
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print('>>> Sem identacao <<< ')
print(json.dumps(teste))
print('>>> Sem identacao <<< ')

print('>>> Com identacao <<< ')
# use four indents to make it easier to read the result:
print(json.dumps(teste, indent=4))
print('>>> Com identacao <<< ')