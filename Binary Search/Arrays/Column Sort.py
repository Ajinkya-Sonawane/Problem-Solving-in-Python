# https://binarysearch.com/problems/Column-Sort
class Solution:
    def solve(self, matrix):
        res = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        for row in res:
            row.sort()
        
        res = [[res[j][i] for j in range(len(res))] for i in range(len(res[0]))]
        return res