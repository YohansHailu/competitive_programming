class Solution:
    def profit_helper(self, index, sell, prices, memo):
        if index >= len(prices):
            return 0
        if (index, sell) in memo:
            return memo[(index, sell)]
        
        res = self.profit_helper(index + 1, sell, prices, memo)
        
        if sell != -1:
            temp = prices[index] - sell + self.profit_helper(index + 2, -1, prices, memo)
            res = max(res,temp)
        else: 
            temp = self.profit_helper(index + 1, prices[index], prices, memo)
            res = max(res,temp)
        
        memo[(index, sell)] = res 
        return res
        
        
    def maxProfit(self, prices: List[int]) -> int:
        memo = dict()
        return self.profit_helper(0, -1, prices, memo)
        
