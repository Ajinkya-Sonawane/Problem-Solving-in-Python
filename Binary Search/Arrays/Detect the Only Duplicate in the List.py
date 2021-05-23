# https://binarysearch.com/problems/Detect-the-Only-Duplicate-in-a-List
class Solution:
    def solve(self, nums):
        ans = 0
        for i in range(1, max(nums) + 1):
            ans ^= i
        for i in range(len(nums)):
            ans ^= nums[i]
        return ans