KEYBOARD = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        path = []
        ans = []
        n = len(digits)
        def dfs(i):
            if i == n:
                ans.append("".join(path))
                return 
            for d in KEYBOARD[int(digits[i])]:
                path.append(d.lower())
                dfs(i + 1)
                path.pop()
        dfs(0)
        return ans


