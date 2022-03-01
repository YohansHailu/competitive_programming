class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        
        if len(root.children) == 0:
            return 1
        
        return max( [self.maxDepth(ch_node) for ch_node in root.children]) + 1
