'''The format() method allows you to format selected parts of a string.
Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?
To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:'''


print("-------------Example 1---------------")

#! Example 1:
age = 23
name = "Prayas"
place = "Faridabad"

txt = "My name is Prayas, and I am {}."
print(txt.format(age))

txt1 = "His name is {1}. {1} is {0} years old and lives in {2}."
print(txt1.format(age,name,place))

txt2 = "{name} owns {carName}. It's a {year} model."
print(txt2.format(carName = "Honda Amaze", name = "Prayas", year = "2018"))



print("--------------Example 2-------------")
#! Example 2: 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 

print("--------------Example 3-------------")
#! Example 3: 

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


print("--------------Example 4-------------")
#! Format the price to be displayed as a number with two decimals:
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))