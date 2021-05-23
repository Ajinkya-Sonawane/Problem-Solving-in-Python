# https://binarysearch.com/problems/Kth-Last-Node-of-a-Linked-List
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        fast = node
        while k!=0:
            fast = fast.next
            k-=1
        while fast.next:
            node=node.next
            fast=fast.next
        return node.val