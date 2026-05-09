class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        def dfs(start_index, curr_sum):
            if curr_sum == target:
                res.append(path[:])
                return 
            
            if curr_sum > target:
                return 

            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i] > target:
                    break
                
                path.append(candidates[i])
                dfs(i + 1, curr_sum + candidates[i])
                path.pop()

        dfs(0, 0)
        return res

