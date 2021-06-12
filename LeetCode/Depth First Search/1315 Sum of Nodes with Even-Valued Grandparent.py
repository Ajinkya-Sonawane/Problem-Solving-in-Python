# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sum_ = 0
        def dfs(root,parent):
            nonlocal sum_
            if not root:
                return 0
            dfs(root.left,root)
            dfs(root.right,root)
            if parent and parent.val%2 == 0:
                if root.right:
                    sum_ += root.right.val
                if root.left:
                    sum_ += root.left.val
        dfs(root,None)
        # def dfs(root,parent,grandparent):
        #     nonlocal sum_
        #     if not root:
        #         return
        #     dfs(root.left,root,parent)
        #     dfs(root.right,root,parent)
        #     if grandparent and grandparent.val %2 == 0:
        #         sum_ += root.val
        # dfs(root,None,None)
        return sum_