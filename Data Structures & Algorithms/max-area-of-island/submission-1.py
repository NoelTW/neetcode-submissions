class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        seen = set()
        def dfs(r, c):
            if r < 0 or r ==n or c < 0 or c == m or grid[r][c] == 0 or (r, c) in seen:
                return 0
            seen.add((r, c))
            return dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1) + 1
        
        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    ans = max(ans, dfs(r, c))
        return ans
