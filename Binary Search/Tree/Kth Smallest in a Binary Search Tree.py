# https://binarysearch.com/problems/Kth-Smallest-in-a-Binary-Search-Tree
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def solve(self, root, k):
        inorder = []
        stack = []
        cur = root
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                inorder.append(cur.val)
                cur = cur.right
            else:
                break
        return inorder[k]