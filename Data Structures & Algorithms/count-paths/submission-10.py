class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [0] * (n + 1)
        f[1] = 1
        for i in range(m):
            for j in range(n):
                f[j + 1] = f[j + 1] + f[j]
        return f[n]
