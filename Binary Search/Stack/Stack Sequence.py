# https://binarysearch.com/problems/Stack-Sequence
class Solution:
    def solve(self, pushes, pops):
        stack = []
        idx,jdx = 0,0
        push_len = len(pushes)
        while True:
            while stack and stack[-1] == pops[jdx]:
                stack.pop()
                jdx += 1
            if idx == push_len:
                break
            stack.append(pushes[idx])
            idx +=1
        return len(stack) == 0