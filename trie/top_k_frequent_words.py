class trieNode:
    def __init__(self):
        self.next_nodes = {} 
        self.end_count = 0
        
class Solution:
    def __init__(self):
        self.trie_root = trieNode()
        
    def add_to_trie(self, word):
        cur = self.trie_root
        for ch in word:
            if ch not in cur.next_nodes:
                cur.next_nodes[ch] = trieNode()
            cur = cur.next_nodes[ch]
        cur.end_count += 1        
        
    def make_maxheap(self, cur, path, maxheap):
        for next_ch in cur.next_nodes:
            path.append(next_ch)        
            
            next_node = cur.next_nodes[next_ch]
            self.make_maxheap(next_node, path, maxheap)
            
            if next_node.end_count > 0:
                word = "".join(path)
                count = next_node.end_count
                heappush(maxheap, (-1*count, word))
                
            path.pop()       
        
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        for word in words:
            self.add_to_trie(word)
            
        maxheap = []
        self.make_maxheap(self.trie_root, [], maxheap)
        
        res = [] 
        for _ in range(k):
            res.append(heappop(maxheap)[1])
        return res
        
        
