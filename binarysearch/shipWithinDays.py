class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left = max(weights) 
        right = sum(weights) 
        
        ans = right 
        
        while left <= right:
            cap = left + (right - left)//2
            
            days_cap = 0
            i = 0
            while i < len(weights):
                total_w = 0
                while i < len(weights) and total_w + weights[i] <= cap:
                    total_w += weights[i]
                    i += 1
                days_cap += 1
            
            possible = days_cap <= days
            if possible:
                ans = cap 
                right = cap - 1 # lets try with less capacity
            else:
                left  = cap + 1
        
        return ans
