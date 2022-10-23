thistuple = ("apple", "banana", "mango")
print(thistuple)

#! Tuples Allow Duplicates

thistuple = ("apple", "banana", "mango", "cherry", "apple")
print(thistuple)
print(len(thistuple))

print("-----------------------------------------")

#! Create Tuple With One Item
#! To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

print("-----------------------------------------")

#! Tuple data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

print("-----------------------------------------")
#! A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)