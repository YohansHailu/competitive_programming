class node:
    def __init__(self):
        self.next_nodes = {} 
        self.isEnd = False   
        
class Trie:
        
    def __init__(self):
        self.root = node() 
        

    def insert(self, word: str) -> None:
        cur = self.root
        for lt in word:
            if lt not in cur.next_nodes:
                cur.next_nodes[lt] = node()
            cur = cur.next_nodes[lt]
        cur.isEnd = True
        
    def search(self, word: str) -> bool:
        cur = self.root
        
        for lt in word:
            if lt not in cur.next_nodes:
                return False
            cur = cur.next_nodes[lt]
            
        return cur.isEnd == True 

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for lt in prefix:
            if lt not in cur.next_nodes:
                return False
            cur = cur.next_nodes[lt]
            
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
