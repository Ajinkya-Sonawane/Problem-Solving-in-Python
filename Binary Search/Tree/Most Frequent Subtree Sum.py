# https://binarysearch.com/problems/Win-After-Last-Round
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def solve(self, root):
        self.res.append(self.traverse(root))
        return max(set(self.res),key=self.res.count)
    
    def traverse(self,root):
        if not root:
            return None
        self.res.append(root.val)
        l = self.traverse(root.left)
        r = self.traverse(root.right)
        if not l:
            l = 0
        else:
            self.res.append(l)
        if not r:
            r = 0
        else:
            self.res.append(r)
        treesum = l + r + root.val
        self.res.append(treesum)
        return treesum