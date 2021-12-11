class Solution(object):
    
    def Comp(self,x,y):
        if len(x) == len(y):
            return cmp(x,y)
        
        else: return cmp(x+y,y+x)
       
        
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        allzero = True
        for i in nums:
            if i != 0:
                allzero = False;
        
        if allzero == True:
            return "0"
        
        
        s = list(map(str,nums))
        
        s.sort(cmp=lambda x,y:self.Comp(x,y))
        
        s.reverse()
        st = "".join(s)
        
      
        
        return st
