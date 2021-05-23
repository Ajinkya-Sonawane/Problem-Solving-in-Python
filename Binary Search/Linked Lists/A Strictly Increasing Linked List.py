# https://binarysearch.com/problems/A-Strictly-Increasing-Linked-List
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head):
        prev = head
        head = head.next
        while head:
            if head.val <= prev.val:
                return False
            prev = head
            head = head.next
        return True
