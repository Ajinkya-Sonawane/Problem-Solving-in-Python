# https://binarysearch.com/problems/Vertical-Lines-in-Binary-Tree
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.lines = set()

    def solve(self, root):
        self.traverse(root,0)
        return len(self.lines)

    def traverse(self,root,cnt):
        if not root:
            return
        self.lines.add(cnt)
        self.traverse(root.left,cnt-1)
        self.traverse(root.right,cnt+1)

    