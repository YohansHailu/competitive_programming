class Solution:
    def path_sum(self, point, grid, memo):
        i, j = point
        if memo[i][j] != None:
            return memo[i][j]
     
        if (i,j) == (len(grid) - 1, len(grid[0]) - 1):
            return grid[i][j]
        
        left_sum = sys.maxsize
        right_sum = sys.maxsize
        
        if j + 1 < len(grid[0]):
            left_sum = self.path_sum( (i,j+1), grid, memo)
            
        if i + 1 < len(grid):
            right_sum = self.path_sum( (i+1,j), grid, memo)
        
        memo[i][j] = grid[i][j] + min(left_sum, right_sum)
        
        return memo[i][j]
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0]) 
        m = len(grid) 
        memo = [ [ None for i in range(n)] for _ in range(m) ]
        start = (0,0) 
        return self.path_sum(start, grid, memo)
       
        
