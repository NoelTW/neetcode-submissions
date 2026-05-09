from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        sum to half of total
        target = total // 2
        This is 1 01 knapsack problem
        """

        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        n = len(nums)
        
        @cache
        def dfs(i, c):
            if i < 0:
                return True if c == 0 else  False
            if nums[i] > c:
                return dfs(i - 1, c)
            return dfs(i-1, c) or dfs(i - 1, c - nums[i])
        return dfs(n - 1, target)