class Solution:
    def climbStairs(self, n: int) -> int:
        # dp array meaning 
        # i th Stairs
        # dp[i] : number of distinct way

        dp = [0, 1 , 2]

        if n < 2:
            return dp[n]


        for i in range(3, n + 1):
            dp.append(dp[i-1] + dp[i-2])

        return dp[n]