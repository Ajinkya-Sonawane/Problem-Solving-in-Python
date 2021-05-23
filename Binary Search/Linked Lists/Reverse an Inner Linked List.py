# https://binarysearch.com/problems/Reverse-an-Inner-Linked-List
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def solve(self, node, i, j):
        dummy = LLNode(val=-1, next=node)

        curr = dummy
        cnt = 0
        while cnt < i:
            curr = curr.next
            cnt += 1
        front_r = prev = curr
        curr = curr.next
        end_r = curr

        cnt = i
        while cnt <= j:
            curr.next, prev, curr = prev, curr, curr.next
            cnt += 1

        front_r.next = prev
        end_r.next = curr

        return dummy.next        