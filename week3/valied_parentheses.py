class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            elif s[i] == ")":
                if len(stack) == 0:
                    return False
                t = stack.pop()
                if t != "(":
                    return False
            elif s[i] == "]":
                if len(stack) == 0:
                    return False
                t = stack.pop()
                if t != "[":
                    return False
            elif s[i] == "}":
                if len(stack) == 0:
                    return False
                t = stack.pop()
                if t != "{":
                    return False
                    
        
        if len(stack) == 0:
            return True
        
        return False
        
