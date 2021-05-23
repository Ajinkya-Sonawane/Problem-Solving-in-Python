# https://binarysearch.com/problems/Swap-Kth-Node-Values
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        head = node
        cnt = k
        while k:
            k-=1
            node = node.next
        k1,fast = node,node
        node = head
        while fast.next:
            fast=fast.next
            node = node.next
        k1.val,node.val = node.val,k1.val
        return head
