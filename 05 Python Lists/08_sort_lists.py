thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #! sorts list alphanumerically (ascending order)
print(thislist)

numlist = [100, 50, 65, 82, 23]
numlist.sort() #! sorts list alphanumerically (ascending order)
print(numlist)

print("--------------------------------------------")

#! for descending order: 
thislist1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
numlist1 = [100, 50, 65, 82, 23]

thislist1.sort(reverse=True)
numlist1.sort(reverse=True)

print(thislist1)
print(numlist1)

print("--------------------------------------------")

#! By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
#! Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#! We can use built-in functions as key functions when sorting a list.
#! So if you want a case-insensitive sort function, use str.lower as a key function:
thislist.sort(key = str.lower)
print(thislist)

print("--------------------------------------------")

#! Reverse order 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)