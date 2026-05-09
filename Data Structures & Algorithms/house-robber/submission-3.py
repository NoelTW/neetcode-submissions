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
        for i in range(n):
            f[i + 2] = max(f[i + 1], f[i] + nums[i])
        return f[-1]

