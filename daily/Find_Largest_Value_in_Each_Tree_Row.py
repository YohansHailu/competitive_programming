class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # bfs
        if root == None:
            return []
        
        ans = []
        que = deque()
        que.append(root) 
        
        while len(que) > 0:
            mx =  -1*float("inf") 
            for _ in range(len(que)):
                
                cur = que.popleft()
                mx = max(cur.val, mx) 
                if cur.left: que.append(cur.left)
                if cur.right: que.append(cur.right)
                
            ans.append(mx) 
            
        return ans 
