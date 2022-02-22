class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for i in nums:
            count[i] = count.get(i,0) + 1

        tw = 0
        ans = []
        
        d = [ [] [] [] ]
        d.sort(key = lambda x: x[1])
        
        while tw <k:
            max_value = None 
            max_count = -1
            for i in count:
                if count[i] > max_count:
                    max_count = count[i]
                    max_value = i
            ans.append(max_value)
            tw+=1
            count[ max_value ] = -1

        return (ans)
