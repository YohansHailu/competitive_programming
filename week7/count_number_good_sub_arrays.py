class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
       
        ans = 0
        
        odd_pre = 0
        odd_dict = {0:1}
        
        for elmt in nums:
            if elmt % 2 != 0:
                odd_pre += 1
                
            if odd_pre - k in odd_dict:
                ans += odd_dict[ odd_pre - k]
                
            odd_dict[ odd_pre ] = odd_dict.get( odd_pre,0) + 1
            
            
        return ans
                
        
