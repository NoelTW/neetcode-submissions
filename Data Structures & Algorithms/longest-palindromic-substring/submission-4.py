class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans_l, ans_r = 0, 0
        
        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 2 > ans_r - ans_l:
                ans_r = r - 1
                ans_l = l + 1
        
        for i in range(n - 1):
            l = i 
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 2 > ans_r - ans_l:
                ans_r = r - 1
                ans_l = l + 1
        return s[ans_l: ans_r + 1]