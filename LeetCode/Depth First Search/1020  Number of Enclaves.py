# https://leetcode.com/problems/number-of-enclaves/
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        def dfs(i,j):
            if 0<= i<rows and 0<=j<cols:
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    dfs(i+1,j)
                    dfs(i-1,j)
                    dfs(i,j-1)
                    dfs(i,j+1)

        #Traverse first and last column
        for row in range(rows):
            if grid[row][0]:
                dfs(row,0)
            if grid[row][cols-1]:
                dfs(row,cols-1)
        #Traverse first and last row
        for col in range(cols):
            if grid[0][col]:
                dfs(0,col)
            if grid[rows-1][col]:
                dfs(rows-1,col)
        cnt=0
        #Traverse entire grid to see if any land (1) still exists
        for row in grid:
            for col in row:
                if col == 1:
                    cnt +=1
        return cnt