class Solution:
    def invert(self,s):
        for i in range(0,len(s)):
            s[i] = "0" if s[i] == "1" else "1"
        return s
    def reverse(self,s):
        for i in range(0,len(s)//2):
            s[i] , s[len(s)-i-1] =  s[len(s)-i-1] , s[i] 
        return s
    
    def helper(self,s_count,count,n,k):
        if count >= n:
            return s_count
        
        if 2**count > k:
            return s_count
        
        s_count = s_count + ["1"] + self.reverse(self.invert(s_count))
        return self.helper(s_count,count+1,n,k)
    
    def findKthBit(self, n: int, k: int) -> str:
        
        sn = self.helper(["0"],1,n,k);
       
        return sn[k-1]
        
