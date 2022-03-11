  def max_rob(self, index, can_rob, memo, nums):

      if index >= len(nums):
          return 0

      if memo[index][can_rob] != None:
          return memo[index][can_rob]

      if can_rob == False:
          memo[index][can_rob] = self.max_rob(index+1, True, memo, nums)
          return memo[index][can_rob] 

      not_robed = self.max_rob(index+1,  True, memo, nums)
      robed = nums[index]  + self.max_rob(index+1, False, memo, nums)

      memo[index][can_rob] = max(robed, not_robed)
      return memo[index][can_rob] 

  def rob(self, nums: List[int]) -> int:
      memo = [ [None  for _ in range(2)] for _ in range(len(nums))  ] 
      return self.max_rob(0, True, memo, nums)
