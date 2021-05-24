class Solution:
    def solve(self, s1, s2):
        idx1,idx2 = 0,0
        s1Len,s2Len = len(s1),len(s2)
        while idx1 < s1Len and idx2 < s2Len:
            if s1[idx1] == s2[idx2]:
                idx1 += 1
            idx2 += 1
        return idx1 == s1Len