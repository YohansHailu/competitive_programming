class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # we go level by level
        # regiter max time
        graph = {node:[] for node in range(1,n+1)}
        indigree = {node:0 for node in range(1,n+1)}
        life = [0]*n
        
        for start, end in relations:
            graph[start].append(end)
            indigree[end] += 1
        
        que = deque()
        for node in indigree:
            if indigree[node] == 0:
                que.append(node)
                life[node-1] = time[node-1]
        
        while len(que) > 0:
            cur = que.popleft()
            for nbr in graph[cur]:
                
                life[nbr-1] = max(life[nbr-1], life[cur-1] + time[nbr-1])
                
                indigree[nbr] -= 1
                if indigree[nbr] == 0:
                    que.append(nbr)
                
        return max(life)    
