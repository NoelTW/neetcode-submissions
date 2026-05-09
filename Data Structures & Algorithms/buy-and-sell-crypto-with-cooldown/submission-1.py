class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        from functools import cache

        n = len(prices)
        f = [[0, 0] for i in range(n + 2)]
        f[0][1] = -float('inf')
        f[1][1] = -float('inf')
        for i in range(n):
            f[i+2][0] = max(f[i + 1][0], f[i + 1][1] + prices[i])
            f[i+2][1] = max(f[i + 1][1], f[i][0] - prices[i])
        return f[n + 1][0]
            
