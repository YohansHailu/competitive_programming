class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.k = k
        if len(nums) - k > 0:
            self.minh = nums[len(nums)-k:] # hold top k
        else:
            self.minh = nums
            
        heapify(self.minh)
        

    def add(self, val: int) -> int:
        # holes the top k in min heap
        
        if len(self.minh) < self.k:
            heappush(self.minh,val)
            
        elif val > self.minh[0]:
            heappop(self.minh)
            heappush(self.minh,val)
            
        return self.minh[0]
