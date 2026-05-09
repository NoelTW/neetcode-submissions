class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
    
        from functools import cache
        @cache
        def dfs(i, j):
            if i < 0 and j < 0:
                return 0
            if i < 0 or j < 0:
                return i + 1 if j < 0  else j + 1
            if word1[i] == word2[j]:
                return dfs(i-1, j-1)
            return min(dfs(i - 1, j-1),  dfs(i, j-1), dfs(i - 1, j)) + 1
        
        return dfs(len(word1) - 1, len(word2) - 1)