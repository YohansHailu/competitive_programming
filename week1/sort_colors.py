class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            
            min_index = i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[min_index]:
                    min_index = j
            
            #swap them
            temp = nums[i]
            nums[i] = nums[min_index]
            nums[min_index] = temp
            
        
