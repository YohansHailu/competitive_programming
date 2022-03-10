class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mx = prices[-1]
        ans = 0 
        
        for i in range(len(prices)-1, -1, -1):
            mx = max(prices[i],mx)
            ans = max(ans, mx - prices[i])
        
        return ans
