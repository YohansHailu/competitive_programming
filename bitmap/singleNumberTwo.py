class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(31,-1,-1):
            count = 0
            for num in nums:
                count += num & 1<<i and 1
            ans |= (count % 3 != 0)
            ans <<= 1
            
        ans >>= 1    
        result = 0
        for i in range(32):
            result += (ans & 1) * 1<<i 
            ans >>= 1
            
        return (-1*(ans & 1) * 1 << 32)   + result
            
            
        
