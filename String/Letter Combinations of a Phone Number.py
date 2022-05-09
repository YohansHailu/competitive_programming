class Solution:
    def helper(self, s, i, digits):
        
        if i == len(digits):
            self.ans.append("".join(s))
            return
        
        for c in self.map[digits[i]]:
            s.append(c)
            self.helper(s,i+1, digits)
            s.pop()
        
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        self.map = {'2':"abc", 
                    '3':"def", 
                    '4':"ghi", 
                    '5':"jkl", 
                    '6':"mno", 
                    '7':"pqrs", 
                    '8':"tuv", 
                    '9':"wxyz"}
         
        self.ans = []
        self.helper([], 0, digits)
        
        return self.ans 
