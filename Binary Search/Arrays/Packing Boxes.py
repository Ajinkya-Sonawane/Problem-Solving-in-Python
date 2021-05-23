# https://binarysearch.com/problems/Packing-Boxes
class Solution:
    def solve(self, nums):
        if not nums:
            return []
        pidx = 0
        res = []
        prev = nums[0]
        max_i = len(nums)-1
        for idx,num in enumerate(nums):
            if num != prev:
                res.append(nums[pidx:idx])
                pidx = idx                
            prev = num
        if nums:
            res.append(nums[pidx:idx+1])
        return res      
