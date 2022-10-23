thistuple = ("apple", "banana", "cherry")
for items in thistuple:
    print(items)

print("------------------------------------")

#! Loop Through the Index Numbers
for i in range(len(thistuple)):
    print(thistuple[i])

print("------------------------------------")
thistuple1 = ("apple", "banana", "cherry")
#! using a while loop
j = 0
while j<len(thistuple1):
    print(thistuple1[j])
    j += 1