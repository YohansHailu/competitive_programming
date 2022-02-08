class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        suf_pro = [1]
        pre_pro = [1]
        
        for i in range(len(nums)):
            pre_pro.append(pre_pro[-1]*nums[i])
            suf_pro.append(suf_pro[-1]*nums[len(nums)-i-1])
            
        suf_pro.reverse() 
        ans = []
        for i in range(len(nums)):
            ans.append(pre_pro[i] * suf_pro[i+1])
        return ans
       
