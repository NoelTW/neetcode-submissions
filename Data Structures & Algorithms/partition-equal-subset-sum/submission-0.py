class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        f = [[0] * (target + 1) for _ in range(n + 1)]
        for i, x in enumerate(nums):
            for c in range(target + 1):
                if c < x:
                    f[i+1][c] = f[i][c]
                else:
                    f[i+1][c] = max(f[i][c], f[i][c - x] + x)
        return f[n][target] == target
