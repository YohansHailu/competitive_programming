class Solution:
    def make_graph(self, recipes, ings):
        graph = dict()
        
        for i in range(len(recipes)):
            for j in range(len(ings[i])):
                
                if ings[i][j] not in graph:
                    graph[ings[i][j]] = []
                    
                graph[ings[i][j]].append(recipes[i])
         
        return graph 
    
    def findAllRecipes(self, recipes, ings, supplies):
        
        # make graph 
        # if in recipe yes
        #if in resource done
        
        graph = self.make_graph(recipes, ings)
        supplies = set(supplies) 
        recipes = set(recipes) 
        
        
        
        # make indgree
        res = set()
        in_digree = {node:0 for node in supplies}
        
        for node in graph:
            for ch in graph[node]:
                
                if ch not in in_digree:
                    in_digree[ch] = 0
                    
                in_digree[ch] += 1
        
        que = deque()
        for node in in_digree:
            if in_digree[node] == 0:
                que.append(node)
                
        while len(que) > 0:
            cur = que.popleft()
            
                
            if cur in recipes:
                res.add(cur)
                
            if cur not in supplies and cur not in recipes: 
                continue
                
            if cur not in graph:    
                continue
                
            for nbr in graph[cur]:
                
                in_digree[nbr] -= 1
                if in_digree[nbr] == 0:
                    que.append(nbr)
               
        return res    
            
            
