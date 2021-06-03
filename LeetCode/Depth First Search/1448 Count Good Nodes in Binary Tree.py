# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.cnt = 0
    
    def goodNodes(self, root: TreeNode) -> int:
        self.traverse(root,-float("inf"))
        return self.cnt
        
    def traverse(self,root,max_):
        if not root:
            return

        if max(max_,root.val) == root.val:
            self.cnt +=1
        self.traverse(root.left,max(max_,root.val))
        self.traverse(root.right,max(max_,root.val))
        