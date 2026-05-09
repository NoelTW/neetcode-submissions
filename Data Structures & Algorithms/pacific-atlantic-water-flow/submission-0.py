class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])

        pac_set = set()
        atl_set = set()
        def dfs(r, c, prev, sea_set):
            if r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prev or (r,c) in sea_set:
                return
            sea_set.add((r,c))
            dfs(r + 1, c, heights[r][c], sea_set)
            dfs(r - 1, c, heights[r][c], sea_set)
            dfs(r, c - 1, heights[r][c], sea_set)
            dfs(r, c + 1, heights[r][c], sea_set)

        #up #down
        for c in range(COLS):
            dfs(0, c, 0, pac_set)
            dfs(ROWS - 1, c, 0, atl_set)

        #left #right
        for r in range(ROWS):
            dfs(r, 0, 0, pac_set)
            dfs(r, COLS -1 ,0, atl_set)
        
        return list(pac_set.intersection(atl_set))


