fruits = ["apple", "banana", "cherry"]

#!Do not print banana:
for items in fruits:
    if items == "banana":
        continue
    print(items)

#! With the continue statement we can stop the current iteration of the loop, and continue with the next: