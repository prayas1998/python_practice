dict1 = {
    "brand": "honda",
    "model": "amaze",
    "year" : "2018 diesel",
    "electric" : False,
    "color" : "white"
}

x = dict1["year"]
x1 = dict1.get("year") #! another method
print(x)
print(x1)

print("_____________________________")
#! Get keys : The keys() method will return a list of all the keys in the dictionary.

x2 = dict1.keys()
print(x1)

print("_____________________________")
#! Add a new item to the original dictionary, and see that the keys list gets updated as well:
dict1["passenger capacity"] = 5
print(dict1)
print(len(dict1))

print("_____________________________")
#! Get Values : The values() method will return a list of all the values in the dictionary.
x3 = dict1.values()
print(x3)

#! Make a change in the original dictionary, and see that the values list gets updated as well:
dict1["color"] = "red"
print(dict1)

print("_____________________________")
#! Get Items : 
print(dict1.items())

#! Check if Key Exists : To determine if a specified key is present in a dictionary use the in keyword
if "model" in dict1:
    print("yes, model is present in the dictionary")