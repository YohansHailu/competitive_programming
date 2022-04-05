class Solution:
    def get_closest_to_end(self, end, events):
        l = 0
        r = len(events) - 1 
        best = -1 
        
        while l <= r:
            mid = (l + r)//2
            
            if events[mid][0] > end:
                best = mid
                r = mid - 1    
            else:
                l = mid + 1
                
        return best
    
        
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        events = events
        dp = [[0,-1,-1] for i in range(len(events))] 
        
        dp[-1] = [0, events[-1][2], events[-1][2]]
        
        mx = max(dp[-1]) 
        
        n = len(events)
        
        dp.append( [0,0,0] )
        
        
        for i in range(n-2, -1, -1):
            for j in range(1,3):
                
                ni = self.get_closest_to_end(events[i][1], events)
                    
                
                if j == 1:
                    dp[i][j] = max(events[i][2], dp[i+1][j])
                    
                if j == 2:
                    dp[i][j] = max(events[i][2] + dp[ni][j-1], dp[i+1][j] )
                    
                mx  = max(mx, dp[i][j])
                
        return mx
