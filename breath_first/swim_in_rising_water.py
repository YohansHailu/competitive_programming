class Solution:
    def djk(self, start, grid, minheap = list(), visited = set()):
        cost, i, j = start
        if (i, j) == (len(grid)-1, len(grid[0])-1):
            return start 
        
        visited.add( (i,j) ) 
        
        dirs = (0,1,0,-1,0)
        for d in range(len(dirs) - 1):
            
            ni = i + dirs[d]
            nj = j + dirs[d+1]
            
            if not (0<= ni < len(grid) and 1<= nj < len(grid[0])):
                continue
                
            if (ni, nj) in visited:
                continue
            
            new_cost = grid[ni][nj] - grid[i][j]
            new_cost = 0 if  new_cost < 0  else new_cost 
                
            heappush(minheap, (cost + new_cost, ni, nj) )
        
        
        next_point = heappop(minheap)
        
        return self.djk(next_point, grid, minheap, visited)
        
    def swimInWater(self, grid: List[List[int]]) -> int:
        
            return self.djk( (0,0,0), grid)[0]
        
