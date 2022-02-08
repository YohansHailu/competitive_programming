class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        ## constract prefix matrix
        self.pre_mat = []
        for row in range(len(self.matrix)):
            self.pre_mat.append([0])
            for col in range(len(self.matrix[row])):
                self.pre_mat[row].append(self.pre_mat[row][-1] + self.matrix[row][col])
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        while row1 <= row2:
            ans += self.pre_mat[row1][col2+1] - self.pre_mat[row1][col1]
            row1 += 1
        return ans 
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
