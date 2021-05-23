# https://binarysearch.com/problems/Sort-a-Linked-List
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        head = node
        temp = None
        res = []
        while node:
            res.append(node.val)
            node = node.next
        res.sort()
        for val in res:
            x = LLNode(val,None)
            if not temp:
                temp = x
                head = x
            else:
                temp.next = x
                temp = temp.next
        return head