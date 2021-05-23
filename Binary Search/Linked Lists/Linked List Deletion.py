# https://binarysearch.com/problems/Linked-List-Deletion
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, target):
        head = node
        prev = None
        while node:
            if node.val == target:
                if prev == None:
                    head = node.next
                else:
                    prev.next = node.next
            else:
                prev = node
            node = node.next
        return head