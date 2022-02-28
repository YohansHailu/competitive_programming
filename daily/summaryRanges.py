def summaryRanges(self, nums: List[int]) -> List[str]:
    ans = [] 
    left = 0 
    right = 0
    while right < len(nums):

        while right+1 < len(nums) and nums[right+1] == nums[right]+1: #check this latter
            right += 1


        if left == right:  
            ans.append(f"{nums[left]}")
        else:
            ans.append(f"{nums[left]}->{nums[right]}")

        right += 1 
        left = right

    return ans
