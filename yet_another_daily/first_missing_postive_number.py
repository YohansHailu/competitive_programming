class Solution:
    def mark(self, arr, val):
        #  1 indexed
        if val == "marked" or val <= 0 or val > len(arr):
            return;
        if arr[val - 1] != "marked":
            temp = arr[val - 1]
            arr[val - 1] = "marked"
            self.mark(arr, temp) 
        
    def firstMissingPositive(self, nums: List[int]) -> int:
        # make them zero cascadingly
        # offcet by one
        for i in range(len(nums)):
            self.mark(nums, nums[i])
        for i in range(len(nums)):
            if nums[i] != "marked":
                return i + 1
        return len(nums) + 1
         
