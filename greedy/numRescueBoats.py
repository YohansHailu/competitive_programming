class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # window size less 2 
        # start and end pointer
        
        # if start + end greter than limimt mov end
        # else move both
        
        people.sort()
        left = 0
        right = len(people) - 1
        
        n_boats = 0
        while right >= left:
            if people[right] + people[left] <= limit:
                right -= 1
                left += 1
            else:
                right -= 1
            n_boats += 1
            
        return n_boats
                
                
