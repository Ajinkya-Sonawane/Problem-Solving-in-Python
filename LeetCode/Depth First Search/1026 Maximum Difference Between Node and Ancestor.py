# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        ans = -float("inf")
        def dfs(root,max_,min_):
            nonlocal ans
            if not root:
                return
            ans = max(ans,abs(max_-root.val))
            ans = max(ans,abs(root.val - min_))
            dfs(root.left,max(max_,root.val),min(min_,root.val))
            dfs(root.right,max(max_,root.val),min(min_,root.val))
        dfs(root,root.val,root.val)            
        # def dfs(root,max_,min_):
        #     if not root:
        #         return max_ - min_
        #     max_ = max(max_,root.val)
        #     min_ = min(min_,root.val)
        #     l = dfs(root.left,max_,min_)
        #     r = dfs(root.right,max_,min_)
        #     return max(l,r)
        # return dfs(root,root.val,root.val)
        return ans