from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = inf
        ans = 0
        for r in range(len(prices)):
            if prices[r] - curr_min > ans:
                ans = prices[r] - curr_min
            curr_min = min(curr_min, prices[r])
        return ans 