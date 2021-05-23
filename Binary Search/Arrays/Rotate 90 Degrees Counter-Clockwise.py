# https://binarysearch.com/problems/Rotate-by-90-Degrees-Counter-Clockwise
class Solution:
    def solve(self, matrix):
        if not matrix or not matrix[0]:
            return []
        n = len(matrix)
        for row in matrix:
            row.reverse()
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        return matrix