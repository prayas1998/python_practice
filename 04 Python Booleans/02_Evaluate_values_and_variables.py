print(bool("Hello"))
print(bool(10))

print("------------------------------------------------------------------------------------")


#! Evaluate two variables:
x = 10
y = 15

print(bool(x))
print(bool(y))

print("-------------------------------------------------------------------------------------")

#! Almost any value is evaluated to True if it has some sort of content.
#! Any string is True, except empty strings.
#! Any number is True, except 0.
#! Any list, tuple, set, and dictionary are True, except empty ones.

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print("-------------------------------------------------------------------------------------")

#! Some Values are False
#! In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))