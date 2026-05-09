from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])        
        que = deque()
        start = (0,0)
        visit = set()
        que.append(start)
        visit.add(start)
        res = 0 
        directions = [(0,1), (1, 0), (-1, 0), (0, -1)] 
        while que:
            for _ in range(len(que)):
                r, c = que.popleft()
                if (r == ROWS - 1) and (c == COLS - 1):
                    return res
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr, nc) in visit or grid[nr][nc] == 1:
                        continue
                    que.append((nr, nc))
            res += 1

        return -1

