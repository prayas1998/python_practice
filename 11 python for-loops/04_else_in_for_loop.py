# Else in For Loop

#! The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
    print(x)
else:
    print("Finished")


print("-----------------------")
#! Note: The else block will NOT be executed if the loop is stopped by a break statement

for y in range(6):
    if y == 3:
        break
    print(y)
else:
    print("this will not be printed!")