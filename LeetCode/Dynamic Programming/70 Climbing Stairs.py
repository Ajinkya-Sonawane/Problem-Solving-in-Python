# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0]*(n+1)
        memo[0] = 1
        memo[1] = 1
        #Iterative
        for i in range(2,n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]
        
        #Recursive
        # def recurse(x,memo):
        #     if memo[x]>0:
        #         return memo[x]            
        #     y = recurse(x-1,memo) + recurse(x-2,memo)
        #     memo[x] = y
        #     return y
        # return recurse(n,memo)