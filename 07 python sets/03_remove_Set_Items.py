mySet = {False, 'cherry', '24', 'apple', 'prayas', 'banana', 24, 'mango', 'orange'}
mySet1 = {False, '24', 'apple', 'prayas', 'banana', 24, 'mango', 'orange'}

mySet.remove(False)
mySet.remove(24)
mySet.discard('banana') #! If the item to remove does not exist, discard() will NOT raise an error.
print(mySet)

mySet1.clear() #! Empties the set
print(mySet1)

del mySet1 #! Deletes the set compeletely
