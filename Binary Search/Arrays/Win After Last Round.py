# https://binarysearch.com/problems/Win-After-Last-Round
class Solution:
    def solve(self, nums):
        nums.sort(reverse=True)
        try:
            cut = max(num + i for i, num in enumerate(nums, 1))
        except ValueError:
            return 0
        x = len(nums)
        for i, num in enumerate(nums):
            if num + x < cut:
                return i
        return len(nums)
