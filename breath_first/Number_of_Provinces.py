class Solution:
    def dfs(self,node,isConnected,visited):
        visited.add(node)
        
        for i in range(len(isConnected)):
            if isConnected[node][i] and i not in visited:
                self.dfs(i,isConnected,visited)
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = set() 
        ans = 0
        
        for node in range(len(isConnected)):
            
            if node not in visited:
                ans += 1 
                self.dfs(node, isConnected, visited)
        
    
    
        return ans
