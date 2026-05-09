from functools import cache

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        @cache
        def dfs(i, c):
            if i < 0:
                return 0
            if c - weight[i] < 0:
                return dfs(i-1, c)
            return max(dfs(i-1, c), dfs(i-1, c - weight[i]) + profit[i])
        return dfs(n-1, capacity)
