class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pre = [0]
        for elt in nums: 
            pre.append(pre[-1]+elt)
            
        res = float("inf") 
        que = deque()
        for i in range(len(pre)):
            
            while len(que) > 0 and pre[i] < pre[que[-1]]:
                que.pop()
                
            que.append(i)
            
            while len(que) > 0 and pre[que[-1]] - pre[que[0]] >= k:
                res = min(res, que[-1] - que[0])
                que.popleft()
        
        return res if res != float("inf") else -1
