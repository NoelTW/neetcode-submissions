class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        ans = -float('inf')
        for x in nums:
            pre += x
            ans = max(pre, ans)
            pre = max(0, pre)
        return ans