class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()

                if token == "+":
                    new_num = num1 + num2
                elif token == "-":
                    new_num = num2 - num1
                elif token == "*":
                    new_num = num1 * num2
                else:
                    new_num = int(num2 / num1)

                stack.append(new_num)
        
        return stack[0]

                