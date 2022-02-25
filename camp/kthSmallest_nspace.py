class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        
        # make the heap
        minheap = []
        for i in range(len(matrix)):
            heappush(minheap, (matrix[i][0],i,0) )
        
        for _ in range(k):
            poped = heappop(minheap)
            i = poped[1]
            j = poped[2]
            
            if j+1 < len(matrix[i]):
                heappush(minheap, (matrix[i][j+1],i,j+1) )
        
        return poped[0]
