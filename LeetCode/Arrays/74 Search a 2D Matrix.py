class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix[0])-1
        while i < len(matrix) and j >= 0:
            val = matrix[i][j]
            if val == target:
                return True
            if val > target:
                j-=1
            else:
                i+=1
        return False