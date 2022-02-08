#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # null at the right
        
        # dumby
        # head left right
        # if left equal to right all nexted if or if right null it done
        # if equal , right go untile not equal or null
        # head will next to right .. left will be right
        
        if head == None:
            return head
       
        dumb = ListNode(0,head)
        head = dumb
        
        while head.next != None:
            start = head.next
            end = start.next
            if end == None or start.val != start.next.val:
                head = head.next
            else:
                while end != None and start.val == end.val:
                    end = end.next
                head.next = end
                
                
        return dumb.next 
                
                
            
            
        
        
