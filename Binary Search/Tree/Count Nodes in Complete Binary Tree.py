# https://binarysearch.com/problems/Count-Nodes-in-Complete-Binary-Tree 
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        stack = [root]
        cnt = 0
        while stack:
            node = stack.pop()
            cnt += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return cnt