class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        freq = Counter(s)
        
        visited = set()
        stack = []
        
        for ch in s:
            if ch in visited:
                freq[ch] -= 1
                continue
            
            while len(stack) > 0  and ch < stack[-1] and freq[stack[-1]] > 1:
                freq[stack[-1]] -= 1
                visited.remove(stack[-1])
                stack.pop()
            
            stack.append(ch)
            visited.add(ch)
                
        return "".join(stack)
