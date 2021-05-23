# https://binarysearch.com/problems/Odd-Number-of-Digits
class Solution:
    def solve(self, nums):
        cnt = 0
        for num in nums:
            if self.digits(num) % 2 != 0:
                cnt +=1
        return cnt


    def digits(self,n):
        digitcount = 0
        while n:
            n //= 10
            digitcount += 1
        return digitcount