from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False

        @cache
        def dfs(i: int, j: int) -> bool:
            if i < 0 and j < 0:
                return True
            if i >= 0 and s1[i] == s3[i + j + 1] and dfs(i - 1, j):
                return True
            if j >= 0 and s2[j] == s3[i + j + 1] and dfs(i, j - 1):
                return True
            return False
                   

        return dfs(n - 1, m - 1)