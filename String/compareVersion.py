class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1 = v1 + ".0"*(len(v2) - len(v1))
        v2 = v2 + ".0"*(len(v1) - len(v2))
        
        v1 = v1.split(".") 
        v2 = v2.split(".") 
        
        for i, val in enumerate(v1):
            if val == v2[i]:
                continue
                
            if int(val) > int(v2[i]):
                return 1
            
            elif int(val) < int(v2[i]):
                return -1
            
        return 0 
        
