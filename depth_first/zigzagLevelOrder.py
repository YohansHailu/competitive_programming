class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return [] 
        
        ans = []
        
        que = deque()
        que.append( root )
        
        level = 0 
        while len(que) > 0:
            
            qlist = [i.val for i in que]
            
            if level % 2 != 0:
                qlist.reverse()
                
            ans.append(qlist)
            
            for _ in range(len(que)):
                cur = que.popleft()
                
                if cur.left: que.append(cur.left);
                if cur.right: que.append(cur.right);
            
            level += 1
        
        return ans
