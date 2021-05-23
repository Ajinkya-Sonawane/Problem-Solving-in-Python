# https://binarysearch.com/problems/Invert-Tree
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, node):
        if node == None:
            return None
        self.solve(node.right)
        self.solve(node.left)
        temp = node.right
        node.right = node.left
        node.left = temp
        return node
        