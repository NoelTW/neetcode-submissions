class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []
        def backtrack(i, curr_sum):
            if curr_sum == target:
                ans.append(path[:]) 
            if i == n:
                return 
            for j in range(i, n):
                if nums[j] + curr_sum > target:
                    continue
                else:
                    path.append(nums[j])
                    backtrack(j, curr_sum + nums[j])
                    path.pop()
        backtrack(0, 0)
        return ans
