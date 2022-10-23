dict1 = {
    "brand": "honda",
    "model": "amaze",
    "year" : "2018 diesel",
    "electric" : False,
    "color" : ["white"]
}

#! Print all key names in the dictionary, one by one:
for keys in dict1 : 
    print(keys)

print("______________________________________")
#! Print all values in the dictionary, one by one:
for values in dict1 :
    print(dict1[values])


print("______________________________________")

#! other methods to print keys and values:

for i in dict1.keys():
    print(i)

print("---")

for x in dict1.values():
    print(x)

print("---")
#! loop through both keys and values:
for y in dict1.items():
    print(y)
