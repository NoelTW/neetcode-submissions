class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = []
        ans = []
        used = [0] * n
        def backtrack():
            if len(path) == n:
                ans.append(path[:])
                return 
            for j in range(n):
                if used[j] == 1:
                    continue
                used[j] = 1
                path.append(nums[j])
                backtrack()
                used[j] = 0
                path.pop()
        backtrack()
        return ans