# https://binarysearch.com/problems/Mixed-Sorting
class Solution:
    def solve(self, nums):
        even = []
        odd = []
        for x in nums:
            if x%2:
                even.append(x)
            else:
                odd.append(x)
        even = sorted(even)
        odd = sorted(odd,reverse=True)
        for idx,x in enumerate(nums):
            if x%2:
                nums[idx] = even.pop()
            else:
                nums[idx] = odd.pop()
        return nums
