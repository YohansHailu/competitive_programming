class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        

    def addNum(self, num: int) -> None:
        if len(self.minheap) == 0:
            heappush(self.minheap,num)
            return
            
        if num >= self.minheap[0]:
            heappush(self.minheap,num)
        else:
            heappush(self.maxheap,-1*num)
        
        if len(self.minheap) - len(self.maxheap) == 2:
            heappush(self.maxheap,-1*heappop(self.minheap))
        
        if len(self.maxheap) - len(self.minheap) == 2:
            heappush(self.minheap,-1*heappop(self.maxheap))

    def findMedian(self) -> float:
        
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + (-1)*self.maxheap[0])/2
        
        return self.minheap[0] if len(self.minheap) > len(self.maxheap) else (-1)*self.maxheap[0]
        
