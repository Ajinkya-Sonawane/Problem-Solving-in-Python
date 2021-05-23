# https://binarysearch.com/problems/Replace-Linked-List-on-Index
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, a, b, lo, hi):
        head = a
        cnt = 0
        h1 = None
        while cnt <= hi:
            if cnt == lo-1:
                h1 = a
            a = a.next
            cnt += 1
        if not h1:
            head = b
        else:
            h1.next = b
        while b.next:
            b = b.next
        b.next = a
        return head