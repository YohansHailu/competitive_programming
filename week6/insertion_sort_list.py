class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dumb = ListNode()
        sorted_list = dumb
        
        while head != None:
            
            temp = sorted_list
            while temp.next != None and head.val > temp.next.val:
                temp = temp.next
            f = head.next
            head.next = temp.next
            temp.next = head
            head = f
        return dumb.next
  
