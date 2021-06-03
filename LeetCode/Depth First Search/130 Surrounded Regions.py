# https://leetcode.com/problems/surrounded-regions/
class Solution:
    def dfs(self,board,i,j):
        if 0 <= i < self.rows and 0 <= j < self.cols and board[i][j] == 'O':
            board[i][j] = 'A'
            self.dfs(board,i+1,j)
            self.dfs(board,i-1,j)
            self.dfs(board,i,j+1)
            self.dfs(board,i,j-1)
            
    def solve(self, board: List[List[str]]) -> None:
        self.rows = len(board)
        self.cols = len(board[0])

        for idx in range(0,self.rows):
            if board[idx][0] == 'O':
                self.dfs(board,idx,0)
            if board[idx][self.cols-1] == 'O':
                self.dfs(board,idx,self.cols-1)

        for idx in range(0,self.cols):
            if board[0][idx] == 'O':
                self.dfs(board,0,idx)
            if board[self.rows-1][idx] == 'O':
                self.dfs(board,self.rows-1,idx)

        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
