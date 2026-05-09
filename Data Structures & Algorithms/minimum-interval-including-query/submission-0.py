class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        que = []
        j = 0
        seen = {}
        for i, query in enumerate(sorted(queries)):
            while j < len(intervals) and intervals[j][0] <= query:
                s, e = intervals[j]
                heapq.heappush(que, (e - s + 1 , e )) 
                j += 1
            while que and que[0][1] < query:
                heapq.heappop(que)
            seen[query] = que[0][0] if que else -1
        ans = []
        for query in queries:
            ans.append(seen[query])
        return ans
