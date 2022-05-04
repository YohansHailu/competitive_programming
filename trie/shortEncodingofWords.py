class TrieNode:
    def __init__(self):
        self.next_nodes = {}
       
    
class Solution:
    def add(self, word, root):
        cur = root
        for ch in word:
            if ch not in cur.next_nodes:
                cur.next_nodes[ch] = TrieNode()
            cur = cur.next_nodes[ch]
        
    def isPrefix(self, word, root):
        cur = root
        for ch in word:
            if ch not in cur.next_nodes:
                return False
            cur = cur.next_nodes[ch]
        return len(cur.next_nodes) != 0
    
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = TrieNode()
        words = set(words)
        for word in words:
            word = reversed(word)
            self.add(word, root)
        
        res = sum(map(len, words)) + len(words)
        for word in words:
            word = list(reversed(word))
            if self.isPrefix(word, root):
                res -= len(word) + 1
        
        return res 
