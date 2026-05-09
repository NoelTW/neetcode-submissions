from functools  import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def dfs(m, n):
            if m == 0 or n == 0:
                return 1
            
            return dfs(m-1,n) + dfs(m, n - 1)
        
        return dfs(m-1,n-1)