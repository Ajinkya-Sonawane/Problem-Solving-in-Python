# https://binarysearch.com/problems/Inorder-Successor
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, t):
        stack = []
        cur = root
        flag = False
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                if flag:
                    return cur.val
                if cur.val == t:
                    flag = True
                cur = cur.right
            else:
                break