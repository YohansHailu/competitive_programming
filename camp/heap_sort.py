class Solution:
    def leftChild(self,index):
        return 2*index + 1
    def rightChild(self,index):
        return 2*index +2
    def parent(self,index):
        return (index - 1)//2
    def getMin(self,arr):
        return arr[0]

    def heapify(self,arr, n, i):
        while(True):
            smallest = i
            left = self.leftChild(i)
            right = self.rightChild(i)
            
            if left < n and arr[left] < arr[i]:
                smallest = left

            if right < n and arr[right] < arr[smallest]:
                smallest = right

            if smallest == i:
                break
            else: 
                arr[smallest],arr[i] = arr[i], arr[smallest]
            i = smallest

    def insert(self,arr,n,item):
        arr[n-1] = item;
        
        i  = n-1
        p =  self.parent(i)
        while arr[i] < arr[p]:
            arr[p], arr[i] = arr[i], arr[p]
            if p == 0:
                break;
            i = p
            p =  self.parent(i)

    def remove(self,arr):
        if self.n == 0:
            return

        arr[0],arr[ self.n-1 ] = arr[self.n-1],arr[0]
        self.n -= 1
        self.heapify(arr,self.n,0)

    def buildHeap(self,arr,n):
        for i in range(len(arr)):
            self.heapify(arr, len(arr), len(arr)-i-1);

    def HeapSort(self, arr, n):
        self.n = n
        for i in range(n):
            arr[i] *= -1

        self.buildHeap(arr,n)
        for i in range(len(arr)):
            self.remove(arr)

        for i in range(n):
            arr[i] *= -1
