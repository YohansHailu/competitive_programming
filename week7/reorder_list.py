    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find the mid 

        size = 0
        temp = head
        while temp != None:
            size += 1
            temp = temp.next
        
        before_mid = head
        for _ in range(size//2 -1 + size%2):
            before_mid = before_mid.next
        
        mid = before_mid.next
        before_mid.next = None
        
        #put to stack
        node_stack = list()
        while mid != None:
            go_m = mid.next
            mid.next = None
            node_stack.append(mid)
            mid = go_m
                
        t_head = head
        while len(node_stack) > 0:
            go_h = head.next
            poped = node_stack.pop()
            poped.next = head.next
            head.next = poped
            head = go_h
            
            
        
