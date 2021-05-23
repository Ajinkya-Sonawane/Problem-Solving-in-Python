# https://binarysearch.com/problems/Level-Order-Traversal
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        queue = [root]
        res = []
        while queue:
            cur = queue[0]
            del queue[0]
            res.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return res