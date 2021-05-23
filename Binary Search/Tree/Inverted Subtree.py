# https://binarysearch.com/problems/Inverted-Subtree
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, source, target):
        if not source or not target:
            return not source and not target
        t = self.isSubtree(target, source)
        return t

    def isSubtree(self, s, t):
        def sametree(s, t):
            if not s or not t:
                return not s and not t
            elif s.val == t.val:
                return (sametree(s.left, t.left) and sametree(s.right, t.right)) or (
                    sametree(s.right, t.left) and sametree(s.left, t.right)
                )
            else:
                return False

        if not s:
            return False
        elif sametree(s, t):
            return True
        else:
            return self.isSubtree(s.right, t) or self.isSubtree(s.left, t)
