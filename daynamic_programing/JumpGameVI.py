class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        maxheap = [] 
        dp = [-1]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            
            while maxheap and maxheap[0][1] > i+k:
                heappop(maxheap)
                
            cur = nums[i] + (-1*maxheap[0][0] if maxheap else 0)
            dp[i] = cur
            heappush(maxheap, (-1*dp[i], i))
        
        return dp[0]
