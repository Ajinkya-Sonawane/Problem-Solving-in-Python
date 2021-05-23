# https://binarysearch.com/problems/Kth-Smallest-Element
class Solution:
    def solve(self, nums, k):
        heapq.heapify(nums)
        while k:
            heapq.heappop(nums)
            k -= 1
        return heapq.heappop(nums)