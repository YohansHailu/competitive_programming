class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        row = 0 
        
        left = 0 
        right = len(matrix) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if target >= matrix[mid][0]:
                row = mid
                left = mid + 1
            else:
                right = mid - 1
            
        print(row)
        left = 0 
        right = len(matrix[row]) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if matrix[row][mid] == target:
                return True
            
            if target > matrix[row][mid]:
                left = mid + 1
                
            elif target < matrix[row][mid]:
                right = mid - 1
        
        return False
