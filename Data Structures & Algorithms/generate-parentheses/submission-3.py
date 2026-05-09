class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        path = []
        ans = []

        def dfs(i, c, o):
            if i == 2*n:
                ans.append("".join(path))
                return 
            if c < n:
                path.append("(")
                dfs(i + 1, c +1, o)
                path.pop()
            if o < c:
                path.append(")")
                dfs(i + 1, c, o +1)
                path.pop()
        dfs(0, 0, 0)
        return ans


