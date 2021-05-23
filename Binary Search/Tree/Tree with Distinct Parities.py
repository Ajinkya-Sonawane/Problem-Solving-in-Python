# https://binarysearch.com/problems/Tree-with-Distinct-Parities
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        return self.traverse(root)[1]

    def traverse(self,node):
        if not node:
            return 0,0
        l,lcnt = self.traverse(node.left)
        r,rcnt = self.traverse(node.right)
        cnt = lcnt + rcnt
        if node.left and node.right:
            cnt +=  l&1 ^ r&1
        return l+r+node.val,cnt