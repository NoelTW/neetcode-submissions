class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        cur_val = 0
        for token in tokens:
            

            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                
                match token:
                    case "+":
                        if stack:
                            pop_1 = stack.pop()
                            pop_2 = stack.pop()
                            stack.append(pop_2 + pop_1)
                    case "-":
                        if stack:
                            pop_1 = stack.pop()
                            pop_2 = stack.pop()
                            stack.append(pop_2 - pop_1)
                    case "*":
                        if stack:
                            pop_1 = stack.pop()
                            pop_2 = stack.pop()
                            stack.append(pop_2 * pop_1)
                    case "/":
                        if stack:
                            pop_1 = stack.pop()
                            pop_2 = stack.pop()
                            stack.append(int(pop_2 / pop_1))
        return stack.pop()


                            