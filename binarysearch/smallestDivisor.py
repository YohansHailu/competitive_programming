class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        ans = 10**6
        
        left = 1
        right = max(nums) # this will give me the min
        
        while left <= right: 
            mid = left + (right - left) //2
            
            dsum = 0
            for val in nums:
                dsum += math.ceil(val/mid)
            
            if dsum <= threshold:
                ans = mid 
                right = mid - 1
            else: 
                left = mid + 1
                
        return ans 
