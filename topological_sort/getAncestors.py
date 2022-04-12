class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = {node:[] for node in range(n)}
        
        for start, end in edges:
            graph[start].append(end)
        
        in_digree = {node:0 for node in range(n)} 
        for node in graph:
            for nbr in graph[node]:
                in_digree[nbr] += 1
        
        que = deque()
        for node in in_digree:
            if in_digree[node] == 0:
                que.append(node)
        
        ## final solution
        ansc = [[0] for i in range(n)]
        
        while len(que) > 0:
            cur = que.popleft()
            
            for nbr in graph[cur]:
                ansc[nbr] += [cur]
                ansc[nbr] += ansc[cur] 
                
                in_digree[nbr] -= 1
                if in_digree[nbr] == 0:
                    que.append(nbr)
                    
        for i in range(len(ansc)):
            sort(ansc[i])
            
            
        return ansc    
