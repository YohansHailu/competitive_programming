class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = [] 
        
        que = deque()
        que.append( root )
        
        while len(que) > 0:
            
            ans.append( sum([i.val for i in que]) / len(que) )
            for _ in range(len(que)):
                
                cur = que.popleft()
                
                if cur.left: que.append(cur.left)
                if cur.right: que.append(cur.right)
                    
        
        return ans
