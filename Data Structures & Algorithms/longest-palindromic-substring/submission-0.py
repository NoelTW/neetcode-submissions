class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        mx_len = 0
        res = ""

        def expand(l, r):
            nonlocal res
            nonlocal mx_len
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > mx_len:
                    res = s[l : r + 1]
                    mx_len = r - l + 1
                l -= 1
                r += 1

        for i in range(n):
            p1 = expand(i, i)
            p2 = expand(i, i + 1)

        return res
