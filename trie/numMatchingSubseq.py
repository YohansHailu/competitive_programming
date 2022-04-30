class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        kinda_trie = defaultdict(list) 
        for word in words:
            kinda_trie[word[0]].append(word[1:])
            
        res = 0     
        for ch in s:
            if ch not in kinda_trie:
                continue
                
            next_words = kinda_trie[ch].copy()
            del kinda_trie[ch]
            
            for word in next_words:
                if word == "":
                    res += 1
                    continue
                kinda_trie[word[0]].append(word[1:])
                
        return res    
