class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # add each letter to dictionaray
        # with count 
        # dicrease if the window by
        
        ans = 0 
        
        count = 0
        w_dict = {}
        
        left = 0
        for right in range(len(s)):
            w_dict[s[right]] = w_dict.get(s[right],0) + 1
            count += 1
            while count > len(w_dict):
                w_dict[s[left]] -= 1
                if w_dict[s[left]] == 0:
                    w_dict.pop(s[left])
                count -= 1
                left += 1
                
            ans = max(ans,right-left+1) 
        return ans 
