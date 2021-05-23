# https://binarysearch.com/problems/Linked-List-to-Integer
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        res = 0
        while True:
            res ^= node.val
            node = node.next
            if not node:
                return res
            res <<= 1