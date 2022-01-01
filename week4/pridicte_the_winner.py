class Solution:
    
   def helper(self,nums, left, right, p1_sum, p2_sum, turn = 2):
        if turn % 2 == 0:
            #players 1 turn
            if right == left:
                return  [p1_sum + nums[left], p2_sum]
            
            f_score = self.helper(nums,left+1,right,p1_sum+nums[left],p2_sum,turn+1)
            s_score = self.helper(nums,left,right-1,p1_sum+nums[right],p2_sum,turn+1)
            
            return f_score if f_score[0] >= s_score[0] else s_score;
            
        else:
            #player 2s turn
            if right == left:
                return  [p1_sum,p2_sum + nums[left] ]
            
            f_score = self.helper(nums,left+1,right,p1_sum,p2_sum + nums[left],turn+1)
            s_score = self.helper(nums,left,right-1,p1_sum,p2_sum + nums[right],turn+1)
            
            return f_score if f_score[1] >= s_score[1] else s_score;
            
   def PredictTheWinner(self, nums: List[int]) -> bool:
    optimal_score = self.helper(nums,0,len(nums)-1,0,0,2)
    return optimal_score[0] >= optimal_score[1]
    
 
