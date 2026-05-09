class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        f = [0] * (amount + 1)
        f[0] = 1
        for coin in coins:
            for c in range(amount + 1):
                if c >= coin:
                    f[c] = f[c] + f[c - coin] 
        
        return f[amount]
        