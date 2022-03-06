class Solution:
    def lca_helper(self, root, depth):
        
        if root.left == None and root.right == None:
            return (root, depth)
           
        left_depth = -1*sys.maxsize 
        if root.left:
            left_anc, left_depth = self.lca_helper(root.left, depth+1)
            
        right_depth = -1*sys.maxsize 
        if root.right:
            right_anc, right_depth = self.lca_helper(root.right, depth+1)
        
        if left_depth == right_depth:
            return(root, left_depth)
        
        mdepth = max(left_depth, right_depth)
        mdepth_anc = left_anc if left_depth > right_depth else right_anc
        
        return (mdepth_anc, mdepth)
        
        
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        return self.lca_helper(root,0)[0]
