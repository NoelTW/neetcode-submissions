class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def check(path):
            """
            ((()))
            """
            stack = []
            for char in path:
                if char == "(":
                    stack.append(char)
                elif char == ")":
                    if not stack:
                        return False
                    stack.pop() 
            return len(stack) == 0

        res = []
        path = [] 
        directions = [")","("]
        def backtrack():
            if len(path) == 2 * n:
                if check(path[:]):
                    res.append("".join(path))
                return 

            for direction in directions:
                if not path and direction == ")":
                    continue
                path.append(direction)
                backtrack()
                path.pop()
        backtrack()
        
        return res