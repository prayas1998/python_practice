# Reverse array k times:

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3


def rotateKTimes(nums, k):
    k = k % (len(nums)) # this will help if k > length of array
    def reverse(nums, i, j):
        while i <= j:
            temp = 0
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i = i + 1
            j = j - 1

    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)
    return nums


print(rotateKTimes(nums, k))
