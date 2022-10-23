# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:

def myFunc(country = "India"):
    print("I am from " + country)

myFunc("USA")
myFunc() #! Prints India
myFunc("Germany")

