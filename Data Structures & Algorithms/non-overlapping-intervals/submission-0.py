class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        ans = 0
        pe = -float("inf")
        for i in range(n):
            cs, ce = intervals[i]
            if cs < pe:
                ans += 1
                pe = min(ce, pe)
            else:
                pe = ce
        return ans