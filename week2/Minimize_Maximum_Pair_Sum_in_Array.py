    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        
        n = len(nums)//2
        max_psum = nums[0] + nums[len(nums)-1]
        
        for i in range(0,n+1):
            psum = nums[i] + nums[len(nums)-1-i]
            if psum>max_psum:
                max_psum = psum
        
        return max_psum
        
