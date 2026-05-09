from heapq import heappush, heappop 

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        R, C = len(heights), len(heights[0])
        efforts = [[float('inf')] * C for _ in range(R)]
        efforts[0][0] = 0
        hq = [(0, 0, 0)]

        while hq:
            e, r, c = heappop(hq)

            if r == R - 1 and c == C - 1:
                    return e # Found the min effort to destination

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    # What is the 'effort' to move to this neighbor?
                    new_effort = max(e, abs(heights[r][c] - heights[nr][nc]))
                    
                    # If this path is better than any previous path to (nr, nc)
                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heappush(hq, (new_effort, nr, nc))
        