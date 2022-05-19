class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        res = ['']
        for i in range(n):
            res = ["0"+bit for bit in res] + ["1"+bit for bit in res[::-1]]
        
        return map(lambda x:int(x,2), res)
