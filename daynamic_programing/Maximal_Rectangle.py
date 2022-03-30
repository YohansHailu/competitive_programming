class Solution:
    def make_right_one_memo(self, matrix):
        # here is the dp
        memo = dict()
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])-1,-1,-1):
                if matrix[i][j] != "1":
                    count = 0
                    continue
                count += 1
                memo[(i,j)] = count
            count = 0    
        return memo       
                
    
    def cal_rect_area(self, point, matrix):
        i, j = point
        height = 1
        mn_width = float("+inf")
        area = float("-inf")
        
        while i >= 0:
            if matrix[i][j] != '1':
                break
            width = self.right_ones_memo[(i,j)]
            mn_width = min(mn_width, width)
            area = max(area, mn_width * height)
            
            height += 1
            i -= 1
            
        return area 
        
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        count = 0 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != '1':
                    break
                    
                count += 1
                    
        if count == len(matrix) * len(matrix[0]):
            return count
                    
        self.right_ones_memo = self.make_right_one_memo(matrix)
        mx = 0 
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    area = self.cal_rect_area((i,j), matrix)
                    mx = max(mx, area)
        return mx         
