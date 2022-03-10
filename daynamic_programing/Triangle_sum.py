class Solution:
    def triangle_helper(self, point, triangle, memo):
        
        i,j = point
        if memo[i][j] != None:
            return memo[i][j]
        
        if i == len(triangle) - 1:
            return triangle[i][j]
        
        right = self.triangle_helper( (i+1 ,j+1), triangle, memo)
        left =  self.triangle_helper( (i+1 ,j), triangle, memo)
            
        memo[i][j] = triangle[i][j] + min(left, right)
        return memo[i][j]
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        memo = [ [None for _ in range(len(triangle))] for _ in range(len(triangle))]
        
        return self.triangle_helper((0,0), triangle, memo)
        
        
