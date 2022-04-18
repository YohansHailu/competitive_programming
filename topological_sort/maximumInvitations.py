class Solution:
    def dfs_max_len(self, cur, rev_graph):
        
        self.visited.add(cur) 
        
        depth = 0
        for nbr in rev_graph[cur]:
            depth = max(depth, self.dfs_max_len(nbr, rev_graph) )
        return 1 + depth
            
         
    def get_max_cycle(self, cur, index, graph, path):
        if cur in path:
            return index - path[cur]
        
        if cur in self.visited:
            return 0
        
        self.visited.add(cur) 
        path[cur] = index
        
        nbr = graph[cur]
        return self.get_max_cycle(nbr, index+1, graph, path)
        
        
    def maximumInvitations(self, graph: List[int]) -> int:
         
        self.visited = set() 
        mituals = 0
        
        # making graphs
        rev_graph = {i:[] for i in range(len(graph))}
        for i in range(len(graph)):
            rev_graph[graph[i]].append(i)
        
        # totoal number of mituals
        for node in graph:
            if node in self.visited: 
                continue
                
            nbr = graph[node]
            if graph[nbr] == node:
                
                idx = rev_graph[node].index(nbr)
                rev_graph[node].pop(idx)
                
                idx = rev_graph[nbr].index(node)
                rev_graph[nbr].pop(idx)
                
                mituals += self.dfs_max_len(node, rev_graph)
                mituals += self.dfs_max_len(nbr, rev_graph)
                
        # find the bigest cycle
        max_cycle = float("-inf")
        for node in graph:
            if node in self.visited:
                continue
                
            path = dict() 
            max_cycle  = max(max_cycle, self.get_max_cycle(node, 0, graph, path))
        
        return max(max_cycle, mituals)
    
    
    
