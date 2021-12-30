class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()
        n = len(citations)
        ans = -1;
        for i in range(n):
            if citations[i] >= n-i:
                ans = max(ans,n-i)
               
        if ans == -1:
            if sum(citations) == 0:
                return 0
            return n
        return ans
        
     
