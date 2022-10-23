'''
JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.
'''

import json

# some json
x =  '{ "name":"John", "age":30, "city":"New York"}'

# Parse x
y = json.loads(x)

print(y["age"])