class Solution:
    def coin_helper(self,amount, coin_count, coins, memory):
        if amount in memory:
            return coin_count + memory[amount]
        
        min_coins = sys.maxsize
        for acoin in coins:
            if amount - acoin > 0:
                ith_count = self.coin_helper(amount - acoin, 1, coins, memory)
                min_coins = min(min_coins, ith_count)
        
        memory[amount] = min_coins
        return coin_count + memory[amount] 
        
        
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        memory = dict()
        memory[0] = 0
        for i in coins:
            memory[i] = 1
            
        result = self.coin_helper(amount, 0, coins, memory) 
        if result == sys.maxsize:
            return -1
        return result
            
