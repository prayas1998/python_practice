# Recursive approach

import math


def binarySearch(arr, start, end, target):
    mid = math.floor((start + end) / 2)

    if start > end:
        return "Cannot find number"

    if arr[mid] == target:
        return f"target is at index: {mid}"

    elif target > arr[mid]:
        return binarySearch(arr, mid + 1, end, target)

    else:
        return binarySearch(arr, start, mid - 1, target)


nums = [1, 3, 5, 7, 9, 11]
target = 7

print(binarySearch(nums, 0, len(nums) - 1, target))
