class Solution:

    def get_less_thans(self, nums, val):

        count = 0
        for i in nums:
            if i < val:
                count += 1
        return count

    def findDuplicate(self, nums):

        left = 1
        right = len(nums) - 1
        ans = 0

        while left <= right:

            mid = (left + right)//2
            less_thans = self.get_less_thans(nums, mid)

            if less_thans < mid:
                ans = mid
                left = mid + 1
            else: 
                right = mid - 1

        return ans 
