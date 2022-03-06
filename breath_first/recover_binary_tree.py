class Solution:
    def inorder(self, root, arr):
        if root == None:
            return
        
        self.inorder(root.left, arr)
        
        arr.append(root)
        
        self.inorder(root.right, arr)
        
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = [] 
        self.inorder(root, arr)
        sorted_arr = arr.copy()
        sorted_arr.sort(key  = lambda x: x.val)
        
        first_node = None 
        for i in range(len(arr)):
            if arr[i].val == sorted_arr[i].val:
                continue
                
            if first_node == None:
                first_node = arr[i]
            else:
                first_node.val, arr[i].val = arr[i].val, first_node.val
            
            
            
             
        
