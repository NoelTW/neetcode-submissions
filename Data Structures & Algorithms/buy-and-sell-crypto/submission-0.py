class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr_min = prices[0]

        for price in prices[1:]:
            if price > curr_min:
                profit = max(profit, price - curr_min)
            else:
                curr_min = price
        
        return profit

        
        