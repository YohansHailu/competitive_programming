class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        cur = 0
        left = 0
        right = 0
        
        while right < len(nums):
            while right < len(nums) and nums[left] == nums[right]:
                right+=1;
            if right < len(nums):
                left = right
                cur += 1
                nums[cur] = nums[right]
        
        return cur+1
