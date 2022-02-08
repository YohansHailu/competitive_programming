class Solution:
    def max_window(self,arr,Len,av_index=-1,av_len=0):
        # av_index -1 to not to do
        f_max = 0
        w_sum = 0
        left = 0
        right = 0
        while right <len(arr):
            if right == av_index:
                right += av_len 
                left = right
                w_sum = 0
                
            if right >= len(arr):
                continue
                
            w_sum += arr[right]
            while (right-left+1) > Len: 
                w_sum -= arr[left]
                left += 1
                
            f_max = max(w_sum,f_max)
            right += 1    
            
        return f_max
    
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        
        ans = 0 
        
        w_sum = sum(nums[0:firstLen]) 
        left = 0 
        right = firstLen 
        while right < len(nums):
            w_sum += nums[right]
            while(right-left+1) > firstLen:
                w_sum -= nums[left];
                left += 1
            s_max = self.max_window(nums,secondLen,left,firstLen)
            ans = max(ans,s_max+w_sum)
            right += 1 
            
        w_sum = sum(nums[0:secondLen]) 
        left = 0 
        right = secondLen 
        while right < len(nums):
            w_sum += nums[right]
            while(right-left+1) > secondLen:
                w_sum -= nums[left];
                left += 1
            s_max = self.max_window(nums,firstLen,left,secondLen)
            ans = max(ans,s_max+w_sum)
            right += 1 
        return ans
