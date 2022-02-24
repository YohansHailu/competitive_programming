    def binarysearch(self,nums,target,leftmost):
        
        best = -1
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                best = mid
                if leftmost == True:
                    right = mid - 1
                else:
                    left = mid + 1
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid-1
            
        return best 
        
        
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       
        findex = self.binarysearch(nums,target,True)
        sindex = self.binarysearch(nums,target,False)
        
        return [findex,sindex]
