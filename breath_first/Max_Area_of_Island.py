class Solution:
    def traverse_land(self, grid, i, j):
         
        grid[i][j] = 0
        
        area = 0
        dir = (0, 1, 0, -1, 0)
        for di in range(len(dir) - 1):
            new_i = i + dir[di]
            new_j = j + dir[di + 1] 
            
            if not ( 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) ):
                    continue
                    
            if grid[new_i][new_j] == 1:
                   area += self.traverse_land(grid, new_i, new_j)
                    
        return area + 1
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.traverse_land(grid,i,j)
                    max_area = max(area, max_area)
                    
        return max_area 
