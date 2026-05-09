class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0
        # define a dfs helper function
        def dfs(r, c):
            if (r, c) in visited:
                return 0
            if (r < 0) or (c < 0) or (r == ROWS) or ( c == COLS) or grid[r][c] == 0:
                return 0
            visited.add((r,c))
            return dfs(r + 1, c) + dfs(r - 1,c) + dfs(r,c + 1) + dfs(r,c -1) + 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if ((r,c) not in visited) and grid[r][c] == 1:
                    max_area = max( dfs(r, c), max_area )
            
        return max_area
        

