# With the break statement we can stop the loop before it has looped through all the items:

fruits = ["apple", "banana", "cherry"]
for items in fruits:
    print(items)
    if items == "banana":
        break

print("--------------------")
#! Exit the loop when x is "banana", but this time the break comes before the print:

for x in fruits:
    if x == "banana":
        break
    print(x)