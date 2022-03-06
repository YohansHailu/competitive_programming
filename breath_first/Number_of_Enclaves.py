class Solution:
    def dfs_make_zero(self, source, grid):
        i,j = source
        grid[i][j] = 0
        
        dirs = (0,1,0,-1,0) 
        for d in range(len(dirs) - 1):
            
            ni = i + dirs[d]
            nj = j + dirs[d+1]
            
            if not (0<= ni < len(grid) and 0<= nj < len(grid[0])):
                continue
            if grid[ni][nj] == 0:
                continue
            
            self.dfs_make_zero((ni,nj), grid)
             
        
        
    def numEnclaves(self, grid: List[List[int]]) -> int:
       
        
        for i in [0,len(grid)-1]:
            for j in range(0,len(grid[0])):
                
                if grid[i][j] == 1:
                    self.dfs_make_zero((i,j), grid)
                
                
        for i in range(0,len(grid)):
            for j in [0,len(grid[0])-1]:
            
                if grid[i][j] == 1:
                    self.dfs_make_zero((i,j), grid)
        
        count = 0 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
                    
        return count
