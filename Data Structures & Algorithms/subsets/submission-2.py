class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []
        def dfs(i):
            if i == len(nums):
                ans.append(path[:])
                return
            
            dfs(i+1)
            path.append(nums[i])
            dfs(i+1)
            path.pop()
        dfs(0)
        return ans