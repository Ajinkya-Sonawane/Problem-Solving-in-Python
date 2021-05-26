# https://binarysearch.com/problems/Insert-Into-Linked-List
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head, pos, val):
        prev = None
        node = head
        while pos:
            prev = node
            node = node.next
            pos -=1        
        if pos == 0:
            if not prev:
                head = LLNode(val,node)
            else:
                prev.next = LLNode(val,node)
        return head