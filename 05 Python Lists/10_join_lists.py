list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

newList = list1 + list2
print(newList)

print("----------------------2nd method----------------------")

#! Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for item in list2:
    list1.append(item)
print(list1)

print("----------------------3rd method----------------------")

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)