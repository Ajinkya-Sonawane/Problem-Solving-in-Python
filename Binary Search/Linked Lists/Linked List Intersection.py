# https://binarysearch.com/problems/Linked-List-Intersection
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, l0, l1):
        head = LLNode(0,None)
        sentinal = head
        while l0 and l1:
            if l0.val == l1.val:
                sentinal.next = l0
                sentinal = l0
                l0 = l0.next
                l1 = l1.next
                sentinal.next = None
            elif l0.val > l1.val:
                l1 = l1.next
            else:
                l0 = l0.next
        return head.next