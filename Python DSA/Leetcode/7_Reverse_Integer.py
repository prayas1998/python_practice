def reverse(x):
    sign = -1 if x < 0 else 1
    x = x * sign
    reverse = 0
    while x > 0:
        digit = x % 10  # to find the last digit
        reverse = (reverse * 10) + digit
        x = x // 10

    return 0 if reverse < -2 ** 31 or reverse > 2 ** 31 - 1 else sign * reverse


print(reverse(123))
