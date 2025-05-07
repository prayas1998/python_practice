'''#!Question:
Print array after it is right rotated K times
Given an Array of size N and a value K, around which we need to right rotate the array. How do you quickly print the right rotated array?
#link: https://www.geeksforgeeks.org/print-array-after-it-is-right-rotated-k-times/
#! Examples:
Input: Array[] = {1, 3, 5, 7, 9}, K = 2.
Output: 7 9 1 3 5
Explanation:
After 1st rotation – {9, 1, 3, 5, 7}After 2nd rotation – {7, 9, 1, 3, 5}
-------------------------------------------------------------------------------
Input: Array[] = {1, 2, 3, 4, 5}, K = 4.
Output: 2 3 4 5 1      
'''

'''
Logic:
1. Find mod of k. Because array will be same when returned N times. N is the length of array.
2. Reverse the complete array.
3. Reverse from index 0 to index (k-1)
4. Reverse from index k to (n-1)
'''

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
