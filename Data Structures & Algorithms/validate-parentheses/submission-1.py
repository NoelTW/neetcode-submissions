class Solution:
    def isValid(self, s: str) -> bool:
        check_board = {
            "[" : "]",
            "{": "}",
            "(": ")"
        }
        stack = []
        for sub_s in s:
            if sub_s in check_board.keys():
                stack.append(sub_s)
            elif stack :
                pop = stack.pop()
                if check_board[pop] != sub_s:
                    return False
            else:
                return False

        if stack:
            return False
        return True

                       
                
