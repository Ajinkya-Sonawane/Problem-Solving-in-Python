# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, target: int) -> bool:
        stack = []
        
        def dfs(root):
            if not root:
                return False
            if target - root.val in stack:
                return True
            stack.append(root.val)
            y = dfs(root.left)
            x = dfs(root.right)
            return x or y
        return dfs(root)