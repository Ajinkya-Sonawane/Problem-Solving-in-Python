# https://leetcode.com/problems/word-search/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])
        word_len = len(word)
        def dfs(i,j,idx):
            if idx == word_len:
                return True
            if 0<=i<rows and 0<=j<cols:
                if board[i][j] == word[idx]:
                    board[i][j] = 1
                    a = dfs(i+1,j,idx+1)
                    b = dfs(i,j+1,idx+1)
                    c = dfs(i-1,j,idx+1)
                    d = dfs(i,j-1,idx+1)
                    board[i][j] = word[idx]
                    return a or b or c or d
            return False
        
        for row in range(rows):
            for col in range(cols):
                if dfs(row,col,0):
                    return True
        return False