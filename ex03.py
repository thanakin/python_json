import json

print(json.dumps({"name": "Thanakin", "age": 12}))
#{"name": "Thanakin", "age": 12}

print(json.dumps(["uvas", "bananas"]))
#["uvas", "bananas"]

print(json.dumps(("laranjas", "abacaxis")))
#["laranjas", "abacaxis"]

print(json.dumps("Ola Mundo!"))
#"Ola Mundo!"

print(json.dumps(42))
#42

print(json.dumps(3.1415))
#3.1415

print(json.dumps(True))
#true

print(json.dumps(False))
#false

print(json.dumps(None))
#null