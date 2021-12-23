class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        ndict = dict()
        gStack = list();
        
        gStack.append(nums2[0])
        for i in nums2[1:]:
        
            if len(gStack) > 0 :
                t = gStack[-1]
                while t < i and len(gStack) > 0:
                    ndict[gStack.pop()] = i
                    if len(gStack) > 0:
                        t = gStack[-1]

            gStack.append(i)

        
        for i in gStack:
            ndict[i] = -1
            
                
        ans = []
        
        for i in nums1:
            ans.append(ndict[i])
        
        return ans
            
        
     
            
        
