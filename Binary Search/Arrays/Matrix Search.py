#alexwice
class Solution:
    def solve(self, matrix, n):
        def possible(x):
            # Is the number of elements y with
            # y <= x greater than n?
            c = len(matrix[0]) - 1
            count = 0
            for row in matrix:
                while c >= 0 and row[c] > x:
                    c -= 1
                count += c + 1
            return count > n

        lo = matrix[0][0]
        hi = matrix[-1][-1]
        while lo < hi:
            mi = lo + hi >> 1
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo