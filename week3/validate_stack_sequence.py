class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        

        stack = []
        pop_index = 0
        
        for push_index in range(len(pushed)):
            
            stack.append(pushed[push_index])
            while len(stack) > 0 and pop_index < len(popped) and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
            
        if len(stack) == 0 and pop_index == len(popped):
            
            return True
        
        return False
            
