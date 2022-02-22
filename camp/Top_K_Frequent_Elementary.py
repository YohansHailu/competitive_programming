class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = Counter(nums)
        
        ans = [] 
        
        for val in freqDict:
            if len(ans) < k:
                heappush(ans, (freqDict[val], val) )
                continue
            
            heappushpop(ans,(freqDict[val], val))
            
        return [i[1] for i in ans]
        
        
        
