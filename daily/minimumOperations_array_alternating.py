    def get_first_second_majority(self, freq):
        fmaj = 0 
        smaj = 0 
        
        for elm in sorted(freq.keys(), key = lambda x:freq[x]):
            if freq[elm] >= freq[fmaj]:
                smaj = fmaj
                fmaj = elm
                
        return (fmaj, smaj)        
            
        
        
    def minimumOperations(self, nums: List[int]) -> int:
        efreq = Counter(nums[0:len(nums):2])
        ofreq = Counter(nums[1:len(nums):2])
        
        efreq[0] = 0
        ofreq[0] = 0
        
        even_m = self.get_first_second_majority(efreq)
        odd_m = self.get_first_second_majority(ofreq)
        
        if odd_m[0] != even_m[0]:
            return len(nums) - (ofreq[odd_m[0]] + efreq[even_m[0]])
        
        return len(nums) - max(efreq[even_m[0]] + ofreq[odd_m[1]] \
                               , ofreq[odd_m[0]] + efreq[even_m[1]])
        
        
