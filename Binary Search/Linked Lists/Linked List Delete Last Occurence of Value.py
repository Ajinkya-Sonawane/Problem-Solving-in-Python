# https://binarysearch.com/problems/Linked-List-Delete-Last-Occurrence-of-Value
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, target):
        head = node
        prev= None
        del_prev = None
        del_node = None
        while node:
            if node.val == target:
                del_prev = prev
                del_node = node                
            prev= node
            node=node.next
        if del_node:
            if not del_prev:
                head = del_node.next
            else:
                del_prev.next = del_node.next
        return head