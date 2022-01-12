class Solution:
    def trap(self, heights: List[int]) -> int:
        max_left = [0]*len(heights);
        cur_max = heights[0]
        
        for i in range(len(heights)):
            cur_max = max(cur_max,heights[i])
            max_left[i] = cur_max
        
        max_right = [0]*len(heights)
        cur_max = heights[len(heights)-1]
        
        for i in range(len(heights)):
            cur_max = max(cur_max, heights[len(heights)-1-i])
            max_right[len(heights)-1-i] = cur_max
        
        water = 0
        
        for i in range(len(heights)):
            water += min(max_left[i],max_right[i]) - heights[i]
        
        return water
            
        
