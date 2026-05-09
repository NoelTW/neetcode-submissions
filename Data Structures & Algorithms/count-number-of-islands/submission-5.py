class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        n, m = len(grid), len(grid[0])

        def dfs(r, c):
            if r == n or r < 0 or c == m or c < 0 or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
            
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    dfs(r, c)
                    ans += 1

        return ans
