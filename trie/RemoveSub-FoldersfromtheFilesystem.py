class TrieNode:
    def __init__(self):
        self.next_nodes = {}
        self.isEnd = False 
        
class Solution:
    def add(self, word, trie_root):
        cur = trie_root
        for ch in word:
            if ch not in cur.next_nodes:
                cur.next_nodes[ch] = TrieNode()
            cur = cur.next_nodes[ch]
        cur.isEnd = True    
        
    def contains(self, word, trie_root):
        cur = trie_root
        for ch in word:
            if ch not in cur.next_nodes:
                return False
            cur = cur.next_nodes[ch]
            
        return cur.isEnd == True    
    
    def dfs(self, cur, path, arr):
        
        for ch in cur.next_nodes:
            path.append(ch)
            
            if cur.next_nodes[ch].isEnd:
                arr.append("/" + "/".join(path))
            else:
                self.dfs(cur.next_nodes[ch], path, arr) 
                
            path.pop()
        
        
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # add all words
        trie_root = TrieNode()
        for word in folder:
            word = word.split("/")[1:]
            self.add(word, trie_root)
        
        res = []
        self.dfs(trie_root, [], res)
        return res 
