print("-------Example 1---------")

def myFunct(n):
    return lambda a : a*n

doubler = myFunct(2)
print(doubler(11)) #! 22




print("-------Example 2---------")

def myFunct1(n):
    return lambda b : b*n

tripler = myFunct1(3)
print(tripler(11)) #! 33




print("-------Example 3---------")
#! use the same function definition to make both functions, in the same program:

def myFunct2(n):
    return lambda c : c*n

doubler1 = myFunct2(2)
tripler = myFunct2(3)

print(doubler(11))
print(tripler(11))