# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for items in fruits:
    if "a" in items:
        newList.append(items)

print(newList)