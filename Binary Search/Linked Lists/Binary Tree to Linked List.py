# https://binarysearch.com/problems/Binary-Tree-to-Linked-List
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def solve(self, root):
        ll_node = LLNode(0,None)        
        ll_node_tra = ll_node
        stack = []
        cur = root
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                temp = LLNode(cur.val,None)
                ll_node_tra.next = temp
                ll_node_tra = temp
                cur = cur.right
            else:
                break
        return ll_node.next