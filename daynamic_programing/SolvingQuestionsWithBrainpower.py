class Solution:
    def helper(self, i, q):
        if i>= len(q):
            return 0
        
        if self.memo[i] != -1:
            return self.memo[i]
        
        self.memo[i]= max(q[i][0] + self.helper(i + q[i][1]+1,q), self.helper(i+1,q))
        
        return self.memo[i]
        
    def mostPoints(self, questions: List[List[int]]) -> int:
        self.memo = [-1]*len(questions)
        return self.helper(0,questions)
