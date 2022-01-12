class Solution:
    def recuresive(self,cur_pos,arr,k):
        if len(arr) == 1:
            return arr[0]

        cur_pos += k
        cur_pos %= len(arr)
        arr.pop(cur_pos)
        cur_pos %= len(arr)
        
        return self.recuresive(cur_pos,arr,k) 

    def findTheWinner(self, n: int, k: int) -> int:
        
        return self.recuresive(0,list(range(1,n+1)),k-1)
