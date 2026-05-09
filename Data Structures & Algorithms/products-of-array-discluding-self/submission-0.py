class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [None] * len(nums)

        for i in range( len(nums) ):
            j = 0
            comprod = 1
            while j < len(nums):
                if j != i:
                    comprod *= nums[j]
                j += 1
            ans[i] = comprod
        
        return ans

