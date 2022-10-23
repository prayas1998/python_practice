#A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myfunc():
    x = 400
    print(x)

myfunc()


print("___________Function Inside Function__________")

def myfunc1():
    y = 500
    
    def innerfunc():
        print(y)
    innerfunc()

myfunc1()