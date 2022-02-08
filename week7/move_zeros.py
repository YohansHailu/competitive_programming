class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left = 0
        right = 1
        
        while right < len(nums) and left < len(nums):
            
            # left must be zero
            while left < len(nums) and nums[left] != 0:
                left += 1
            
            # right must be none zeor
            while right < len(nums) and nums[right] == 0:
                right += 1
                
            if left >= right:
                right = left +1 
                
            if right < len(nums):
                nums[left] = nums[right]
                nums[right] = 0
            
            
