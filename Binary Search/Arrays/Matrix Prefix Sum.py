# https://binarysearch.com/problems/Matrix-Prefix-Sum
class Solution:
    def solve(self, matrix):
        res = []
        if not matrix:
            return matrix
        for x in matrix:
            if not x:
                return matrix          
            res.append(x.copy())
        row_len = len(matrix)
        col_len = len(matrix[0])

        for i in range(1,row_len):
            res[i][0] = res[i-1][0] + matrix[i][0]
        for j in range(1,col_len):
            res[0][j] = res[0][j-1] + matrix[0][j]
        print(res)
        for i in range(1,row_len):
            for j in range(1,col_len):
                      res[i][j] = res[i-1][j] + res[i][j-1] - res[i-1][j-1] + matrix[i][j]
        return res