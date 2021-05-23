# https://binarysearch.com/problems/Counting-Maximal-Value-Roots-in-Binary-Tree
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.cnt = 0

    def solve(self, root):
        self.traverse(root)
        return self.cnt

    def traverse(self,root):
        if not root:
            return 0
        l = self.traverse(root.left)
        r = self.traverse(root.right)
        max_ = max([l,r,root.val])
        if root.val >= max_:
            self.cnt += 1
        return max_