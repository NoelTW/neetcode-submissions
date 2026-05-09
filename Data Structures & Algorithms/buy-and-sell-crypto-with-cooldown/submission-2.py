class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, hold):
            from math import inf
            if i < 0:
                return -inf if hold else 0
            if (i, hold) in memo:
                return memo[(i, hold)]
            if hold:
                memo[(i, hold)] = max(dfs(i - 1, True), dfs(i-2, False) - prices[i])
                return memo[(i, hold)]
            memo[(i, hold)] = max(dfs(i - 1, False), dfs(i-1, True) + prices[i])
            return memo[(i, hold)]
        return dfs(len(prices) -1, False)