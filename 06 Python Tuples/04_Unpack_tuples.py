fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

print("------------------------------------------------")

#! Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

print("------------------------------------------------")
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)