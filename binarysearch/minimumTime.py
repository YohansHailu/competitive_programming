class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 1
        right = totalTrips*min(time)
        ans = 0 
        while left <= right:
            midtime = left + (right - left)//2
            
            trip_count = 0 
            for bus in time:
                trip_count += math.floor(midtime / bus)
            
            if trip_count >=  totalTrips:
                ans = midtime
                right = midtime - 1
            else:     
                left = midtime + 1
                                       
                

        return ans 
                
