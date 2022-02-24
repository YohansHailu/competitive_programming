    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        maxheap = [] 
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                
                if len(maxheap) < k:
                    heappush(maxheap,-1*matrix[i][j])
                else:
                    heappushpop(maxheap,-1*matrix[i][j])
        
        return -1*maxheap[0]
