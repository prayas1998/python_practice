def myfunc():
    global x #! If you use the global keyword, the variable belongs to the global scope.
    x = 400
    print(x)

myfunc()
print(x)