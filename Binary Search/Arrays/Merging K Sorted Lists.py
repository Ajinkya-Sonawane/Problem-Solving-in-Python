# https://binarysearch.com/problems/Merging-K-Sorted-Lists
class Solution:
    def solve(self, lists):
        min_heap = []

        for i in range(len(lists)):
            if len(lists[i]) > 0:
                heapq.heappush(min_heap, (lists[i][0], i, 0))

        res = []

        while len(min_heap) > 0:
            a, i, j = heapq.heappop(min_heap)

            if j + 1 < len(lists[i]):
                heapq.heappush(min_heap, (lists[i][j + 1], i, j + 1))

            res.append(a)

        return res
