from functools import cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        @cache
        def dfs(i, j):
            if i < j:
                return 0
            if j < 0:
                return 1
            # if si == tj we can choose not to keep or not keep
            res = 0
            if s[i] == t[j]:
                res +=  dfs(i -1 , j - 1) + dfs(i - 1, j)
            else:
                res +=  dfs(i - 1, j)
            return res

        return dfs(n - 1, m - 1)