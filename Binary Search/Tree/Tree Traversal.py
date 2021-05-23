# https://binarysearch.com/problems/Tree-Traversal
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, moves):
        head = root
        stack = []
        for move in moves: 
            if move == "RIGHT":
                stack.append(root)                
                root = root.right
            elif move == "LEFT":
                stack.append(root)
                root = root.left
            elif move == "UP":
                root = stack.pop()
        return root.val