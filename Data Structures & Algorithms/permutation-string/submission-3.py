class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        cnt = dict()
        k = 0
        for c in s1:
            cnt[c] = cnt.get(c, 0) + 1
            k += 1
        l = 0
        seen = dict()
        for r in range(len(s2)):
            seen[s2[r]] = seen.get(s2[r], 0) + 1
            if r - l + 1 > k:
                seen[s2[l]] -= 1
                if not seen[s2[l]]:
                    del seen[s2[l]]
                l += 1
            if cnt == seen:
                return True
        
        return False