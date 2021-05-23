# https://binarysearch.com/problems/Longest-Alliteration
class Solution:
    def solve(self, words):
        if not words:
            return 0
        if len(words)== 1:
            return 1
        mxcnt=1
        cnt=1
        prev = words[0][0]
        for i in range(1,len(words)):
            if words[i][0] == prev:
                cnt+=1
                mxcnt=max(mxcnt,cnt)
            else:
                prev = words[i][0]
                cnt = 1

        mxcnt=max(mxcnt,cnt)
        return mxcnt