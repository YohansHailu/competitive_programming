class Solution:
    def isMatch_helper(self, s, si, pi, memo):
        if si == len(s):
            
            for i in self.fsm[pi:]:
                if len(i) != 2:
                    return False
            return True 
        
        if pi == len(self.fsm):
            return si == len(s)
        
        if (si,pi) in memo:
            return False
        
        if len(self.fsm[pi]) == 2:
            
            if self.isMatch_helper(s, si, pi+1, memo):
                return True
            
            while si < len(s) and self.fsm[pi][0] in [".", s[si] ]:
                
                if self.isMatch_helper(s, si+1, pi+1, memo):
                    return True
                si += 1
                
            memo.add((si,pi))    
            return False 
        
        if s[si] == self.fsm[pi] or self.fsm[pi] == ".":
            if self.isMatch_helper(s, si+1, pi+1, memo):
                return True
            
        memo.add((si,pi))    
        return False 
        
    def isMatch(self, s: str, p: str) -> bool:
        
        self.fsm  = []
        for i in range(len(p)):
            if p[i] == "*":
                continue
            if i < (len(p) - 1) and p[i+1] == "*":
                self.fsm.append(p[i]+p[i+1])
                continue 
            self.fsm.append(p[i])
            
            
        memo = set()        
        return self.isMatch_helper(s,0,0,memo)
