class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # number of zeros less than or equals to k
        # then valied windows
        
        
        ans = 0
        n_zeros = 0
            
        left = 0
        right = 0
        while right < len(nums):
            if left > right:
                right = left
                
            if nums[right] == 0:
                n_zeros += 1
            
            while k < n_zeros:
                if nums[left] == 0:
                    n_zeros -= 1
                left += 1
            ans = max(ans,right - left + 1)
            
            right += 1
            
        return ans 
