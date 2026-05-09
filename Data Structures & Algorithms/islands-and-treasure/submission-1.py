class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        ROWS, COLS = len(grid), len(grid[0])
        q = deque() 
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c)) 
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        

        while q:
            r, c = q.popleft() 

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue
                    
                if grid[nr][nc] != (2**31 - 1): # Only process empty rooms (INF)
                    continue
                
                grid[nr][nc] = grid[r][c] + 1
                
                # Add this newly processed empty room to the queue to explore its neighbors
                q.append((nr, nc))





                