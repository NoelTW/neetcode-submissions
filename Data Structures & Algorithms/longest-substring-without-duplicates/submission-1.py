class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        l = 0 
        counter = set()
        for r in range(n):
            while s[r] in counter:
                counter.remove(s[l])
                l += 1
            counter.add(s[r])
            ans =max(ans, r - l + 1)
        return ans