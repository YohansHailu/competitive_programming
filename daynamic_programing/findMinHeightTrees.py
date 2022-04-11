class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1: 
            return [0]
        
        graph = {node:[] for node in range(n)}
        
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            
        in_degree = {node:0 for node in range(n)}
        
        for node in graph:
            for nbr in graph[node]:
                in_degree[nbr] += 1
                
        
        que = deque()
        for node in in_degree:
            if in_degree[node] == 1:
                que.append(node)
                
        node_set = set(in_degree)        
        while len(node_set) > 2:
            for _ in range(len(que)):
                cur = que.popleft()
                node_set.remove(cur)
                for nbr in graph[cur]:
                    in_degree[nbr] -= 1

                    if in_degree[nbr] == 1:
                        que.append(nbr)
            
        return que 
