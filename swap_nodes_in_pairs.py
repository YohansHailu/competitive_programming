class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dumb = ListNode()
        dumb.next = head
        prev = dumb
        
        while head!= None and head.next != None:
            temp_last = head.next.next
            temp_next = head.next

            head.next = temp_last
            temp_next.next = head
            prev.next = temp_next

            prev = head
            head = prev.next
        
        return dumb.next
