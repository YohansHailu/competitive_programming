class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freqDict = Counter(words)
        freqh = []
        for i in freqDict:
            heappush(freqh, (-1*freqDict[i],i) )
        
        ans = []
        for i in range(k):
            ans.append(heappop(freqh))
            
        return [i[1] for i in ans]
