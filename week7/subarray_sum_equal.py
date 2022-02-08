class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # have a prifix sum
        # zero in prefix sum
        
        # dictionary of prefix sum with count
        
        
        pre_sum = 0
        for elmt in nums:
            pre_sum += elmt
    
    
        ans = 0
        pre_dict = {}
        for elmt in pre_sum:
            # elmt - k = x 
            if (elmt - k) in pre_dict:
                ans += pre_dict[elmt-k]
                
            pre_dict[elmt] = pre_dict.get(elmt,0) + 1
        return ans
