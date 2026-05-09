class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.count = 0
        ROW, COL = len(grid) , len(grid[0])
        visit = set()
        direction = ((0,1),(0,-1),(1,0),(-1,0))
        def dfs(r,c):
            if r == ROW or  c == COL:
                return
            if r < 0 or c < 0:
                return
            if (r, c) in visit:
                return 
            if grid[r][c] == "0":
                return 

            visit.add((r,c))
            for (dr, dc) in direction:
                dfs(r + dr, c + dc)
        
        count = 0
        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in visit and grid[r][c] == "1":
                    dfs(r,c)
                    count += 1
        
        return count
            
            
