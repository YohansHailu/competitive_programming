    def is_art(self,nums,left,right):
        
        mi = nums[left]
        ma = nums[right]
        
        for i in range(left,right+1):
            mi = min(nums[i],mi)
            ma = max(nums[i],ma)
        
        if ma == mi:
            return True
        gap = (ma-mi) / (right - left)
        
        
        sd = dict()
        for i in range(left,right+1):
            if nums[i] in sd:
                return False
            else:
                sd[nums[i]] = 1
        
        
        elmt = mi
        while elmt < ma:
            if elmt in sd:
                elmt+=gap
            else:
                return False
        
        return True
        
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        ans = [False] * len(l)
        
        for i in range(len(l)):
            ans[i] = self.is_art(nums,l[i],r[i])
        return ans
