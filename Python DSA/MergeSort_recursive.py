import math


def mergeSort(arr):
    # base case:
    if len(arr) <= 1:
        return arr

    # mid = math.floor(len(arr) / 2)

    mid = len(arr) // 2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = mergeSort(left_arr)
    right_arr = mergeSort(right_arr)

    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    result = []
    i, j = 0, 0  # 'i' and 'j' are indices of left_arr and right_arr resp.

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1

    # for the left out elements in left_arr list:
    for item in left_arr[i:]:
        result.append(item)

    # for the left out elements in right_arr list:
    for item in right_arr[j:]:
        result.append(item)

    return result


arr1 = [5, 7, 10, 3, 6, 2, 11, 1]
print(mergeSort(arr1))
