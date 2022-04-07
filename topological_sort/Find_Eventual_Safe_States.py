class Solution:
    def dfs(self, node, graph, path):
        
        if node in self.visited: 
            return self.visited[node]
        
        nbrs = graph[node] 
        if nbrs == []:
            self.ans.add(node)
            return True
        
         
        for nbr in nbrs:
            
            if nbr in path:
                return False
            
            path.add(nbr)
            
            if self.dfs(nbr, graph, path) == False:
                self.visited[node] = False 
                return False
            
            path.remove(nbr)
            
        self.visited[node] = True
        
        self.ans.add(node)    
        return True
            
        
        
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        self.ans = set() 
        self.visited = {} 
        
        for i in range(len(graph)):
            if i not in self.visited:
                self.dfs(i, graph, set([i]))
        
        return sorted(list(self.ans))
