class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        f = [[0] * (m +1) for _ in range(n + 1) ]

        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    f[i+ 1][j + 1] = f[i][j ] + 1
                else:
                    f[i+ 1][j + 1] = max(f[i][j + 1], f[i + 1][j])
        return f[n][m]