class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from functools import cache
        n = len(coins)

        @cache
        def dfs(i,c):
            if i < 0:
                return 0 if c == 0 else float('inf')
            if c < coins[i]:
                return dfs(i- 1, c)
            return min(dfs(i-1,c) , dfs(i, c-coins[i]) + 1)
        res = dfs(n - 1, amount)
        return res if res != float('inf') else -1 