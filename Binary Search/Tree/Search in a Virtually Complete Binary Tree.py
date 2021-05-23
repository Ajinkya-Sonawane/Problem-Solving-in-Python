# https://binarysearch.com/problems/Search-in-a-Virtually-Complete-Binary-Tree
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, target):
        queue = [root]
        res = []
        x = target
        while x >= 1:
            res.insert(0,x)
            x //=2
        while queue:
            cur = queue[0]
            del queue[0]
            if cur.val == target:
                return True
            if cur.left and cur.left.val in res:
                queue.append(cur.left)
            if cur.right and cur.right.val in res:
                queue.append(cur.right)
        return False