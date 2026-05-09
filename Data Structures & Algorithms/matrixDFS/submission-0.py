class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        def dfs(grid, r, c,visit):
            ROWS = len(grid)
            COLS = len(grid[0])
            # base case for fail
            # Case 1 reach boundary
            if min(r, c) < 0 or r == ROWS or c == COLS:
                return 0
            
            # Case 2 If current position is blocked
            if grid[r][c] == 1:
                return 0
            
            # If it's visited
            if (r,c) in visit:
                return 0

            # base case for reach the target
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            visit.add((r,c))
            top = dfs(grid, r-1, c, visit)
            right = dfs(grid, r, c + 1, visit)
            bottom = dfs(grid, r + 1, c , visit)
            left = dfs(grid, r, c - 1, visit)
            visit.remove((r,c))
            return top + right + bottom + left

        return dfs(grid, 0, 0, set())