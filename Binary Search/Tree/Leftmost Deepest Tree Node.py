# https://binarysearch.com/problems/Leftmost-Deepest-Tree-Node
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        return self.traverse(root)[0]

    def traverse(self,root):
        if not root:
            return 0,0
        if not root.left and not root.right:
            return root.val,1
        l,lheight = self.traverse(root.left)
        r,rheight = self.traverse(root.right)
        if lheight == rheight:
            return l,lheight+1
        elif lheight>rheight:
            return l,lheight+1
        else:
            return r,rheight+1