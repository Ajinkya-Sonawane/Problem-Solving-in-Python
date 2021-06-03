# https://leetcode.com/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.cnt = 0
        mat = [[1]*n for _ in range(0,m)]
        for row in range(1,m):
            for col in range(1,n):
                mat[row][col] = mat[row-1][col] + mat[row][col-1]
        return mat[-1][-1]
        