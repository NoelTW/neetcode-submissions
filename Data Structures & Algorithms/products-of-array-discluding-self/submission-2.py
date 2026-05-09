class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * (n + 1)
        
        for i,x in enumerate(nums):
            pre[i+1] = pre[i] * nums[i]
        
        suf = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf[i] = suf[i+1] * nums[i]
        
        return [pre[i] * suf[i+1] for i in range(n)]