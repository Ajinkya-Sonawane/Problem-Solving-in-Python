# 
class Solution:
    def solve(self, a, b):
        # return bin(int(a,2) + int(b,2))[2:]
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ans = ""
        while i >= 0 or j >= 0:
            sm = 0
            if i >= 0:
                sm += int(a[i])
                i -= 1
            if j >= 0:
                sm += int(b[j])
                j -= 1
            if carry:
                sm += 1
            carry = sm // 2
            sm = sm % 2
            ans = str(sm) + ans
        if carry == 1:
            ans = "1" + ans
        return ans