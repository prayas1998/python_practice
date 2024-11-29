def palindrome(x: int):
    if x < 0:
        return False

    temp = x
    reverse = 0
    while x > 0:
        digit = x % 10  # to find the last digit
        reverse = (reverse * 10) + digit
        x = x // 10

    if temp == reverse:
        return True
    else:
        return False


print(palindrome(121))
