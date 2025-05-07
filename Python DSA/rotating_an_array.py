# Rotate an array around a pivot piont
'''
An ARRAY and a PIVOT POINT is gives around which we have to rotate the array.
Logic:
1. Reverse from index 0 to index (d-1)
2. Reverse from index d to (n-1)
3. Reverse the complete array from index 0 to (n-1)
'''

def rev(arr, i, j):
    while i <= j:
        temp = arr[i]
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
