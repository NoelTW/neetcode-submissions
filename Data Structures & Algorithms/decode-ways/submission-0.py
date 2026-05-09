from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(i):
            if i < 0:
                return 1
            count = 0
            if s[i] != "0":
                count += dfs(i - 1)
            if i > 0 and s[i - 1] != "0":
                num = int(s[i-1 : i+1])
                if 10 <= num <= 26:
                    count += dfs(i - 2)
            return count
                
        return dfs(len(s) - 1)