class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(lambda x,y: cmp(x[0],y[0]))
        
        result = [ [intervals[0][0],intervals[0][1]] ]
        
        rIndex = 0;
        for inIndex in range(1,len(intervals)):
            
            left = result[rIndex][0]
            right = result[rIndex][1]
            
            begin = intervals[inIndex][0]
            endOfint = intervals[inIndex][1]
            
            if( left<= begin<= right ):
                result[rIndex][1] = right if right >= endOfint else endOfint 
            else:
                result.append(intervals[inIndex])
                rIndex+=1;
        
        return result
