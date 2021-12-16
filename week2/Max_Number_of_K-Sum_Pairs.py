    def maxOperations(self, nums: List[int], k: int) -> int:
        difs  = dict()
        ans = 0
        for i in range(len(nums)):
            if nums[i] in difs:
                ans+=1
                difs[nums[i]] -=1
                if difs[nums[i]] <= 0:
                    del difs[nums[i]]
            else:
                d = k - nums[i]
                difs[d] = difs.get(d,0) + 1 
        return ans
            
