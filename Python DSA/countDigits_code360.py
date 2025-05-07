'''
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
'''

n = 5

for i in range(1, n+1):
    # First inner loop
    for j in range(1, n-i+1):
        print(" ", end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    for j in range(2, i+1):
        print("*", end=" ")
    print()
    
for i in reversed(range(1, n+1)):
    # First inner loop
    for j in range(1, n-i+1):
        print(" ", end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    for j in range(2, i+1):
        print("*", end=" ")
    print()