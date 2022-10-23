dict1 = {
    "brand": "honda",
    "model": "amaze",
    "year" : "2018 diesel",
    "electric" : False,
    "color" : ["white"]
}

#! The pop() method removes the item with the specified key name:
dict1.pop("color")
print(dict1)

#! The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
dict1.popitem()
print(dict1)

#! The del keyword removes the item with the specified key name:
del dict1["brand"]
print(dict1)
#! The del keyword can also delete the dictionary completely:


#! The clear() method empties the dictionary:
dict1.clear()
print(dict1)