# Count digits: https://www.naukri.com/code360/problems/count-digits_8416387

def countDigits(n):
    count = 0
    # Convert n to string to iterate through digits
    for i in str(n):
        if int(i) != 0 and n % int(i) == 0:
            count += 1
    return count

n = 660
print(countDigits(n))