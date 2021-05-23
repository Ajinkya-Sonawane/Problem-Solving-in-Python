# https://binarysearch.com/problems/Elephant-Tree
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        self.traverse(root)
        return root

    def traverse(self,node):
        if not node:
            return 0
        l = self.traverse(node.left)
        r = self.traverse(node.right)
        node.val = node.val + l +r
        return node.val