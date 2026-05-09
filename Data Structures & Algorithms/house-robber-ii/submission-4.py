from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        @cache
        def dfs(s, e):
            if e < s:
                return 0 
            return max(dfs(s, e-2) + nums[e] , dfs(s, e - 1) )
        
        return max(dfs(1, len(nums) - 1), dfs(0, len(nums) - 2))
            