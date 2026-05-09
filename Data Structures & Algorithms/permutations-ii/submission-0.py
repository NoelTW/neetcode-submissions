class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = [] 
        visit = set()
        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            inner_visit = set()
            for i in range(len(nums)):
                if i in visit or nums[i] in inner_visit:
                    continue
                visit.add(i)
                inner_visit.add(nums[i])
                path.append(nums[i])
                backtrack()
                path.pop()
                visit.remove(i)
        
        backtrack()
        return res
