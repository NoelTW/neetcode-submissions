class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        R, C = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1


        ans = 0

        while q:
            if fresh == 0:
                return ans
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in ((1, 0), (0,1), (-1,0), (0, -1)):
                    nr, nc = r+dr, c+dc
                    if 0<=nr<R and 0<=nc<C and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr,nc))
            ans += 1
        
        return ans if fresh == 0 else -1
