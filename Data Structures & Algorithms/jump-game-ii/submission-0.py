class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0 
        next_right = 0
        curr_right = 0
        for i in range(len(nums) - 1):
            next_right = max(next_right, nums[i] + i)
            if i == curr_right:
                curr_right = next_right
                ans += 1
        return ans
