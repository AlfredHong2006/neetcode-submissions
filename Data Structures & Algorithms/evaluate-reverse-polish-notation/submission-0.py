class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
            #using a stack
            #pop the last two values before the operand and replace that shit with the result from the operator

        stack = []
        for i in range(len(tokens)): 
            if tokens[i] not in ["+", "-" , "/", "*"]:
                stack.append(tokens[i])
            else:
                a = int(stack.pop(-1))
                b = int(stack.pop(-1))
                if tokens[i] == "/":
                    stack.append(int(b/a))
                elif tokens[i] =="+":
                    stack.append(b+a)
                elif tokens[i]=="-":
                    stack.append(b-a)
                else:
                    stack.append(b*a)
        return int(stack[0])
