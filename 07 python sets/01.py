thisSet = {"apple", "banana", "cherry"}
print(thisSet)


#! Duplicate values will be ignored:

thisSet1 = {"apple", "banana", "cherry", "apple"}
print(thisSet1)
print(len(thisSet1))

#!A set can contain different data types:

thisSet2 = {"apple", "Prayas", True, 108}
print(thisSet2)

print(type(thisSet))

thisSet3 = set(("apple", "Prayas", True, 108))
print(thisSet3)