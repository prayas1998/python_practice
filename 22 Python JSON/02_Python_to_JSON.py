import json

# python dict
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into json
y = json.dumps(x)

print(y)