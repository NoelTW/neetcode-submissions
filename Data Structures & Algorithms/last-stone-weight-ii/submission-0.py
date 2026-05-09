class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) // 2
        f = [0] * (target + 1)
        for x in stones:
            for c in range(target, x-1, -1):
                f[c] = max(f[c],f[c-x] + x)
        return sum(stones) - f[target] - f[target]
