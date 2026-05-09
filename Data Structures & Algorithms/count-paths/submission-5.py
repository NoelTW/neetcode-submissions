class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[0] * (n + 1) for _ in range(m + 1)]
        f[0][1] = 1
        for i in range(m):
            for j in range(n):
                f[i+1][j+1] = f[i+1][j] + f[i][j+1]
        print(f)
        return f[m][n]