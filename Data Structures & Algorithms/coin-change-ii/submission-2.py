class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        f = [0] * (amount + 1)
        f[0] = 1
        for i, x in enumerate(coins):
            for c in range(amount + 1):
                if c >= x:
                    f[c] += f[c - x]
        return f[amount]