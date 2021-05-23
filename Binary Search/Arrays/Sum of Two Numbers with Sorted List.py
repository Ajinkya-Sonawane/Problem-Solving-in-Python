# https://binarysearch.com/problems/Sum-of-Two-Numbers-with-Sorted-List
class Solution:
    def solve(self, nums, k):
        start,end = 0,len(nums)-1
        while start < end:
            val = nums[start]+nums[end] 
            if val == k:
                return True
            elif val < k:
                start += 1
            else:
                end -= 1
        return False
