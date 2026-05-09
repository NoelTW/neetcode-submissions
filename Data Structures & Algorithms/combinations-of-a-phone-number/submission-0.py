class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        
        def backtrack(index, path):
            key_map = ["","","abc", "def", "ghi", "jkl", "mno","pqrs","tuv","wxyz"]
            if len(path) == len(digits):
                if path:
                    res.append("".join(path[:]))
                return 
            key = digits[index]
            for char in key_map[int(key)]:
                path.append(char)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return res