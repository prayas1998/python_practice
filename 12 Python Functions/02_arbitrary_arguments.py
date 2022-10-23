# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a #!tuple of arguments, and can access the items accordingly:

def myFunction(*child):
    print("The youngest child is " + child[2])

myFunction("Etawah", "Piyush", "Bhalia")