# https://binarysearch.com/problems/Square-of-a-List
class Solution:
    def solve(self, nums):
        for idx,num in enumerate(nums):
            nums[idx] = num**2
        return sorted(nums)