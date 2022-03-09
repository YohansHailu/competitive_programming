 def min_cost_helper(self, index, cost,memory):
        if memory[index] != -1: 
            return memory[index]
        
        if index >= len(cost) - 2:
            memory[index] = cost[index]
            return cost[index]
        
        a = self.min_cost_helper(index + 1, cost, memory)
        b = self.min_cost_helper(index + 2, cost, memory)
        
        min_cost = cost[index] + min(a,b)
        
        memory[index] = min_cost
        return min_cost 
        
        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memory = [-1]*len(cost)
        first = self.min_cost_helper(0, cost, memory)
        second = self.min_cost_helper(1, cost, memory)
        
        return min(first, second)
