class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        step = 0
        while i < len(nums):
            step = max(nums[i], step)
            if step == 0:
                break
            i += 1
            step -= 1
        return i >= len(nums) - 1