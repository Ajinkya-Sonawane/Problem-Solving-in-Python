# https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = []
        res = []
        total = len(nums)
        def backtrack(temp: List[int]):
            if len(stack) == total:
                res.append(stack.copy())
                return
            for num in temp:
                stack.append(num)
                x = temp.copy()
                x.remove(num)
                backtrack(x)
                stack.pop()
        backtrack(nums)
        return res