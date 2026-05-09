from heapq import heappop, heappush


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        stops = [float("inf")] * n
        hq = [[0, src, 0]]
        while hq:
            w1, u, s = heappop(hq)
            if u == dst:
                return w1
            if s > k or s >= stops[u]:
                continue
            for v, w2 in adj[u]:
                heappush(hq, (w1 + w2, v, s + 1))
        return -1
