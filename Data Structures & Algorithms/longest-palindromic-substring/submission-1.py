from functools import cache

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 枚舉選哪個
        n = len(s)
        def ok(l, r):
            while l < r :
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        ans = ""
        curr_len = 0
        for l in range(n):
            for r in range(l, n):
                if ok(l, r):
                    if r - l + 1 > curr_len:
                        curr_len = r - l + 1
                        ans = s[l:r + 1]
        return ans