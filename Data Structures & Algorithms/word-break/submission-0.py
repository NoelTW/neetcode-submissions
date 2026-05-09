class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        cache = {}
        def backtrack(start_index):
            if start_index == n:
                return True
            if start_index in cache:
                return cache[start_index]
            for i in range(start_index, n):
                word = s[start_index:i+1]
                if word in wordDict:
                    res = backtrack(i + 1)
                    if res:
                        return True
                    cache[start_index] = res
            return False
        return backtrack(0)

