class Solution:
    def isIsomorphic(self, a: str, b: str) -> bool:
        if len(a) !=  len(b):
            return False
        
        visited = set()
        maped = dict()
        for i, ch in enumerate(a):
            if ch in maping:
                if maping[ch] != b[i]: return False
            else:    
                if b[i] in maped: return False
                maping[ch] = b[i]; maped.add(b[i])
        return True 
