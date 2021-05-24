# https://leetcode.com/problems/decompress-run-length-encoded-list/
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for idx in range(0,len(nums),2):
            res.extend([nums[idx+1]]*nums[idx])
        return res