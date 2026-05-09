class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        p = 1
        for num in nums:
            p *= num
            pre.append(p)
        suf = [1] * len(nums)
        s = 1
        for i in range(len(nums) - 1, - 1, -1):
            s *= nums[i]
            suf[i] =s
        ans = []

        for i in range(len(nums)):
            if i == 0:
                val = suf[i + 1]
            elif i == len(nums) - 1:
                val = pre[i - 1]
            else :
                val = pre[i - 1] * suf[i + 1]
            ans.append(val)
        return ans