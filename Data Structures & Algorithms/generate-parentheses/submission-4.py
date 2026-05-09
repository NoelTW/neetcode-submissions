class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = []
        def dfs(i, o, c):
            if i == 2 * n:
                ans.append("".join(path))
                return 
            if o < n:
                path.append("(")
                dfs(i + 1, o + 1, c)
                path.pop()
            if c < o:
                path.append(")")
                dfs(i + 1, o, c+1)
                path.pop()
        dfs(0, 0, 0)
        return ans