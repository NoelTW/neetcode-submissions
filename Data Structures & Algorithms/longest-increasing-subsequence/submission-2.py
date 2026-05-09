from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        f = [0] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    f[i] = max(f[j], f[i])
            f[i] += 1
        
        return max(f)