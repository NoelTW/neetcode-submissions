class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()
        self.count = 0
        direction = [(0,1),  (1,0), (-1,0), (0,-1)]
        def dfs(r, c):
            print(r,c)
            if r == ROW or r < 0 or c == COL or c < 0 or (r, c) in visit :
                return 
            if grid[r][c] == 1:
                return

            if r == ROW - 1 and c == COL-1:
                self.count +=1 
                return

            visit.add((r,c))
            for dr, dc in direction:
                dfs(r+dr, c+dc)
            visit.remove((r,c))
        
        dfs(0,0 )
        
        return self.count