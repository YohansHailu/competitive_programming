class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left_w = 0
        right_w = sum(nums[1:])
        
        if right_w == left_w:
            return 0
        
        for i in range(1,len(nums)):
            
            left_w += nums[i-1]
            right_w -= nums[i]
        
            if right_w == left_w:
                return i
            
        return -1
