# List Items
#! List items are ordered, changeable, and allow duplicate values.
#! List items are indexed, the first item has index [0], the second item has index [1] etc.
thisList = ["apple", "banana", "cherry"]
print(len(thisList))

print("------------------------------------------------------")

list1 = ["Prayas", "etawah", "Piyush", "Shubham"]
list2 = [1,5,7,8,34,9,2]
list3 = [True, False, True, True, False]
list4 = ["Prayas", "apple", 23, False, 699, True]

print(list1)
print(list2)
print(list3)
print(list4)
print(type(list1))

print("------------------------------------------------------")

#! Another way to create lists is using list() constructor
myList = list(("Apple", "Banana", "Prayas", 101, False))
print(myList)