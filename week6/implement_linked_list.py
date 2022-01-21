lass node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        

    def get(self, index: int) -> int:
        head = self.head
        i = 0
        while head != None and i < index:
            head = head.next
            i += 1
            
        if head == None:
            return -1
        
        return head.val
    
    def addAtHead(self, val: int) -> None:
        new_node = node(val,self.head)
        self.head = new_node
        if self.tail == None:
            self.tail = self.head
        

    def addAtTail(self, val: int) -> None:
        new_node = node(val)
        
        if self.tail == None:
            self.tail = new_node
            self.head = self.tail
        else:    
            self.tail.next = new_node
            self.tail = new_node
    
    
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.head = node(val,self.head)
            return;
            
        head = self.head
        i = 0
        while head != None and  i < index-1:
            head = head.next
            i += 1
        if head != None:
            new_node = node(val)    
            new_node.next = head.next
            head.next = new_node
            if new_node.next == None:
                self.tail = new_node 
        return;
        
    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return;
        
        head = self.head
        i = 0
        while head != None and  i < index-1:
            head = head.next
            i += 1
        
        if head == None:
            return
        
        if head.next != None:
            head.next = head.next.next
            if head.next == None:
                self.tail = head
        return;

