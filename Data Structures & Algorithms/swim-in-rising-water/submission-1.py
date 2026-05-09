class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)

        dist = [[float('inf')] * n for _ in range(n)]

        dist[0][0] = grid[0][0]

        min_heap = [(grid[0][0], 0, 0)]

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


        while min_heap:
            curr_max, r, c = heapq.heappop(min_heap)
            if curr_max > dist[r][c]:
                continue
            if r == n - 1 and c == n- 1:
                return curr_max
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    new_max = max(curr_max, grid[nr][nc])
                    if new_max < dist[nr][nc]:
                        dist[nr][nc] = new_max
                        heapq.heappush(min_heap, (new_max, nr, nc))
