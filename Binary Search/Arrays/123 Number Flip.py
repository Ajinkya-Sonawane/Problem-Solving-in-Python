# https://binarysearch.com/problems/123-Number-Flip
class Solution:
    def solve(self, n):
        li = list(str(n))
        for idx,val in enumerate(li):
            if val != '3':
                li[idx] = '3'
                return int(''.join(li))
        return n