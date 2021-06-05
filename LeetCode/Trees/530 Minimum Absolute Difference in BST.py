# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.ans = float("inf")
        self.prev = -float("inf")
        
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.ans
        
    
    def traverse(self,root):
        if not root:
            return 
        self.traverse(root.left)
        self.ans = min(self.ans,abs(self.prev - root.val))
        self.prev = max(self.prev,root.val)
        self.traverse(root.right)