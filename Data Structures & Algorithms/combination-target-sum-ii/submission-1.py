class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        n = len(candidates)
        candidates.sort()
        def backtrack(i, s):
            # base case 
            if s > target:
                return
            if s == target:
                ans.append(path[:])
                return 
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                path.append(candidates[j])
                backtrack(j + 1, s + candidates[j])
                path.pop()
        backtrack(0, 0)
        return ans