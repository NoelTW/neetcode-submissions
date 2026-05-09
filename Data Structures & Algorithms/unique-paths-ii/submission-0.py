class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])


        dp = [ ([0] * COLS) for _ in range(ROWS)]
        
        for r in range(ROWS):
            if obstacleGrid[r][0]:
                break
            dp[r][0] = 1
        for c in range(COLS):
            if obstacleGrid[0][c]:
                break
            dp[0][c] = 1
        print(dp)
        # if ROWS == 1 or COLS == 1:
        #     return
        
        for r in range(1,ROWS):
            for c in range(1,COLS):
                left = 0 if obstacleGrid[r - 1][c] else dp[r-1][c]
                up = 0 if obstacleGrid[r][c -1 ] else dp[r][c -1 ] 
                dp[r][c] = left + up 

        return dp[ROWS-1][COLS-1]