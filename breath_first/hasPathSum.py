class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root == None:
            return False
        
        if targetSum - targetSum < 0: 
            return False
            
        if targetSum - root.val == 0: 
            if root.left == None and root.right == None:
                return True 
        
        
        return self.hasPathSum(root.left,targetSum - root.val) or self.hasPathSum(root.right,targetSum - root.val)
        
