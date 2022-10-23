class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("Prayas", "Gautam")
x.printname()

class Student(Person): #! syntax for creating child class
    pass
#! Now the Student class has the same properties and methods as the Person class.


#! Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
class Student1(Person):
    def __init__(self, fname, lname): #! When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
        self.fname = fname
        self.lname = lname

    def print(self):
        print(self.fname, self.lname)


#! To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Student2(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x1 = Student1("Piyush", "Saini")
x1.print()

x2 = Student2("Prashant", "Gaurav")
x2.printname()
