# https://binarysearch.com/problems/Palindromic-Tree
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.res = []

    def solve(self, root):
        self.traverse(root)
        start,end = 0,len(self.res)-1
        while start <= end:
            if self.res[start] != self.res[end]:
                return False
            start +=1
            end -=1
        return True

    def traverse(self,root):
        if not root:
            return
        
        self.traverse(root.left)
        self.res.append(root.val)
        self.traverse(root.right)