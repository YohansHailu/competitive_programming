def has_cycle(head):
    has_set = set()
    
    slow = head
    fast = head.next
    
    while fast != None and fast.next != None:
        if slow == fast:
            return 1
        slow = slow.next
        fast = fast.next.next
        
            
    return 0
