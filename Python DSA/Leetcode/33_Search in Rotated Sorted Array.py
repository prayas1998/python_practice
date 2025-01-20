# Search in a rotated sorted array:

# arr = [4,5,6,7,0,1,2]

def search(arr, target):
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # base case of simple binary search
        if arr[mid] == target:
            return mid

        # Modified binary search
        # check if left array is sorted
        if arr[left] <= arr[mid]:
            # Check if target is in left range:
            if arr[left] <= target < arr[mid]:  # target is present in left range [4,6]
                right = mid - 1
            else:  # target is present in right range [0,1]
                left = mid + 1

        # if right array is sorted:
        else:
            if arr[mid] < target <= arr[right]:  # target is present in right range [0,1]
                left = mid + 1
            else:  # target is present in left range [4,6]
                right = mid - 1

    # if target is not found:
    return -1


arr = [4, 5, 6, 7, 0, 1, 2]

target = 2
print(search(arr, target))
