class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        f_dict = dict()
        
        for i in arr:
            f_dict[i] = f_dict.get(i,0) + 1
        
        f_list = []
        
        for i in f_dict:
            f_list.append([i,f_dict[i]])
        
        f_list.sort(key = lambda x:x[1],reverse=True)
        
        rem = len(arr)/2
        tf  = 0
        ind = 0
        while tf < rem:
            tf += f_list[ind][1]
            ind+=1
        
        return ind
