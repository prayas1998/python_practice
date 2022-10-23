class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print(f"Hello! My name is {self.name} and I'm {self.age} years old")

p1 = person("Prayas", 24)
p1.myFunc()
