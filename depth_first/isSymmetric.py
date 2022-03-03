class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        que = deque()
        que.append(root) 
        
        while len(que) > 0:
            
            for _ in range(len(que)):
                
                cur = que.popleft()
                if cur == None:
                    continue
                que.append( cur.left )
                que.append( cur.right )
            
            que_list = [i.val if i != None else None for i in que]
            
            if que_list != que_list[::-1]:
                return False
            
        return True
        
