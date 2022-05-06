class TrieNode:
    def __init__(self):
        self.next = {}
        self.isEnd = False 
        
class Solution:
    def add(self, word, root):
        cur = root
        for ch in word:
            if ch not in cur.next:
                cur.next[ch] = TrieNode()
            cur = cur.next[ch]    
        cur.isEnd = True  
        
    def dfs_get_matchs(self, cur, pattern, i, matchs, path):
        
        for ch in cur.next:
            path.append(ch)
            
            if cur.next[ch].isEnd:
                if (i == len(pattern) - 1 and pattern[-1] == ch) \
                   or  (i == len(pattern) and "a" <= ch <= "z"):
                    matchs.add("".join(path))
                
            if i < len(pattern) and ch == pattern[i]:
                self.dfs_get_matchs(cur.next[ch], pattern, i+1,matchs, path)
            elif "a" <= ch <= "z":
                self.dfs_get_matchs(cur.next[ch], pattern, i,matchs, path)
                
            path.pop()
            
    
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        root = TrieNode()
        for word in queries:
            self.add(word, root)
        matchs = set()
        self.dfs_get_matchs(root,pattern, 0 ,matchs, [])
        return [queries[i] in matchs for i in range(len(queries))]
        
