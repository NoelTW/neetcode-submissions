class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        from functools import cache
        n = len(coins) # 物品
        # amount 背包
        @cache
        def dfs(i,c):
            if i < 0:
                return 1 if not c else 0
            res = 0
            if c >= coins[i]:
                res += dfs(i, c - coins[i])
            res += dfs(i - 1, c)
            return res
        return dfs(n-1, amount)