class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        ans=0
        # hashmap
        seen = set()
        for r in range(n):
            x = s[r]
            while x in seen:
                y = s[l]
                seen.remove(y)
                l += 1
            seen.add(x)
            ans = max(r-l+1, ans)
        return ans
