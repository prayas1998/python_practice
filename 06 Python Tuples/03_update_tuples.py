# Change Tuple Values
#! Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#! But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

myTuple = ("apple", "car", "bike", "mango")
myList = list(myTuple) #! Prints as list
print(myList)
myList[1] = "scooter"
myTuple = tuple(myList) #! Prints as tuple
print(myTuple)

#! Delete a tuple completely
myTuple = ("apple", "car", "bike", "mango")
del myTuple