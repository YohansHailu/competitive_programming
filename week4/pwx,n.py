class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif abs(n) == 1:
            return x**(n)
        
        else:
            half_power =self.myPow(x,n//2)
            return half_power * half_power  * x**(n%2);
