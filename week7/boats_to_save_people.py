    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k modulo by size
        nums2 = [] 
        for i in nums:
            nums2.append(i)
        
        for i in range(len(nums)):
            nums[(i+k)%len(nums)] = nums2[i]
