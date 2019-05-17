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

# sort the result alphabetically by keys:
print(json.dumps(teste, indent=4, sort_keys=True))