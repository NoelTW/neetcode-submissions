class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # p - (s-p) = t
        target += sum(nums)
        if target % 2 or target < 0:
            return 0
        target //= 2
        n = len(nums)
        f = [0] * (target + 1)
        f[0] = 1
        for x in nums:
            for c in range(target, x - 1, -1 ):
                f[c] = f[c] + f[c - x]
        return f[target]

