class Solution:
    def search(self, nums: List[int], target: int) -> int:
        import bisect
        j =  bisect.bisect_left(nums, target) 
        return j if j < len(nums) and nums[j] == target else -1