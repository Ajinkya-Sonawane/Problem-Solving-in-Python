# https://binarysearch.com/problems/Linked-List-to-ZigZag-Tree-Path
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        root = Tree(-math.inf,None,None)
        temp = root
        while node:
            x = Tree(node.val,None,None)
            if temp.val > node.val:                
                temp.left = x
                temp = temp.left                
            else:
                temp.right = x
                temp = temp.right
            node = node.next
        return root.right