# https://binarysearch.com/problems/Swap-Consecutive-Index-Pairs
class Solution:
    def solve(self, nums):        
        p1,p2 = 0,1
        while p1+2 < len(nums):
            nums[p1],nums[p1+2] = nums[p1+2],nums[p1]
            p1 += 4
        while p2+2 < len(nums):
            nums[p2],nums[p2+2] = nums[p2+2],nums[p2]            
            p2 += 4
        return nums