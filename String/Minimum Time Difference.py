class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort(key= lambda elt:int(elt[:2])*60 + int(elt[-2:]))
        
        mn = float("+inf")
        for i in range(1, len(timePoints)):
            cur = int(timePoints[i][:2])*60 + int(timePoints[i][-2:])
            prev = int(timePoints[i-1][:2])*60 + int(timePoints[i-1][-2:])
            
            mn = min(mn,cur - prev)
            
        cur = int(timePoints[-1][:2])*60 + int(timePoints[-1][-2:])
        prev = int(timePoints[0][:2])*60 + int(timePoints[0][-2:])
        mn = min(mn,24*60 - (cur - prev))
        
        return mn    
