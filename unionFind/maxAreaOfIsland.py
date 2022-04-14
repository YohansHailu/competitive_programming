class Solution(object):
    def find(self, node):
        if self.parent[node] == node:
            return self.parent[node]
        
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node] 
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            return
            
        if self.size[root_a] < self.size[root_b]:
            self.parent[root_a] = self.parent[root_b]
            self.size[root_b] += self.size[root_a]
        else:
            self.parent[root_b] = self.parent[root_a]
            self.size[root_a] += self.size[root_b]
         
        
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.parent = {}  
        self.size = {} 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.parent[(i,j)] = (i,j)
                    self.size[(i,j)] = 1
                
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 0:
                    continue
                    
                dirs = [(0,1),(0,-1),(1,0),(-1,0)]
                for d in dirs:
                    ni = i + d[0]
                    nj = j + d[1]
                    
                    if not( 0 <= ni < len(grid) and 
                           0<= nj < len(grid[0]) ):
                        continue
                    
                    if grid[ni][nj] == 1:
                        node = (i,j) 
                        nbr = (ni,nj) 
                        self.union(node, nbr)
                        
        if len(self.size.values()) == 0:                 
            return 0
        
        return max(self.size.values())         
