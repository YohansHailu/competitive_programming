    def get_closest(self, end, rides):
        l = 0
        r = len(rides) - 1
        best = len(rides) 
        
        while l <= r:
            m = (l + r)//2
            
            if rides[m][0] >= end:
                best = m
                r = m - 1
            else:
                l = m + 1
                
        return best 
   

    def helper(self, i, rides):
        
        #
        if i >= len(rides):
            return 0
        
        if i in self.memo:
            return self.memo[i]
        
        not_taken = self.helper(i+1, rides)
        
        # taken
        ni = self.get_closest(rides[i][1], rides)
        
        rev = sum(rides[i]) - 2*rides[i][0]
        taken = rev + self.helper( ni, rides)
        
        self.memo[i] = max(not_taken, taken) 
        return self.memo[i]
        
        
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        self.memo = dict()
        return self.helper(0, rides)
        
