# https://binarysearch.com/problems/Add-Linked-Lists
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, l0, l1):
        sentinal = LLNode(0,None)
        head = sentinal
        sum_ = 0
        carry = 0
        while l0 or l1:
            if l0 and l1:
                sum_ = l0.val + l1.val + carry
                l0 = l0.next
                l1 = l1.next
            elif not l0:
                sum_ = l1.val + carry 
                l1 = l1.next
            elif not l1:
                sum_ = l0.val + carry 
                l0 = l0.next
            carry = sum_ // 10
            sentinal.next = LLNode(sum_%10,None)
            sentinal = sentinal.next
        if carry:
            sentinal.next = LLNode(carry,None)
        return head.next