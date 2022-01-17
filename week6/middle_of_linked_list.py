class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        size = 0
        while cur != None:
            size += 1
            cur = cur.next
        
        for _ in range(size//2):
            head = head.next
        
        return head
        
