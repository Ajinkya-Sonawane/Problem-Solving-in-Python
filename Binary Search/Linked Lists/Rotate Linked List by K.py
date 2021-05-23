# https://binarysearch.com/problems/Rotate-Linked-List-by-K
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head, k):
        slow = fast = head
        for _ in range(k):
            fast = fast.next

        if not fast or k == 0:
            return head

        while fast.next:
            slow = slow.next
            fast = fast.next

        # Now, slow is k from the end.
        ans = slow.next
        slow.next = None
        fast.next = head
        return ans
