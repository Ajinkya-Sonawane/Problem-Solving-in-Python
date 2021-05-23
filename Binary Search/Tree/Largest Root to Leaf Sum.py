# https://binarysearch.com/problems/Largest-Root-to-Leaf-Sum
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root:
            return 0
        l = self.solve(root.left)
        r = self.solve(root.right)
        return max(l,r)+root.val