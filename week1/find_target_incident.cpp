class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort();
        index = -1;
        
        try:
            index = nums.index(target);
        except:
            index = -1;
            
        result = []
        if index != -1:
            result.append(index);
            while index+1 < len(nums) and nums[index] == nums[index+1]:
                index+=1;
                result.append(index)
        return result
