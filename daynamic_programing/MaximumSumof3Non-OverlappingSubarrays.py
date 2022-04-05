class Solution:
    def helper(self, i, k, count, nums):
         
        if i >= len(nums):
            return tuple([0])
        
        if count == 0: 
            return tuple([0])
        
        if (i, count) in self.memo: 
            return self.memo[(i, count)]
       
    
         # not take it
        not_taken = self.helper(i+1, k, count, nums)
       
        # taken
        taken = self.helper(i+k, k, count-1, nums)
        
        taken = list(taken)
        
        taken.append(i)
        taken[0] += self.get_wsum[i]
        
        taken = tuple(taken)
        
        if not_taken[0] > taken[0]:
            taken = not_taken
        
        self.memo[(i,count)] = taken
        return taken
        
        
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        self.get_wsum =  defaultdict(int) 
        l = 0
        wsum = sum(nums[0:k])
        self.get_wsum[0] = wsum 
        
        for r in range(k, len(nums)):
            wsum += nums[r]
            wsum -= nums[l]
            
            l += 1
            self.get_wsum[l] = wsum 
            
            
        
        self.memo = dict()
        return sorted(self.helper(0, k, 3, nums)[1:])
