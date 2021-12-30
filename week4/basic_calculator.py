from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        
        s_list = []
        
        for i in s:
            if i != " ":
                s_list.append(i)
                
                
        num_stack = deque()
        op_stack = deque()
        i = 0
        while i < len(s_list):
            
            if s_list[i] in "+-":
                op_stack.append(s_list[i])
         
            else:
                j = i
                while j+1<len(s_list) and s_list[j+1] not in "+-/*":
                    j += 1
                    
                if s_list[i] == "*":
                    num_stack[-1] *= int( "".join(s_list[i+1:j+1]) )
                    
                elif s_list[i] == "/":
                    num_stack[-1] //= int( "".join(s_list[i+1:j+1]) )
                else:
                    num_stack.append(int( "".join(s_list[i:j+1]) ))
            
                i = j
                
            i += 1
                    
        
        while len(op_stack) > 0:
            op = op_stack.popleft()
            num1 = num_stack.popleft()
            num2 = num_stack.popleft()
            
            if op == "+":
                num_stack.appendleft(num1 + num2)
            elif op == "-":
                num_stack.appendleft(num1 - num2)
            
        return num_stack[-1]
            
            
