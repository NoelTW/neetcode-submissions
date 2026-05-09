class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        f = [0] * (target + 1)

        for x in nums:
            for c in range(target, x-1, -1):
                f[c] = max(f[c], f[c - x] + x)
        return f[target] == target
