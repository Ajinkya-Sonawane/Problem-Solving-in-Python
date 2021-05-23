# https://binarysearch.com/problems/Linked-List-Jumps
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):        
        head = node
        while head:
            cnt = head.val
            temp = head
            while cnt > 0:
                if not temp:
                    break
                temp = temp.next
                cnt -= 1
            head.next = temp
            head = head.next
        return node