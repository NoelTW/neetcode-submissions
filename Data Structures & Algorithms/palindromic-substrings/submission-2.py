class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        def ok(l, r):
            res = 0
            while l >= 0 and r < n and s[l] == s[r]:
                res +=1
                l -= 1
                r += 1
            return res
        
        for i in range(n):
            l, r = i, i
            ans += ok(l,r )
            if i < n - 1 and s[i] == s[i + 1]:
                l, r = i, i + 1
                ans += ok(l,r )
        return ans