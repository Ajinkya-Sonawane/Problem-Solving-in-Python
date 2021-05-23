# https://binarysearch.com/problems/Interleaved-Linked-List
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, l0, l1):
        temp0 = l0
        temp1 = l1
        sentinal = LLNode(0,None)
        head = sentinal
        while temp0 and temp1:
            sentinal.next = temp0
            sentinal = temp0
            temp0 = temp0.next
            sentinal.next = temp1
            sentinal = temp1
            temp1 = temp1.next
        if temp0:
            sentinal.next = temp0
        elif temp1:
            sentinal.next = temp1
        return head.next