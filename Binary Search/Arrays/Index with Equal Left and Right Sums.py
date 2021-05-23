# https://binarysearch.com/problems/Index-with-Equal-Left-and-Right-Sums
class Solution:
    def solve(self, nums):
        left,right = 0,sum(nums)
        for idx,val in enumerate(nums):
            if left == (right-val):
                return idx
            left += val
            right -= val
        return -1