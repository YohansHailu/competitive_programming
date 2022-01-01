class Solution:
    def myPow(self,num,k):
        ##calculating num^k
        ## k always  even
        if k == 0:
            return 1
        elif k == 1:
            return num
        
        half_pow = self.myPow(num, k//2) % (10**9 + 7) 
        
        return half_pow * half_pow * num **(k%2)
        
        
    def countGoodNumbers(self, n: int) -> int:
        ans = self.myPow(20, n//2) ## 4*5 = 20
        ans *= 5**(n%2) ## last one 5 if odd
        
        return ans % (10**9 + 7) 
        
     
