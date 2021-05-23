# https://binarysearch.com/problems/Pairwise-Linked-List-Swap
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):        
        temp = node
        if not node: return None
        while temp.next:
            temp.val,temp.next.val = temp.next.val,temp.val
            if not temp.next.next:
                break
            temp = temp.next.next
        return node
        