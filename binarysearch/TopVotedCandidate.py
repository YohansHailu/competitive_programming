class TopVotedCandidate:
    # who was leading before zero
    def bs_last(self,arr,target):
        
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) //2
            
            if target >= arr[mid]:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
        
        
        
    def __init__(self, persons: List[int], times: List[int]):
        self.times = times;
        
        self.leaderAt = []
        
        ## counting sort
        self.count = [0] * (5000 + 1)
        maxperson = 0
        
        for person in persons:
            self.count[person] += 1
            if self.count[person] >= self.count[maxperson]:
                maxperson = person 
            self.leaderAt.append(maxperson)
        
    def q(self, t: int) -> int:
        
        tindex = self.bs_last(self.times,t)
        
        return self.leaderAt[tindex]
