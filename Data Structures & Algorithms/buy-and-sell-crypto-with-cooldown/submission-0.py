class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        from functools import cache

        @cache
        def dfs(i, hold):
            if i < 0:
                return -float("inf") if hold else 0
            if hold:
                return max(dfs(i - 1, True), dfs(i - 2, False) - prices[i])
            return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])
        
        return dfs(len(prices) - 1, 0)