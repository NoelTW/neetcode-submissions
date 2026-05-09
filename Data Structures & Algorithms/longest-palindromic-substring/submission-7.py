class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def ok(l, r):
            min_l, max_r = l,  r 
            while l >= 0 and r < n and s[l] == s[r]:
                min_l, max_r = l,  r
                l -= 1
                r += 1
            return min_l, max_r
        
        ans_l, ans_r = 0, 0
        for i in range(n):
            min_l, max_r = ok(i, i)
            if max_r - min_l > ans_r - ans_l:
                ans_l, ans_r = min_l, max_r
            if i < n - 1 and s[i] == s[i +1]:
                min_l, max_r = ok(i, i +1)
                if max_r - min_l > ans_r - ans_l:
                    ans_l, ans_r = min_l, max_r
        return s[ans_l:ans_r + 1]
