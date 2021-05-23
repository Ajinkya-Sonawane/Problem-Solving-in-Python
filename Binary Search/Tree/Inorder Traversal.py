# https://binarysearch.com/problems/Inorder-Traversal
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        node = root
        stack = []
        ans = []
        while True:
            if node is not None:
                stack.append(node)
                node = node.left           
            elif stack:
                node = stack.pop()
                ans.append(node.val)
                node = node.right
            else:
                break
        return ans
