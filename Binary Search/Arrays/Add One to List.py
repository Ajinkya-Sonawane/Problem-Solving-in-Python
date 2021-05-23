# https://binarysearch.com/problems/Add-One-to-List
class Solution:
    def solve(self, nums):
        idx = len(nums)-1
        carry = 0
        nums[idx] += 1
        while idx >= 0:
            sum_ = nums[idx] + carry
            nums[idx] = sum_ % 10
            carry = sum_ // 10
            idx -= 1
        if carry:
            nums.insert(0,1)
        return nums