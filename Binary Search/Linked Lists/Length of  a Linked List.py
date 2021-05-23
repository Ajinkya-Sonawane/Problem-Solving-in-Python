# https://binarysearch.com/problems/Length-of-a-Linked-List
class Solution:
    def solve(self, node):
        res = 0
        while node:
            res += 1
            node = node.next
        return res