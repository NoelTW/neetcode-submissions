from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        que = deque()
        fresh = 0

        # Step 1: Add all rotten oranges to the queue and count fresh ones
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    que.append((r, c, 0))  # (row, col, minutes)
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes = 0

        # Step 2: BFS traversal
        while que:
            r, c, m = que.popleft()
            minutes = max(minutes, m)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Boundary check and fresh orange check
                if (0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == 1):
                    grid[nr][nc] = 2  # Rot the fresh orange
                    fresh -= 1
                    que.append((nr, nc, m + 1))

        # Step 3: Check if any fresh oranges remain
        return minutes if fresh == 0 else -1
