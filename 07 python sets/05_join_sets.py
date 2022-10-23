set1 = {False, 'cherry', '24', 'apple'}
set2 = {1,2,3, 'cherry'}

set3 = set1.union(set2)
print(set3)

print("-----------------------------------")

#! Intersection updates : Keep ONLY the Duplicates
#! The intersection_update() method will keep only the items that are present in both sets.

# set1.intersection_update(set2)
print(set1)

set4 = set1.intersection(set2)
print(set4)

print("-----------------------------------")


#! symmetric difference : Keep All, But NOT the Duplicates 
#! The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

# set1.symmetric_difference_update(set2)
print(set1)

set5 = set1.symmetric_difference(set2)
print(set5)