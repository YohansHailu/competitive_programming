class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        index_map = {}
        ans = []
        for i in range(len(s)):
                index_map[s[i]] = i
                
        left = 0; right = 0
        while right < len(s):
            
            i = left
            while i <= right:
                while right < len(s) and index_map[s[i]] > right:
                    right += 1
                i += 1 
                
            ans.append(right - left+1)   
            right += 1
            left = right
            
        return ans
