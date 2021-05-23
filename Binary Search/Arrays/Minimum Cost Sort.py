# https://binarysearch.com/problems/Minimum-Cost-Sort
class Solution:
    def solve(self, nums):
        tmpasc = sorted(nums)
        tmpdes = sorted(nums,reverse=True)
        asc,des = 0,0
        for idx,val in enumerate(nums):
            asc += abs(tmpasc[idx]-val)
            des += abs(tmpdes[idx]-val)
        return min(asc,des)