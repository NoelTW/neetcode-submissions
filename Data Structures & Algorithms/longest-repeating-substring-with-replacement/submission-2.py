class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        cnt = [0] * 26
        ans = 0
        for r ,x in enumerate(s):
            cnt[ord(x) - ord("A")] += 1
            while ( (r - l + 1) - max(cnt)  ) > k:
                cnt[ord(s[l]) - ord("A")] -= 1
                l += 1 
            ans = max(ans, r- l + 1)
        return ans
