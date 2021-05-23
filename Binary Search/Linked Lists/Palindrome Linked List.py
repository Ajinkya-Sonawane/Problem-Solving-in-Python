# https://binarysearch.com/problems/Palindrome-Linked-List
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        stack = []
        head = node
        while node:
            stack.append(node)
            node = node.next
        node = head
        mid = len(stack) //2
        while mid:
            if node.val != stack.pop().val:
                return False
            mid -=1
            node = node.next
        return True