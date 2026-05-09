from functools  import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [1] * n

        for r in range(1, m):
            for c in range(n):
                if c - 1 >= 0:
                    dp[c] += dp[c- 1]
        return dp[-1]