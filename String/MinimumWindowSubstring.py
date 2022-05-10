class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        org_freq = Counter(t)
        win_freq = dict() 
        win_count = 0
            
        for i in s:
            win_freq[i] = 0
        
        left_ans = -1  
        smallest_len = float("+inf")
        
        left = 0
        for right in range(len(s)):
            
            if s[right] in win_freq:
                win_count += 1 if win_freq[s[right]] < org_freq[s[right]] else 0
                win_freq[s[right]] += 1
            
            while win_count >= len(t):
                if right - left + 1 < smallest_len:
                    smallest_len = right - left + 1
                    left_ans = left
                
                if s[left] in win_freq:
                    win_count -= 1 if win_freq[s[left]] <= org_freq[s[left]] else 0
                    win_freq[s[left]] -= 1
                    
                left += 1
                
        if smallest_len == float("+inf"):
            return ""
        
        return s[left_ans:left_ans+smallest_len]
