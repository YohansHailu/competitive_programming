class Solution: 
    def select(self, arr, i):
        # code here 
        minIndex = i;
        for index in range(i+1,len(arr)):
            if arr[index] < arr[minIndex]:
                minIndex = index
        
        return minIndex
    
    def selectionSort(self, arr,n):
        #code here
        for index in range(len(arr)-1):
            seIndex = self.select(arr,index)
            
            #swap
            temp = arr[index]
            arr[index] = arr[seIndex]
            arr[seIndex] = temp
