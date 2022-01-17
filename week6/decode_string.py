class Solution:
    def decodeString(self, s: str) -> str:
        stack_ans = []
        stack_mul = []
        i = 0
        while i < len(s):
            while i<len(s) and s[i] != "]":
                if not s[i].isdigit():
                    stack_ans.append(s[i])
                    i += 1
                else:
                    #i is a digint
                    left = i
                    right = left
                    while s[right].isdigit():
                        right += 1
                    stack_mul.append(int(s[left:right]))
                    i = right # right is the first none digit
            ## now i is not ] so we pop
            if len(stack_mul) == 0:
                continue
                
            n = stack_mul.pop()
            sub_s = []
            while len(stack_ans) > 0 and stack_ans[-1] != "[":
                sub_s.append( stack_ans.pop() )
            stack_ans.pop() ## pop the  [
            
            sub_s.reverse()
            
            stack_ans.extend( n*sub_s ) ## pushing back
            i += 1
            
        return("".join(stack_ans))
