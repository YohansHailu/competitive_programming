class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        size = 0
        cur = head
        while cur != None:
            size+=1
            cur = cur.next
        
        mid = head
        for i in range(size//2):
            mid = mid.next
            
        node_stack = []
        while mid != None:
            node_stack.append(mid)
            mid = mid.next
        
        ans = head.val + node_stack[-1].val
        while len(node_stack)>0:
            poped = node_stack.pop()
            ans = max(ans,head.val+poped.val)
            head = head.next
        return ans
