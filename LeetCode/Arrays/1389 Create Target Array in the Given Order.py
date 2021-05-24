# https://leetcode.com/problems/create-target-array-in-the-given-order/
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for idx,num in enumerate(nums):
            res.insert(index[idx],num)
        return res
            