class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("Prayas", 24)

print(p1.name)
print(p1.age)


#! The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class