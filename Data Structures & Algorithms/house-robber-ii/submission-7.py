from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self._rob(0, n - 2), self._rob(1, n - 1))

    def _rob(self, s, e):
        f0 =  f1 = 0
        for i in range(s, e  + 1):
            f0, f1 = f1, max(f0 + self.nums[i], f1)
        return f1

