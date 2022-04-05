class Solution:
    def goodDaysToRobBank(self, arr: List[int], time: int) -> List[int]:
        
        dec = [0]
        inc = [0]
        
        n = len(arr) - 1
        for i in range(1, len(arr)):
            dec.append(dec[-1] + 1 if arr[i] <= arr[i-1] else 0)
            inc.append(inc[-1] + 1 if arr[n-i] <= arr[n-i+1] else 0)
            
        inc.reverse() 
        
        res = []
        for i in range(len(arr)):
            if min(inc[i], dec[i]) >= time:
                res.append(i)
                
        return res
