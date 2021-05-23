# https://binarysearch.com/problems/Binary-Search-Tree-Iterator
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root):
        self.root = root
        self.res = self.fetchInorder(root)
        self.leftEl = len(self.res)

    def next(self):
        x = self.res[0]
        del self.res[0]
        self.leftEl -= 1
        return x

    def hasnext(self):
        return self.leftEl != 0

    def fetchInorder(self,root):
        if not root:
            return []
        left = self.fetchInorder(root.left)
        right = self.fetchInorder(root.right)
        return left + [root.val] + right
        