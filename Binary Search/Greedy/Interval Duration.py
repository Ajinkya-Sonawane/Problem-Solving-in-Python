class Solution:
    def solve(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        currentEnd = intervals[0][1]
        distance = intervals[0][1] - (intervals[0][0] - 1)

        for interval in intervals[1:]:
            if interval[1] > currentEnd:
                distance += interval[1] - max(currentEnd, interval[0] - 1)
                currentEnd = interval[1]

        return distance
