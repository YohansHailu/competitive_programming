class Solution:
    def dfs(self, i):
        if self.ratings[i] <= self.ratings[i+1]:
            if self.ratings[i] == self.ratings[i-1]:
                self.res[i] = 1
            else:
                self.res[i] = self.res[i-1] + 1
            return
        
        self.dfs(i+1) 
        if self.ratings[i] == self.ratings[i-1]:
            self.res[i] = self.res[i+1] + 1
        else:
            self.res[i] = max(self.res[i-1], self.res[i+1]) + 1
            
            
    def candy(self, ratings: List[int]) -> int:
        
        
        self.ratings = [-1] + ratings + [float("inf")]
        self.res = [0] + [0]*len(ratings) + [0]
        
        for i in range(1, len(ratings)+1):
            if self.res[i] == 0:
                self.dfs(i)
                
        return sum(self.res) 
