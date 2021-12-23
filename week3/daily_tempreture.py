class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        
        ans = [0]*len(temperatures)
        st  = []
        
        st.append(0)
        for i in range(1,len(temperatures)):
            
            while len(st)>0 and temperatures[st[-1]] < temperatures[i]:
                
                topIndex = st.pop()
                
                ans[topIndex] = i - topIndex
                
            st.append(i)
            
   
            
        return ans
