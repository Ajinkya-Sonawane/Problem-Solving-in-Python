# https://binarysearch.com/problems/Linked-List-Union

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node1, node2):
        x = LLNode(0,None)
        temp = x        
        while node1 and node2:
            if node1.val < node2.val:
                temp.next = node1
                node1 = node1.next
            elif node1.val > node2.val:
                temp.next = node2
                node2 = node2.next
            else:
                temp.next = node1
                node1 = node1.next
                node2 = node2.next
            temp = temp.next
        if not node1:
            temp.next = node2
        elif not node2:
            temp.next = node1
        return x.next
            