dict1 = {
    "brand": "honda",
    "model": "amaze",
    "year" : "2018 diesel",
    "electric" : False,
    "color" : ["white"]
}

print("---Method 1---")

dict2 = dict1.copy()
print(dict2)

print("---Method 2---")

dict3 = dict(dict1)
print(dict3)