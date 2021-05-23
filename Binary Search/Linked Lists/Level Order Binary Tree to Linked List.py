# https://binarysearch.com/problems/Level-Order-Binary-Tree-to-Linked-List
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
        dq = deque()
        dq.append(root)
        head = LLNode(0,None)
        temp = head
        while dq:
            cur = dq.popleft()
            temp.next = LLNode(cur.val,None)
            temp = temp.next
            if cur.left:
                dq.append(cur.left)
            if cur.right:
                dq.append(cur.right)
        return head.next