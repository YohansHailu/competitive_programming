class trie_node:
    def __init__(self):
        self.next_nodes = {}
        self.isend = False
        
class WordDictionary:

    def __init__(self):
        self.root = trie_node()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.next_nodes:
                cur.next_nodes[ch] = trie_node()
            cur = cur.next_nodes[ch]    
        cur.isend = True 
    def search_help(self, word, start, cur):
         
        for i in range(start, len(word)):
            ch = word[i]
            if ch == ".":
                for ch in cur.next_nodes:         
                    if self.search_help(word, i+1, cur.next_nodes[ch]):
                        return True
                return False 
                
            if ch not in cur.next_nodes:
                return False
            cur = cur.next_nodes[ch] 
            
        return cur.isend == True  
    
    def search(self, word: str) -> bool:
        return self.search_help(word, 0, self.root)
