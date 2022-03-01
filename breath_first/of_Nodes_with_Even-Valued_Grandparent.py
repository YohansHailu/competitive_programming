class Solution:
    def evenGraph_helper(self, node, grand_val, par_val):
        
        if node == None:
            return 0
        
        left_sum = self.evenGraph_helper(node.left, par_val, node.val)
        right_sum = self.evenGraph_helper(node.right, par_val, node.val)
        
        node_sum = left_sum + right_sum 
        if grand_val != None and grand_val % 2 == 0:
            node_sum += node.val 
        
        return node_sum
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        return self.evenGraph_helper(root,None,None)
