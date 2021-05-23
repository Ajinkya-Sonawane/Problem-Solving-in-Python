# https://binarysearch.com/problems/Shortest-Sublist-With-Max-Frequency
class Solution:
    def solve(self, nums):
        k = -1
        check={}
        for i,v in enumerate(nums):
            if v not in check:
                check[v] = [i,i,1]
                if k < 1:
                    k=1
            else:
                check[v][1] = i
                check[v][2]+=1
                x=check[v][2]
                if k <=x:
                    k=x
        ans = float("inf")
        for a in check:
            if check[a][2] == k:
                b=check[a][1]-check[a][0]+1
                if ans > b:
                    ans=b

        return ans
