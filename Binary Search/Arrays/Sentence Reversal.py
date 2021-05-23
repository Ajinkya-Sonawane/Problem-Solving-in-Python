# https://binarysearch.com/problems/Sentence-Reversal
class Solution:
    def solve(self, sentence):
        x = ''.join(sentence)
        x = x.split(' ')
        x = x[::-1]
        res = []
        for world in x:
            for char in world:
                res.append(char)
            res.append(" ")
        return res[:-1]