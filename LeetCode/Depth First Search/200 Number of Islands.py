# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        rows = len(grid)
        cols = len(grid[0])
        def invert(i,j):
            if i < rows and i >= 0 and j < cols and j >= 0:
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    invert(i-1,j)
                    invert(i+1,j)
                    invert(i,j-1)
                    invert(i,j+1)
        
        for i in range(0,rows):
            for j in range(0,cols):
                if grid[i][j] == "1":
                    invert(i,j)
                    cnt += 1
        return cnt