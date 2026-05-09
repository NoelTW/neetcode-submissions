class Solution:
    def partition(self, s: str) -> List[List[str]]:
    
        res = []

        def check(l, r, string):
            while l < r :
                if string[l]!= string[r]:
                    return False
                l += 1
                r -= 1
            return True

        path = []
        def backtrack(start_index):
            if start_index == len(s):
                res.append(path[:])
                return
            
            for i in range(start_index, len(s)):
                if not check(start_index, i, s):
                    continue
                path.append(s[start_index:i + 1])
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return res