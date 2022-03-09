class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()
        arrows = 0
        i = 0
        while i < len(points):
            end = points[i][1]
            arrows += 1
            
            while i < len(points) and points[i][0] <= end:
                end = min(end,points[i][1])
                i += 1
                
        return arrows
            
        
