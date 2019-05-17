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

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(teste, indent=4, separators=(". ", " = ")))
