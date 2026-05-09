class Solution:
    def trap(self, height: List[int]) -> int:
        pre = 0
        suf = 0
        l, r = 0, len(height) - 1
        ans = 0
        while l <= r:
            if height[l] < height[r]:
                ans += max(pre - height[l], 0)
                pre = max(pre, height[l])
                l += 1
            else:
                ans += max(suf - height[r] ,0)
                suf = max(suf, height[r])
                r -= 1
        return ans