# https://binarysearch.com/problems/Unidirectional-Word-Search
class Solution:
    def solve(self, board, word):
        idx = 0
        rows = len(board)
        cols = len(board[0])
        word_len = len(word)
        idx = 0
        for i in range(rows):
            idx = 0
            for j in range(cols):
                if board[i][j] == word[idx]:
                    idx += 1
                if idx == word_len:
                    return True
        for i in range(cols):
            idx = 0
            for j in range(rows):
                if board[j][i] == word[idx]:
                    idx += 1
                if idx == word_len:
                    return True
        return False