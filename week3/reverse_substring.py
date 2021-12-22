class Solution:
    def reverse(self,arr,left,right):
        
        mid = (right - left)//2
        for i in range(0,mid+1):
            arr[left+i],arr[right-i] = arr[right-i],arr[left+i]

        
        
    def reverseParentheses(self, s: str) -> str:
        stack = list()
        slist = list(s)
        
      
        i = 0
        while i < len(slist):
            if slist[i] == "(":
                stack.append(i)
                i += 1
            elif slist[i] == ")":
                left = stack.pop()
                right = i
                self.reverse(slist,left+1,right-1)
                
                slist.pop(right)
                slist.pop(left)
                i-=1
               
            else:
                i += 1
            
        return "".join(slist)
            
        
