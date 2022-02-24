    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxheap = stones
        # heapifying
        for i in range(len(stones)):
            maxheap[i] = -1*maxheap[i]
        heapify(maxheap)
        
        while len(maxheap) > 0:
            fmax = -1*heappop(maxheap)
            if len(maxheap) == 0:
                return fmax
            
            smax = -1*heappop(maxheap)
            
            new = fmax-smax
            if new != 0: 
                heappush(maxheap,-1*new)
         
        return 0
