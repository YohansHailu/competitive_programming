  class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:      
        res = set()
        for bits in range(2**len(nums)):
            subSet = []
            for i in range(len(nums)):
                if bits & 1<<i: subSet.append(nums[i])
            res.add(subSet)        
        return res 
