    def myPow(self,x,n):
        if abs(n) <= 1:
            return x**n
        
        half_pow = self.myPow(x,n//2)%(pow(10,9)+7)
        
        return half_pow*half_pow * x**(n%2)
        
    def minNonZeroProduct(self, p: int) -> int:
        m = int(2**p - 1)
        n = (m-1)//2
        
        # m - 1 poweed n
        z = self.myPow(m-1,n)
        
        return int( m%(pow(10,9)+7) * z%(pow(10,9)+7) )
        
