class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        ans = []
        for interval in intervals:
            # A[0] <= B[0]
            # IF A[1] >= B[0], THEN has interval
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                s, e = ans.pop()
                ans.append([s, max(e, interval[1])])
        return ans
