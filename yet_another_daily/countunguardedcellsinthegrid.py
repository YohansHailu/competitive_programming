class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        blocked = {(i,j) for i,j in  guards + walls}
        visited = set()
        for i,j in guards:
            
            for xi in range(i+1, m):
                if (xi, j) in blocked:
                    break
                visited.add((xi,j))    
                
            for xi in range(i-1, -1, -1):
                if (xi, j) in blocked:
                    break
                visited.add((xi,j))    
            
            for xj in range(j+1, n):
                if (i, xj) in blocked:
                    break
                visited.add((i,xj))    
                
            for xj in range(j-1, -1, -1):
                if (i, xj) in blocked:
                    break
                visited.add((i,xj))    
                
        return m*n - len(visited) - len(blocked)       
