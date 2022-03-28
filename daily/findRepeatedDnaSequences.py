class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # ten letters so the window is 10
        
        if len(s) < 10:
            return []
        
        respo = set()
        ans = set()
        
        left = 0
        
        for i in range(10,len(s)+1):
            win = s[left:i]
            if win in respo:
                ans.add(win)
            else:    
                respo.add(win)
            left += 1
            
        return ans 
