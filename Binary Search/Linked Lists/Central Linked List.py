# https://binarysearch.com/problems/Central-Linked-List
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        cnt = 0
        head = node
        while node:
            cnt += 1            
            node= node.next
        node = head
        cnt = cnt//2
        while cnt:
            cnt -= 1
            node = node.next
        return node.val