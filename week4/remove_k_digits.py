class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack =  list()
        for i  in num:
            
            while len(stack) > 0 and k > 0 and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        
      
            
        ans = "".join(stack[:len(stack)-k])
        ans = ans.lstrip("0")
        
        if ans == "":
            return "0"
                
        return ans
