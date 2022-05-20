# in case anybody is reading this. thank you for your attention
# but try to google rolling-hash first

# I used 30bits for the rollinghash for substring of length 10

# each charactor is coded by 3 bits one for offset. I dont' why it doesn't work by 2 bits
# And so, put each charactor bit codes in order at the hash and update the hash as the window slide


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10: 
            return []
        
        BIT_LEN = 3 
        LEN = 10 
        
        char_map = {"A":1, "C":2, "G":3, "T":4}
        cur_hash = 0
        
        for i in range(LEN):
            cur_hash <<= BIT_LEN
            cur_hash |= char_map[s[i]]
            
        hash_set = set() 
        hash_set.add(cur_hash) 
       
        res = set()
        
        left = 0
        mask = (1<<LEN * BIT_LEN) - 1 # 20 on bits
        for right in range(LEN, len(s)):
            cur_hash <<= BIT_LEN
            cur_hash &= mask 
            left += 1
            
            cur_hash |= char_map[s[right]]
            
            if cur_hash in hash_set:
                res.add(s[left:right+1])
                
            hash_set.add(cur_hash)    
        
        return res
     
