# https://binarysearch.com/problems/Remove-Duplicates-in-Linked-List
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        head = node
        prev = None
        res = {}
        while node:
            if res.get(node.val,0):
                if prev == None:
                    head = node.next
                else:
                    prev.next = node.next
            else:
                res[node.val] = 1
                prev = node
            node = node.next
        return head                