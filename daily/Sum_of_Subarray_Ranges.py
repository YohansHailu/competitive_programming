        ans = 0 
        
        for i in range(len(nums)):
            mx = nums[i]
            mn = nums[i]
            for j in range(i, len(nums)):
                
                if nums[j] > mx:
                    mx = nums[j]
                    
                if nums[j] < mn:
                    mn = nums[j]
                    
                ans += mx - mn 
                
        return ans
