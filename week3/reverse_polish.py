class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack  = list()
        
        for i in range(len(tokens)):
            
            if tokens[i] == "*":
                opr1 = stack.pop()
                opr2 = stack.pop()
                stack.append(int(opr1) * int(opr2))
            elif tokens[i] == "+":
                opr1 = stack.pop()
                opr2 = stack.pop()
                stack.append(int(opr2) + int(opr1))
            elif tokens[i] == "-":
                opr1 = stack.pop()
                opr2 = stack.pop()
                stack.append(int(opr2) - int(opr1))
            elif tokens[i] == "/":
                opr1 = stack.pop()
                opr2 = stack.pop()
                
                stack.append(int(opr2) / int(opr1))
            else:
                stack.append(tokens[i])
        
        return int(stack.pop())
        
