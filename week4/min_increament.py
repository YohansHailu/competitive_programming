class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        nums.sort()
        total_op = 0
        for i in range(len(nums)-1):
            
            if nums[i+1] <= nums[i]:
                diff = nums[i] - nums[i+1]
                nums[i+1] += diff+1
                total_op += diff+1
                
        
        return total_op
