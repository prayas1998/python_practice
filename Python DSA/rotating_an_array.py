# [ 2, 3, 4, 5, 6 ]

def rev(arr, i, j):
    while i <= j:
        temp = arr[i]
        arr[i] = temp
        arr[i] = arr[j]
        arr[j] = temp
        i = i + 1
        j = j - 1
    return arr


def rotate(arr, d):
    rev(arr, 0, d - 1)
    rev(arr, d, len(arr) - 1)
    rev(arr, 0, len(arr) - 1)
    return arr


arr = [2, 3, 4, 5, 6, 1]
d = 3
# ans = [ 5, 6, 1, 2, 3, 4 ]

print(rotate(arr, d))
