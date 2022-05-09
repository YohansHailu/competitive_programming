class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs, key = lambda elt:len(elt)) 
        for s in strs:
            i = 0
            
            while i < len(prefix) and s[i] == prefix[i]:
                i += 1
            prefix = prefix[:i]
            
        return prefix
