# https://binarysearch.com/problems/Linked-List-Partitioning
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        l,m,r = None,None,None
        ltemp,mtemp,rtemp = None,None,None
        while node:
            if node.val == k:
                if not m:
                    m = node
                else:
                    mtemp.next = node
                mtemp = node
            elif node.val < k:
                if not l:
                    l = node
                else:
                    ltemp.next = node
                ltemp = node
            else:
                if not r:
                    r = node
                else:
                    rtemp.next = node
                rtemp = node
            temp = node
            node = node.next
            temp.next = None
        head = l
        if not ltemp:
            if not mtemp:
                head = r
            else:
                head = m                
        else:
            ltemp.next = m
        if not mtemp:
            ltemp.next = r
        else:            
            mtemp.next = r
        return head