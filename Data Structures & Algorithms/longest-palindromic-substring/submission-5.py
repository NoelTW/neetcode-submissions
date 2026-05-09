class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP solution
        L, R = 0, 0 
        n = len(s)
        max_len = 0
        def check(l, r):
            if r == n:
                return l, l
            L, R = 0, 0
            while l >= 0 and r < n and s[r] == s[l]:
                if r - l + 1 > R - L + 1:
                    L, R = l, r

                r += 1
                l -= 1

            return L, R


        for i in range(n):
            l, r = check(i, i)
            if r - l + 1> max_len:
                L, R = l,r
                max_len = R - L + 1
            l, r = check(i, i + 1)
            if r -l + 1 > max_len:
                L, R = l,r
                max_len = R - L + 1

        return s[L:R+1]
            