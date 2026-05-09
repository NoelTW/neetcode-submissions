import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        for u, v, w in times:
            adj[u].append((w, v))

        min_heap = [(0, k)]
    
        res = {}
        while min_heap:
            w1, v1 = heapq.heappop(min_heap)
            if v1 in res:
                continue
            res[v1] = w1
            for w2, v2 in adj[v1]:
                if v2 not in res:
                    heapq.heappush(min_heap,(w1 + w2, v2))
        
        return max(res.values()) if n == len(res) else -1


    