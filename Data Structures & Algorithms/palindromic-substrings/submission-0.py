class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for m in range(len(s)):
            l, r = m, m
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        for m in range(len(s)):
            l, r = m - 1 , m
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
    
        return res