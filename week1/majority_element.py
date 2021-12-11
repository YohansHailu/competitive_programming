class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = dict()
        for i in nums:
            if i in count:
                count[i]+=1;
            else:
                count[i] = 1
        
        result = []
        for i in count:
            if count[i] > len(nums)//3:
                result.append(i)
        
        return result
        
