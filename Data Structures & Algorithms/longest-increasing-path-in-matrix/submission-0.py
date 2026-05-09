class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        memo = {}
        def dfs(r, c):
            best = 1
            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < R and 0 <= nc < C:
                    if matrix[nr][nc] > matrix[r][c]:
                        best = max(best, 1 + dfs(nr, nc))
            return best
        ans = 0
        for r in range(R):
            for c in range(C):
                ans = max(ans, dfs(r, c))
        return ans