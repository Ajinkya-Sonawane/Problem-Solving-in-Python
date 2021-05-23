# https://binarysearch.com/problems/Fixed-Point
class Solution:
    def solve(self, nums):
        ret = -1
        lhs = 0
        rhs = len(nums) - 1
        while lhs <= rhs:
            mid = (lhs + rhs) // 2
            if nums[mid] == mid:
                ret = mid
            if nums[mid] >= mid:
                rhs = mid - 1
            else:
                lhs = mid + 1
        return ret 