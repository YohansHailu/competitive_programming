class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for bits in range(2**len(nums)):
            subSet = []
            for i in range(len(nums)):
                if bits & 1<<i: subSet.append(nums[i])
            res.append(subSet)        
        return res 
