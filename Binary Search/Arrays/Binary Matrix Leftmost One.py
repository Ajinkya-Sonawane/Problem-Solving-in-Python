# https://binarysearch.com/problems/Binary-Matrix-Leftmost-One
class Solution:
    def solve(self, matrix):
        r = 0
        c = len(matrix[0]) - 1 if matrix else 0
        ans = -1

        while r < len(matrix) and c >= 0:
            if matrix[r][c] == 1:
                ans = c
                c -= 1
            else:
                r += 1
        return ans