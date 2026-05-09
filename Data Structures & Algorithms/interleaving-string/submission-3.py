from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n + m != len(s3):
            return False
        @cache
        def dfs(i, j):
            if i < 0 and j < 0:
                return True
            res = False
            if i >= 0 and s1[i] == s3[i + j + 1]:
                res = res or dfs(i - 1, j)
            if j >= 0 and s2[j] == s3[i + j + 1]:
                return res or dfs(i , j - 1)
            return res 
        return dfs(n - 1, m - 1)