
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        cur = root
        
        while(cur != None):
            if cur.val == val:
                return cur
            elif val > cur.val:
                cur = cur.right
            elif val < cur.val:
                cur = cur.left
                
        return None 
