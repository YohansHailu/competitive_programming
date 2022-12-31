class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # two pointer
        if s == "":
            return True
        
        index = 0 
        for ch in t:
            if ch != s[index]:
                continue
                
            index += 1
            if index == len(s):
                return True
        return False    
