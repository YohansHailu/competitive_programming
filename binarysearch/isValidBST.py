class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            
            left_valied,left_max,left_min = helper(root.left) if root.left != None else (True,root.val,root.val)
            right_valied,right_max,right_min = helper(root.right) if root.right != None else (True,root.val,root.val)
            
            valied = True 
            
            if root.left:
                valied = valied and left_valied and root.val > left_max 
                
            if root.right:
                valied = valied  and right_valied and root.val < right_min
               ## max , mi 
                
            print(root.val, left_max,right_max,"is valied",valied)
            return (valied,right_max,left_min)
      
        return helper(root)[0]
