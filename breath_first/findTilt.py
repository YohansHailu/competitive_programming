class Solution:
    def find_helper(self,root):
        if root == None:
            return (0,0)
        
        left_t_sum, left_sum = self.find_helper(root.left) 
        right_t_sum, right_sum = self.find_helper(root.right)
        
        
        node_t_sum = abs(left_sum - right_sum)
        
        total_t_sum = left_t_sum + right_t_sum + node_t_sum 
        sub_tree_sum = left_sum + right_sum + root.val
        
        return (total_t_sum, sub_tree_sum)
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        return self.find_helper(root)[0]
