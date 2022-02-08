class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node_list = []
        
        cur = head
        
        while cur != None:
            node_list.append(cur)
            cur = cur.next
            node_list[-1].next=None
        
        node_list.sort(key = lambda x:x.val)
        dumb = ListNode()
        cur = dumb
        
        for node in node_list:
            cur.next = node
            cur = cur.next
        
        return dumb.next
        
