def search(nums, left, right, target):
    if not nums:
        return -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            return search(nums, left, mid - 1, target)
        else:
            return search(nums, mid + 1, right, target)

    return -1


nums = [2, 3, 4, 5, 6, 7, 8]
target = 10

print(search(nums, 0, len(nums) - 1, target))
