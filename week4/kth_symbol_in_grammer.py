class Solution:
    
    
    def rec_fun(self,bit,rg,k):
        if rg[0] == rg[1]:
            return bit
     

        mid = (rg[0] + rg[1])//2
        if bit == "0":
            if k <= mid:
                rg[1] = mid
                return self.rec_fun("0",rg,k)
            else:
                rg[0] = mid+1
                return self.rec_fun("1",rg,k)
        
        elif bit == "1":
            if k <= mid:
                rg[1] = mid
                return self.rec_fun("1",rg,k)
            else:
                rg[0] = mid+1
                return self.rec_fun("0",rg,k)
        
    def kthGrammar(self, n: int, k: int) -> int:
        return int( self.rec_fun("0", [1, 2**(n-1)], k) )
