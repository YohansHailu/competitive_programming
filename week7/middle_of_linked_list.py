class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        slow = head
        fast = head
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
       
        if fast.next == None:
            return slow
        
        return slow.next
