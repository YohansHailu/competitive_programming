class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        visited = set()
        
        que = deque()
        que.append( start )
        visited.add( start ) 
        
        while len(que) > 0:
            
            cur = que.popleft()
            visited.add( cur ) 
            
            if arr[cur] == 0:
                return True
            
            
            if 0 <= cur  + arr[cur] < len(arr) and cur + arr[cur] not in visited:
                que.append( cur + arr[cur] )
            
            if 0 <= cur  - arr[cur] < len(arr) and cur - arr[cur] not in visited:
                que.append( cur - arr[cur] )
         
        return False
            
        
