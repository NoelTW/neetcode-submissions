class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        s = 0
        res = float('inf')
        for r in range(n):
            s += nums[r]
            while s >= target:
                print(l, r )
                res = min(res, r - l + 1)
                s -= nums[l]
                l += 1
        return res if res != float('inf') else 0