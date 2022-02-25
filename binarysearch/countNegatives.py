class Solution:
    def bs_frist_neg(self,arr,right):
        # the array is dicreasing 
        if right >= len(arr):
            return -1 
        
        ans = -1 
        
        left = 0
        
        while left <= right:
            mid = left + (right - left)//2
            
            if arr[mid] < 0:
                ans = mid
                right = mid-1
            else:
                left = mid+1
                
        return ans 
        
    def countNegatives(self, grid: List[List[int]]) -> int:
        # start from the last
        ans = 0
        m = len(grid)
        n = len(grid[0])
        
        index = n-1 
        for i in range(m):
            
            index = self.bs_frist_neg(grid[i], index if index != -1 else n-1 )
            
            if index != -1:
                ans += n-index
                 
        return ans 
