# https://binarysearch.com/problems/Count-BST-Nodes-in-a-Range
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, node, lo, hi):
        def Nodes_in_range(root, lo, hi):
            if root:
                if lo <= root.val <= hi:
                    return (
                        1 + Nodes_in_range(root.left, lo, hi) + Nodes_in_range(root.right, lo, hi)
                    )
                elif root.val < lo:
                    return Nodes_in_range(root.right, lo, hi)
                else:
                    return Nodes_in_range(root.left, lo, hi)
            return 0

        return Nodes_in_range(node, lo, hi)
