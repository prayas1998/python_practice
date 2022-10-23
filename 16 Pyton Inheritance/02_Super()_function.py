# Super Function
#! Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

#! By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)


class Student(Person):
    def __init__(self,fname,lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def printStudent(self):
        print(self.fname, self.lname, self.graduationyear)


x = Student("Prayas", "Gautam", 2022)
x.printStudent()