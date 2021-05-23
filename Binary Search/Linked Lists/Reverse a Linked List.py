# https://binarysearch.com/problems/Reverse-a-Linked-List
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        prev = None
        temp = node
        while temp:
            x = temp.next
            temp.next = prev
            prev = temp
            temp = x
        return prev
        
