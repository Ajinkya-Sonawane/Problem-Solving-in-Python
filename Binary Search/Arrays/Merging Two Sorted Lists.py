# https://binarysearch.com/problems/Merging-Two-Sorted-Lists
class Solution:
    def solve(self, a, b):
        a_idx,b_idx = 0,0
        res = []
        while a_idx < len(a) and b_idx < len(b):
            if a[a_idx] <= b[b_idx]:
                res.append(a[a_idx])
                a_idx += 1
            else:
                res.append(b[b_idx])
                b_idx += 1
        return res + a[a_idx:] + b[b_idx:]