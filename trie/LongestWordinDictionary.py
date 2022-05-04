class TrieNode:
    def __init__(self):
        self.next_nodes = [None]*26 
        self.isEnd = False
        
class Solution:
    def add(self, word, root):
        cur = root
        for ch in word:
            index = ord(ch) - ord("a")
            if cur.next_nodes[index] == None:
                cur.next_nodes[index] = TrieNode()
            cur = cur.next_nodes[index]
        cur.isEnd = True 
        
    def dfs_helper(self, cur, path):
        res = path.copy()
        for i, node in enumerate(cur.next_nodes): 
            if node == None or node.isEnd == False:
                continue
                
            ch = chr(i + ord("a"))    
            path.append(ch) 
            dfs_res = self.dfs_helper(node, path)
            if len(dfs_res) > len(res):
                res = dfs_res
            path.pop()
            
        return res        
    
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        for word in words:
            self.add(word, root)
        res = self.dfs_helper(root, [])     
        return "".join(res)
