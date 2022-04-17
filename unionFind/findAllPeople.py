class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # heap problem
        secret_set = {0,firstPerson}
        minheap = []
        for x,y, time in meetings:
            heappush(minheap, (time, x, y) )
        
        while len(minheap) > 0:
            conc = []
            time, x, y = heappop(minheap)
            conc.append((x,y))
                
            while len(minheap) > 0 and minheap[0][0] == time:
                time, x, y = heappop(minheap)
                conc.append((x,y))
                
            for x, y in conc:
                if x in secret_set or y in secret_set:
                    secret_set.add(x);secret_set.add(y)
                    
            for x, y in reversed(conc):
                if x in secret_set or y in secret_set:
                    secret_set.add(x);secret_set.add(y)
            
            for x, y in conc:
                if x in secret_set or y in secret_set:
                    secret_set.add(x);secret_set.add(y)
                    
        return secret_set
