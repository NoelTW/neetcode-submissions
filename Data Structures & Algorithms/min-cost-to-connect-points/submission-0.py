class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        v = len(points)
        adj = {}
        for x, y in points:
            adj[(x,y)] = []
        for i in range(v):
            x1, y1 = points[i]
            for j in range(i + 1, v):
                x2, y2 = points[j]
                adj[(x1,y1)].append((abs(x2 - x1) + abs(y2 - y1), x2, y2))
                adj[(x2,y2)].append((abs(x2 - x1) + abs(y2 - y1), x1, y1))
        min_heap = []
        x0, y0 = points[0][0] , points[0][1]
        for cost, x1, y1 in adj[(x0, y0)]:
            heapq.heappush(min_heap,(cost, x1, y1))
        # Find answer
        res = 0 
        visit = set([(x0, y0)])
        while len(visit) < v:
            cost1, x1, y1 = heapq.heappop(min_heap )
            if (x1, y1) in visit:
                continue
            visit.add((x1, y1))
            res += cost1

            for cost2, x2, y2 in adj[(x1,y1)]:
                if (x2, y2) not in visit:
                    heapq.heappush(min_heap,(cost2, x2, y2))
        
        return res
