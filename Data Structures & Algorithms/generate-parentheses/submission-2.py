class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        def backtrack(path, open_, close):
            
            if len(path) == 2 * n:
                res.append("".join(path))
            
            if open_ < n:
                path.append("(")
                backtrack(path, open_ + 1, close)
                path.pop()
                
            if close < open_:
                path.append(")")
                backtrack(path,open_, close+1)
                path.pop()

        backtrack(path, 0, 0)
        return res