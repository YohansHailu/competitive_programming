class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        size = 0
        cur = head
        while cur != None:
            size += 1
            cur = cur.next
        if(n == size):
            return head.next
        cur = head
        for _ in range(size-n-1):
            cur = cur.next
        cur.next = cur.next.next
        return head
