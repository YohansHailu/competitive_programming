class Solution:
    def bob_helper(self, cur_arrows, cur_index, ans):
        if cur_index == len(self.aliceArrows):
            if cur_arrows > 0:
                ans[1][0] += cur_arrows
            return ans
        
        score, res_arr = ans[0], ans[1].copy()
        res = self.bob_helper(cur_arrows, cur_index+1, (score, res_arr) )
        
        
        arrow_cost = self.aliceArrows[cur_index] + 1
        new_arrow = cur_arrows - arrow_cost
        
        if new_arrow >= 0: 
        
            score, res_arr = ans[0], ans[1].copy()
            score += cur_index
            res_arr[cur_index] = arrow_cost 
            
            res_taken = self.bob_helper(new_arrow, cur_index+1,(score, res_arr) )
            
            res = res if res[0] > res_taken[0] else res_taken
            
        return res 
    
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        
        self.aliceArrows = aliceArrows
        ans = ( 0, [0]*len(aliceArrows) )
        res = self.bob_helper(numArrows, 0, ans)
        
        return res[1]
