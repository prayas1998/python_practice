thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist.insert(1, "banana")
print("--------------------------------------------------------")


#! Remove Specified Index

thislist.pop(0)
print(thislist)

thislist.insert(0,"apple")

print("--------------------------------------------------------")

#! Remove the last item
thislist.pop()
print(thislist)

thislist.insert(2,"cherry")

print("-----------------------------------------------------------")

#! The del keyword can also delete the list completely.

# del thislist

#! CLear the list

thislist.clear()
print(thislist) #! prints []