    def longestPalindrome(self, s: str) -> str:
        ans = (0,0)
        for i in range(1,len(s)):
            
            left = i
            right = i
            while left - 1 >= 0 and right + 1 < len(s) and s[right + 1] == s[left - 1]:
                left -= 1
                right += 1
                
            ans = max(ans, (left,right), key = lambda x: x[1] - x[0] + 1)    
            
            if s[i] == s[i-1]:
                left = i-1
                right = i
                while left - 1 >= 0 and right + 1 < len(s) and s[right + 1] == s[left - 1]:
                    left -= 1
                    right += 1
                
            ans = max(ans, (left,right), key = lambda x: x[1] - x[0] + 1)    
            
        
        return s[ans[0]:ans[1]+1] 
