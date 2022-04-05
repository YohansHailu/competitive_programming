class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        
        left = 0
        right = 0
        while right < len(prices):
            
            while right + 1 < len(prices) and prices[right] == prices[right+1] + 1:
                    right += 1
                    
            n = right - left + 1
            ans += n*(n+1) // 2
            
            right += 1
            left = right
            
        return ans 
