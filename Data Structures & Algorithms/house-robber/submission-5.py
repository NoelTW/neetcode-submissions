from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # @cache
        # def dfs(i):
        #     if i < 0:
        #         return 0

        #     return max(dfs(i - 1) , dfs(i - 2) + nums[i])
        # return dfs(n - 1)
        f =  [0] * (n + 2)
        f0 = f1 = 0
        for i in range(n):
            new_f = max(f0 + nums[i], f1) 
            f0 = f1
            f1 = new_f
        return new_f

