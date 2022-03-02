class Solution:
    def dfs_make_x(self,board, i, j):
        board[i][j] = "X"
        for d in range( len(self.Dir) - 1 ):
            ni = i + self.Dir[d]
            nj = j + self.Dir[d+1]
            
            if not self.is_in_range(ni,nj):
                continue

            if board[ni][nj] != "O":
                continue
                
            self.dfs_make_x(board, ni, nj)
            
    def dfs_to_set(self,board, i, j, dset):
        dset.add( (i,j) )
        
        for d in range( len(self.Dir) - 1 ):
            ni = i + self.Dir[d]
            nj = j + self.Dir[d+1]
            
            if not self.is_in_range(ni,nj):
                continue
            if board[ni][nj] != "O":
                continue
            if (ni,nj) in dset:
                continue 
            self.dfs_to_set(board, ni, nj, dset)
        
    def dfs_is_surr(self,board, i, j, visited = set() ):
        
        visited.add( (i,j) ) 
        
        
        for d in range( len(self.Dir) - 1 ):
            ni = i + self.Dir[d]
            nj = j + self.Dir[d+1]
            
            if not self.is_in_range(ni,nj):
                return False
            if board[ni][nj] != "O":
                continue
            if (ni,nj) in visited:
                continue 
                
            res = self.dfs_is_surr(board, ni, nj, visited)
            if res == False:
                return False 
            
        return True 
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.is_in_range = lambda x,y: 0<= x < len(board) and 0<= y < len(board[0])
        self.Dir = (0,1,0,-1,0)
        
        not_sur = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] == "X":
                    continue
                if (i,j) in not_sur:
                    continue
                
                if self.dfs_is_surr(board, i, j):
                    print(i,j)
                    self.dfs_make_x(board, i, j)
                else:
                    self.dfs_to_set(board,i,j,not_sur)
                

        
