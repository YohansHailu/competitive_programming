class TrieNode:
    def __init__(self):
        self.next_nodes = [None]*26
        self.isEnd = False


class Solution:
    def add(self, word, trie_root):
        cur = trie_root
        for letter in word:
            index = ord(letter) - ord("a")
            if cur.next_nodes[index] is None:
                cur.next_nodes[index] = TrieNode()
            cur = cur.next_nodes[index]
        cur.isEnd = True

    def dfs(self, cur_node, arr_size, path, arr):
        next_nodes = cur_node.next_nodes
        for i in range(len(next_nodes)):
            if len(arr) == arr_size:
                return

            if next_nodes[i] is None:
                continue

            letter = chr(i+ord('a'))
            path.append(letter)

            if next_nodes[i].isEnd:
                arr.append("".join(path))

            self.dfs(next_nodes[i], arr_size, path, arr)
            path.pop()

    def suggestedProducts(self, products, searchWord: str):
        trie_root = TrieNode()
        for word in products:
            self.add(word, trie_root)

        res = []
        cur = trie_root

        for i, letter in enumerate(searchWord):

            index = ord(letter) - ord("a")
            if cur:
                cur = cur.next_nodes[index]
            suggs = []
            if cur and cur.isEnd:
                suggs.append(searchWord[:i+1])
            if cur:
                self.dfs(cur, 3, [searchWord[:i+1]], suggs)
            res.append(suggs)
            
        return res
