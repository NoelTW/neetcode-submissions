from functools import cache

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        n = len(s)
        l = 0
        cnt = Counter(t)
        seen = Counter()
        ans = "N" * (n + 1)
        for r, x in enumerate(s):
            seen[x] += 1
            while seen >= cnt:
                if len(ans) >= r - l + 1:
                    ans = s[l : r + 1]
                seen[s[l]] -= 1
                l += 1
            
        return ans if len(ans) <= n else ""
        