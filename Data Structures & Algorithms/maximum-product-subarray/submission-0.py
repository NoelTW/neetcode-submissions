from math import inf

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -inf
        max_curr, min_curr = 1,1

        for num in nums:
            temp = max_curr
            max_curr = max(temp*num, num * min_curr, num)
            min_curr = min(temp*num, num * min_curr, num)
            res = max(max_curr, res)
        
        return res