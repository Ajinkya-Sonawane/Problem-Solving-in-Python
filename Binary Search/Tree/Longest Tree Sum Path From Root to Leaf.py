# https://binarysearch.com/problems/Longest-Tree-Sum-Path-From-Root-to-Leaf
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def solve(self, root):
        return self.traverse(root)[0]

    def traverse(self,root):
        if not root:
            return 0,0
        l,heightL = self.traverse(root.left)
        r,heightR = self.traverse(root.right)
        temp = 0
        if heightL == heightR:
            temp = max(l,r) + root.val
            return temp,heightL+1
        if heightL > heightR:
            temp = l + root.val
            return temp,heightL+1
        temp = r + root.val
        return temp,heightR+1