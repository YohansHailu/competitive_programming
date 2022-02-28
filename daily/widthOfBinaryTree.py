  def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      que = deque()
      que.append( (root, 0, 0)  ) # (node, index, level)

      ans = 0
      cur_level = 0 

      max_i = 0 
      min_i = 0 

      while len(que)  > 0:

          ans = max(ans, max_i - min_i + 1)

          max_i = None 
          min_i = None 
          while len(que) > 0 and que[0][2] == cur_level:
              node,index,level = que.popleft()
              if node.left:
                  que.append( (node.left, 2*index+1, level+1) )
                  min_i = min(2*index+1,min_i)
                  max_i = max(2*index+1,min_i)
              if node.right:
                  que.append( (node.right, 2*index+2, level+1) )
                  min_i = min(2*index+2,min_i)
                  max_i = max(2*index+2,min_i)

          cur_level += 1

      return ans
