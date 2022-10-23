thislist = ["apple", "banana", "cherry"]

for i in thislist:
    print(i)

print("-----------------------------------------------")

print(len(thislist))
for x in range(len(thislist)):
    print(thislist[x])
    
print("-----------------------------------------------")

j = 0
while j<len(thislist):
    print(thislist[j])
    j = j + 1

print("-----------------------------------------------")

#! Shorthand for property to print all items in the list
[print(w) for w in thislist]