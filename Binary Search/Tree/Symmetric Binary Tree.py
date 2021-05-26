# https://binarysearch.com/problems/Symmetric-Binary-Tree
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def solve(self, root):
        return self.traverse(root,root)
    
    def traverse(self,r1,r2):
        if not r1 and not r2:
            return True            
        if r1 and r2:
            if r1.val == r2.val:
                return self.traverse(r1.left,r2.right) and self.traverse(r1.right,r2.left)
        return False    