# https://binarysearch.com/problems/First-Fit-Room
class Solution:
    def solve(self, rooms, target):
        for num in rooms:
            if num >= target:
                return num
        return -1