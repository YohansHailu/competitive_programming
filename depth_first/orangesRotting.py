class Solution:
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        que = deque()
        
        for i in range( len(grid) ):
            for j in range( len(grid[0]) ):
                
                if grid[i][j] == 2:
                    que.append( (i,j) )
                
        level = 0 
        while len(que) > 0:
            
            for _ in range( len(que) ):
                i,j = que.popleft()
                
                dirs = (0, 1, 0, -1, 0)
                for d in range( len(dirs) - 1 ):
                    
                    ni = i + dirs[d]
                    nj = j + dirs[d + 1]
                    
                    if not ( 0<= ni < len(grid) and 0<= nj < len(grid[0]) ):
                        continue
                    
                    if grid[ni][nj] in [2,0]:
                        continue
                    
                    grid[ni][nj] = 2
                    que.append( (ni,nj) )
               
            level += 1 
           
        
        
        for i in range( len(grid) ):
            for j in range( len(grid[0]) ):
                if grid[i][j] == 1:
                    return -1
        if level == 0:        
            return 0
        return level - 1 
