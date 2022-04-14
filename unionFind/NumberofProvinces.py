class Solution(object):
    def find_root(self, node):
        
        if self.parent[node] == node:
            return node
        
        self.parent[node] = self.find_root(self.parent[node])
        return self.parent[node]
        
    def union(self, a, b):
        a_root = self.find_root(a) 
        b_root = self.find_root(b) 
        
        if a_root == b_root: 
            return 
            
        if self.size[a_root] < self.size[b_root]:
            self.parent[a_root] = self.parent[b_root]
            self.size[b_root] += self.size[a_root]
        else:
            self.parent[b_root] = self.parent[a_root]
            self.size[a_root] += self.size[b_root]
        
        
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
       
        # no seting if they are on the same team
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    self.union(i, j)
        
        count = 0
        for i in range(len(self.parent)):
            if self.parent[i] == i:
                count += 1
                
        return count
