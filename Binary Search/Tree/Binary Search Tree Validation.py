# https://binarysearch.com/problems/Binary-Search-Tree-Validation
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        stack = []
        inorder = []
        cur = root
        min_ = -float("inf")
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                if (min_ > cur.val):
                    return False
                min_ = cur.val
                cur=cur.right
            else:
                break
        return True