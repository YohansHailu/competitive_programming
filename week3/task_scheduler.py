class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = dict()
        max_count = 0
        
        for elmt in tasks:
            count[elmt] = count.get(elmt,0) + 1
            max_count = max(max_count,count[elmt])
        
        maxs = 0
        for i in count:
            if count[i] == max_count:
                maxs += 1
        
        slots = (max_count - 1) * n
        #one more slot for maxs
        
        if maxs > 1:
            slots += maxs - 1
            
        idles = slots - (len(tasks) - max_count)
        
        
        if idles < 0:
            return len(tasks)
        else:
            return len(tasks) + idles
