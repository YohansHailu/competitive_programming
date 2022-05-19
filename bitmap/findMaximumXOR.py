class Solution:
    def add(self, root, num):
        cur = root
        for i in range(32, -1, -1):
            bit = (num & 1<<i) >> i
            if bit not in cur:
                cur[bit] = {}
            cur = cur[bit]
    
    def find_closest(self, root, num):
        cur = root
        path = 0 
        for i in range(32,-1, -1):
            bit = (num & 1<<i) >> i
            if bit not in cur:
                bit ^= 1
            path |= bit << i
            cur = cur[bit]
            
        return path        
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = {}
        for num in nums:
            self.add(root, num)
        res = 0 
        for num in nums:
            closest = self.find_closest(root, ~num)
            res = max(res, num ^ closest)
            
        return res 
