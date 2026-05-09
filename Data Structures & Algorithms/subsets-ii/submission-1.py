class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = []
        ans = []
        nums.sort()
        def dfs(i):
            ans.append(path.copy())
            for j in range(i, n):
                if j > i and nums[j - 1] == nums[j]:
                    continue
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
        dfs(0)
        return ans