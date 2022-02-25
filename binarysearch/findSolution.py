class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        # for each x i will go y binary search
        ans = []
         
        n = 1000 
        for x in range(1,n+1):
            
            left = 1
            right = n 
            
            while left <= right:
                mid = left+(right-left)//2
                
                result = customfunction.f(x,mid)
                if result == z:
                    ans.append([x,mid])
                    break 
                elif result > z:
                    right = mid - 1
                elif result < z:
                    left = mid + 1
        return ans
