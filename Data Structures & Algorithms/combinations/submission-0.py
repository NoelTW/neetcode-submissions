class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        path = []

        def backtrack(start_index):
            if len(path) == k:
                res.append(path[:])
                return 
            # 需要: k - len(path)
            # 剩下: n - i + 1
            for i in range(start_index, n-(k - len(path))+2):
                path.append(i)
                backtrack(i + 1)
                path.pop()
        backtrack(1)
        return res
