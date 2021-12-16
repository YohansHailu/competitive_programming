class Solution:
    def flip(self,arr,n):
        for i in range(0,n//2+1):
            arr[i],arr[n-i] = arr[n-i],arr[i]
    def findmax(self,arr,n):
        maxv = arr[0]
        maxI = 0
        for i in range(0,n+1):
            if arr[i] > maxv:
                maxv = arr[i]
                maxI = i
        return maxI
    
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr)-1,0,-1):
            maxI = self.findmax(arr,i)
            self.flip(arr,maxI)
            self.flip(arr,i)
            ans.append(maxI+1)
            ans.append(i+1)
        return ans
