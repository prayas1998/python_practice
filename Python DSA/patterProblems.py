def pattern1(n):
    '''
    * * * * * 
    * * * * * 
    * * * * * 
    * * * * * 
    * * * * * 
    '''
    for i in range(1, n+1):
        for j in range(1, n+1):
            print("* ", end="")
        print()

def pattern2(n):
    '''
    * 
    * * 
    * * * 
    * * * * 
    * * * * *
    '''
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()

def pattern3(n):
    '''
    1 
    1 2 
    1 2 3 
    1 2 3 4 
    1 2 3 4 5 
    '''
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

def pattern4(n):
    '''
    1 
    2 2 
    3 3 3 
    4 4 4 4 
    5 5 5 5 5 
    '''
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end=" ")
        print()

def pattern5(n):
    '''
    * * * * * 
    * * * * 
    * * * 
    * * 
    * 
    '''
    for i in range(1, n+1):
        for j in range(1, (n-i)+2):
            print("*", end=" ")
        print()

def pattern6(n):
    '''
    1 2 3 4 5 
    1 2 3 4 
    1 2 3 
    1 2 
    1
    '''
    for i in range(1, n+1):
        for j in range(1, (n-i)+2):
            print(j, end=" ")
        print()

def pattern7(n):
    '''
        *    
       ***   
      *****  
     ******* 
    *********
    '''
    for i in range(1, n+1):
    # First inner loop
        for j in range(1, n-i+1):
            print(" ", end="")
        for j in range(1, 2*i-1+1):
            print("*", end="")
        for j in range(1, n-i+1):
            print(" ", end="")
        print()

def pattern8(n):
    '''
    *********
     *******
      *****
       ***
        *
    '''
    for i in reversed(range(1, n+1)):
        for j in range(1, n-i+1):
            print(" ", end="")
        for j in range(1, i+1):
            print("*", end="")
        for j in range(2, i+1):
            print("*", end="")
        print()

def pattern9(n):
    ''' 
     *
    ***
   *****
  *******
  *******
   *****
    ***
     *
    '''
    for i in range(1, n+1):
        for j in range(1, n-i+1):
            print(" ", end="")
        for j in range(1, i+1):
            print("*", end="")
        for j in range(2, i+1):
            print("*", end="")
        print()
    for i in reversed(range(1, n+1)):
        for j in range(1, n-i+1):
            print(" ", end="")
        for j in range(1, i+1):
            print("*", end="")
        for j in range(2, i+1):
            print("*", end="")
        print()

def pattern10(n):
    '''
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
    '''
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end="")
        print()

    for i in range(1, n):
        for j in range(1, n-i+1):
            print("*", end="")
        
        print()

def pattern11(n):
    '''
    1 
    0 1 
    1 0 1 
    0 1 0 1 
    1 0 1 0 1
    '''
    for i in range(1, n+1):
        for j in range(1, i+1):
            if (i+j)%2 == 0:
                print('1', end=" ")
            else:
                print('0', end=" ")
        print()

def pattern12(n):
    '''
    1 - - - - - - 1 
    1 2 - - - - 2 1 
    1 2 3 - - 3 2 1 
    1 2 3 4 4 3 2 1

    '''


    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        
        for j in range(2, n-i+2):
            print(" ", end=" ")

        for j in range(2, n-i+2):
            print(" ", end=" ")
            
        for j in reversed(range(1, i+1)):
            print(j, end=" ")
            
        print()

def pattern13(n):
    '''
    1
    2  3
    4  5  6
    7  8  9  10
    11 12 13 14 15
    '''
    count = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(count, end=" ")
            count = count + 1
        print()

def pattern19(n):
    '''
    * * * * * * 
    * *     * * 
    *         * 
    *         * 
    * *     * * 
    * * * * * *
    '''
    # Upper half
    for i in range(1, n+1):
        # Stars
        for j in range(1, n-i+1 + 1):
            print("*", end="")
        
        # spaces
        for j in range(1, i-1 + 1):
            print(" ", end=" ")
        # Stars
        for j in range(1, n-i+1 + 1):
            print("*", end="")
        print()
    
    # Lower half
    for i in reversed(range(1, n+1)):
        # Stars
        for j in range(1, n-i+1 + 1):
            print("*", end="")
        
        # spaces
        for j in range(1, i-1 + 1):
            print(" ", end=" ")
        # Stars
        for j in range(1, n-i+1 + 1):
            print("*", end="")
        print()

def pattern20(n):
    # Upper half
    for i in range(1, n+1):
        # Stars
        for j in range(1, i+1):
            print("*", end=" ")
        
        # Spaces
        for j in range(1, 2*(n-i)+1):
            print(" ", end=" ")
        
        # Stars
        for j in range(1, i+1):
            print("*", end=" ")
        print()
    
    # lower half
    for i in reversed(range(1, n)): # Because rows in lower half is (n-1)
        # Stars
        for j in range(1, i+1):
            print("*", end=" ")
        
        # Spaces
        for j in range(1, 2*(n-i)+1):
            print(" ", end=" ")
        
        # Stars
        for j in range(1, i+1):
            print("*", end=" ")
        print()

def pattern21(n):

    ''' 
    * * * *
    *     *
    *     *
    * * * *
    '''
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == 1 or i == n or j == 1 or j == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def pattern22(n):
    '''
    given: n=4
    
    4444444
    4333334
    4322234
    4321234
    4322234
    4333334
    4444444
    '''
    pass

# pattern1(5)
# pattern2(5)
# pattern3(5)
# pattern4(5)
# pattern5(5)
# pattern6(5)
# pattern7(5)
# pattern8(5)
# pattern9(5)
# pattern10(5)
# pattern11(5)
# pattern12(4)
# pattern13(5)
# pattern14(5)
# pattern15(5)
# pattern16(5)
# pattern17(5)
# pattern18(5)
# pattern19(3)
# pattern20(5)
# pattern21(5)
