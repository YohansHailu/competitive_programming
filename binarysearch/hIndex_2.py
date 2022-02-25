class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        ans = 0
        left = 0
        n = len( citations );
        right = len( citations )-1
        
        while left <= right:
            
            mid = left + (right-left)//2 
            
            hindex = n - mid
            valied = citations[mid] >= hindex 
            if valied:
                ans = hindex
                right = mid - 1
            else:
                left = mid + 1
                
        return ans
