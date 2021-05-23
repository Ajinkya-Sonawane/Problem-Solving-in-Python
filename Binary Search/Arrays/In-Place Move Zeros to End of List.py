# https://binarysearch.com/problems/In-Place-Move-Zeros-to-End-of-List
class Solution:
    def solve(self, nums):
        start = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[start],nums[idx] = nums[idx],nums[start]
                start += 1
        return nums