class RecentCounter:

    def __init__(self):
        self.timeStack = list()
        
        

    def ping(self, t: int) -> int:
        
        
        ans = 0
        i = len(self.timeStack)-1
        while i>=0 and (t - self.timeStack[i]) <= 3000:
            ans += 1
            i -= 1
            
        self.timeStack.append(t)
        return ans+1
        

