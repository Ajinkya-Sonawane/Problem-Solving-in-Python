# https://binarysearch.com/problems/Buying-Cars
class Solution:
    def solve(self, prices, k):
        prices = sorted(prices)
        res = 0
        for price in prices:
            k -= price
            if k < 0:
                return res
            res += 1
        return res