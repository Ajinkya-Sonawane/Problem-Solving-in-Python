# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         self.mappings = ['(',')']
#         self.digit_len = 2*n
#         self.res = []
#         self.dfs("",0)
#         return self.res
        
#     def dfs(self,s,index):
#         if index == self.digit_len:
#             if s and self.validator(s):
#                 self.res.append(s)
#             return
#         self.dfs(s+'(',index + 1)
#         self.dfs(s+')',index + 1)

        
#     def validator(self,s):        
#         cnt = 0
#         for char in s:
#             if char == "(":
#                 cnt += 1
#             elif char == ")":
#                 if cnt:
#                     cnt -=1
#                 else:
#                     return False
#         if cnt < 0:
#             return False
#         return True