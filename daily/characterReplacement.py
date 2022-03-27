class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0 
        for letter in set(s):
            
            win_count = 0 
            left = 0
            for right in range(len(s)):
                win_count += 1 if s[right] != letter else 0
                while win_count > k:
                    win_count -= 1 if s[left] != letter else 0
                    left += 1 
                ans = max(ans, right - left + 1)
                
                
        return ans      
            
