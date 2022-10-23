thislist = ["apple", "banana", "cherry"]

thislist.append("lemon") #! Adds item at the end of a list
print(thislist)

print("--------------------------------------------------------")

#! To insert a list item at a specified index, use the insert() method.

thislist.insert(1,"watermelon") #! Added at index 1 of the list.
print(thislist)

print("--------------------------------------------------------")
#! Extend List : To append elements from another list to the current list, use the extend() method.

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#! The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thistuple = ("kiwi", "lemons", "dragon fruit")
thislist.extend(thistuple)
print(thislist)