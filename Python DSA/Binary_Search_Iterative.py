# Iterative approach

import math


def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = math.floor((start + end) / 2)

        if arr[mid] == target:
            return f"target is present at index: {mid}"

        elif arr[mid] < target:
            start = mid + 1

        else:
            end = mid - 1

    return -1


nums = [1, 3, 5, 7, 9, 11]
target = 7

print(binarySearch(nums, target))
