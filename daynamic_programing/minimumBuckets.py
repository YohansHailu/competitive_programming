class Solution:
    def minimumBuckets(self, s: str) -> int:
        s = list(s) 
        res = 0 
        
        for i in range(1, len(s)-1):
            if s[i] != ".":
                continue
                
            if s[i-1] + s[i+1] == "HH":
                res += 1
                s[i-1:i+2]  = "???"
        
        for i in range(len(s)):
            if s[i] != ".":
                continue
            
            if i+1 < len(s) and s[i+1] == "H":
                s[i+1] = "?"
                res += 1
            
            if i-1 >= 0 and s[i-1] == "H":
                s[i-1] = "?"
                res += 1
                
        for i in s:        
            if i == "H":
                return -1
            
        return res
