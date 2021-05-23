# https://binarysearch.com/problems/K-Prefix
class Solution:
    def solve(self, nums, k):
        for i in range(1,len((nums))):
            nums[i] = nums[i-1] + nums[i]

        for idx in range(len(nums)-1,-1,-1):
            if nums[idx] <= k:
                return idx
        return -1